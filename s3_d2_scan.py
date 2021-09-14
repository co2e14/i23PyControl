import pv
import subprocess
import os
from subprocess import Popen, PIPE
import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import control


def runscan(
    d2_pos_in,
    s3_xsize_set,
    s3_ysize_set,
    s3_x_start,
    s3_x_end,
    x_points,
    s3_y_start,
    s3_y_end,
    y_points,
):
    dt = datetime.now()
    print(
        "Starting beam profile scan at",
        dt.strftime("%H:%M:%s"),
        "on",
        dt.strftime("%d/%m/%y"),
    )
    dt = dt.strftime("%y%m%d_%H%M")

    # store all current values to return to at the end
    d2_y_static = control.ca.caget(pv.d2_y)
    x_size_static = control.ca.caget(pv.s3_xsize + ".RBV")
    y_size_static = control.ca.caget(pv.s3_ysize + ".RBV")
    x_centre_static = control.ca.caget(pv.s3_xcentre + ".RBV")
    y_centre_static = control.ca.caget(pv.s3_ycentre + ".RBV")

    # set x size, y size and move d2 diode in
    control.ca.caput(pv.s3_xsize, float(s3_xsize_set))
    control.ca.caput(pv.s3_ysize, float(s3_ysize_set))
    waitx = control.ca.caget(pv.s3_xsize + ".RBV")
    waity = control.ca.caget(pv.s3_ysize + ".RBV")
    while float(s3_xsize_set) != np.around(float(waitx), 2) and float(
        s3_ysize_set
    ) != np.around(float(waity), 2):
        print(
            "Setting S3 X size to",
            s3_xsize_set,
            "- currently",
            waitx,
            ". Setting S3 Y size to",
            s3_ysize_set,
            "- currently",
            waity,
            end="\r",
        )
        waitx = control.ca.caget(pv.s3_xsize + ".RBV")
        waity = control.ca.caget(pv.s3_ysize + ".RBV")
    else:
        print("XY size set complete\n")
        pass

    control.ca.caput(pv.d2_y, str(d2_pos_in))
    wait = control.ca.caget(pv.d2_y + ".RBV")
    while float(d2_pos_in) != np.around(float(wait), 1):
        print("Moving D2 to", str(d2_pos_in), "- currently", wait, end="\r")
        time.sleep(0.5)
        wait = control.ca.caget(pv.d2_y + ".RBV")
    else:
        print("\nD2 in position, starting X Y grid scan...\n")
        pass

    # move to each x, y value and record d2 current
    x_y_d2cur = []
    for y in np.around(
        np.linspace(float(s3_y_start), float(s3_y_end), float(y_points), endpoint=True),
        2,
    ):
        control.ca.caput(pv.s3_ycentre, str(y))
        y_aim = control.ca.caget(pv.s3_ycentre + ".RBV")
        while float(y_aim) != float(y):
            print("Moving Y centre to", y, "- currently at", y_aim, end="\r")
            time.sleep(0.5)
            y_aim = float(control.ca.caget(pv.s3_ycentre + ".RBV"))
        else:
            print("\nY at", y, end="\r")
            print("")
            pass
        for x in np.around(
            np.linspace(
                float(s3_x_start), float(s3_x_end), float(x_points), endpoint=True
            ),
            2,
        ):
            control.ca.caput(pv.s3_xcentre, str(x))
            x_aim = control.ca.caget(pv.s3_xcentre + ".RBV")
            while float(x_aim) != float(x):
                print("Moving X centre to", x, "- currently at", x_aim, end="\r")
                time.sleep(0.5)
                x_aim = float(control.ca.caget(pv.s3_xcentre + ".RBV"))
            else:
                d2c = control.ca.caget(pv.d2_cur_1)
                print("\nX =", x, "Y =", y, "D2 current =", d2c, end="\n")
                x_y_d2cur.append((x, y, float(d2c)))
                pass

    # return to beginning values
    control.ca.caput(pv.s3_xsize, x_size_static)
    control.ca.caput(pv.s3_ysize, y_size_static)
    time.sleep(0.5)
    waitx = control.ca.caget(pv.s3_xsize_dmov)
    waity = control.ca.caget(pv.s3_ysize_dmov)
    while float(waitx) != float(1) and float(waity) != float(1):
        print(
            "Returning S3 X size to start value",
            x_size_static,
            "and S3 Y size to start value",
            y_size_static,
            end="\r",
        )
        time.sleep(0.5)
        waitx = control.ca.caget(pv.s3_xsize_dmov)
        waity = control.ca.caget(pv.s3_ysize_dmov)
    else:
        print(
            "\nFinished moving X and Y size back to",
            x_size_static,
            "by",
            y_size_static,
            end="\n",
        )
        pass
    control.ca.caput(pv.s3_xcentre, x_centre_static)
    wait = control.ca.caget(pv.s3_xcentre_dmov)
    while float(wait) != float(1):
        print("Returning S3 X centre to start value", x_centre_static, end="\r")
        time.sleep(0.5)
        wait = control.ca.caget(pv.s3_xcentre_dmov)
    else:
        print("\nFinished moving X centre back to", x_centre_static, end="\n")
        pass
    control.ca.caput(pv.s3_ycentre, y_centre_static)
    wait = control.ca.caget(pv.s3_ycentre_dmov)
    while float(wait) != float(1):
        print("Returning S3 Y centre to start value", y_centre_static, end="\r")
        time.sleep(0.5)
        wait = control.ca.caget(pv.s3_ycentre_dmov)
    else:
        print("\nFinished moving Y centre back to", y_centre_static, end="\n")
        pass
    control.ca.caput(pv.d2_y, d2_y_static)
    wait = control.ca.caget(pv.d2_y + ".RBV")
    while np.around(float(wait), 1) != float(d2_y_static):
        print("Returning D2 Y to start value", d2_y_static, end="\r")
        time.sleep(0.5)
        wait = control.ca.caget(pv.d2_y + ".RBV")
    else:
        print("\nFinished movingD2 back to", d2_y_static, end="\n")
        pass

    # generate heatmap of beam
    print("Plotting heatmap, please wait...")
    df = pd.DataFrame(x_y_d2cur, columns=("X", "Y", "D2"))
    df.to_json(dt + ".json")
    df.to_csv(dt + ".csv")
    df = df.pivot("X", "Y", "D2")
    beam_profile = sns.heatmap(df, cmap="coolwarm")
    fig = beam_profile.get_figure()
    fig.savefig(str(dt) + ".png")
    #plt.show()
    print("Finished")
    return(fig)
