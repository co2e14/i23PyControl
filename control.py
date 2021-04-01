#!/bin/env python3
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


class ca:
    def __init__(self):
        print("V0.1")

    def cagetstring(pv):
        val = None
        while val is None:
            try:
                a = Popen(["caget", "-S", pv], stdout=PIPE, stderr=PIPE)
                a_stdout, a_stderr = a.communicate()
                val = a_stdout.split()[1]
                val = str(val.decode("ascii"))
            except:
                print("Exception in ca_py3.py cagetstring maybe this PV aint a string")
                pass
        return val

    def caget(pv):
        val = None
        while val is None:
            try:
                a = Popen(["caget", pv], stdout=PIPE, stderr=PIPE)
                a_stdout, a_stderr = a.communicate()
                val = a_stdout.split()[1].decode("ascii")
                # val = evaluate(val)
                # val = val.decode('ascii')
            except:
                print("Exception in ca_py3.py caget, maybe this PV doesnt exist:", pv)
                pass
        return val

    def caput(pv, new_val):
        check = Popen(["cainfo", pv], stdout=PIPE, stderr=PIPE)
        check_stdout, check_stderr = check.communicate()
        if check_stdout.split()[11].decode("ascii") == "DBF_CHAR":
            a = Popen(["caput", "-S", pv, str(new_val)], stdout=PIPE, stderr=PIPE3)
            a_stdout, a_stderr = a.communicate()
        else:
            a = Popen(["caput", pv, str(new_val)], stdout=PIPE, stderr=PIPE)
            a_stdout, a_stderr = a.communicate()

class control:
    def __init__(self):
        print("V0.1")

    def get_value(self, pv):
        subprocess.run(("caget", pv))

    def push_value(self, pv):
        subprocess.run(("caput", pv))


if __name__ == "__main__":
    # get date and time of run
    dt = datetime.now()
    print(
        "Starting beam profile scan at",
        dt.strftime("%H:%M:%s"),
        "on",
        dt.strftime("%d/%m/%y"),
    )
    dt = dt.strftime("%y%m%d_%H%M")

    # store all current values to return to at the end
    d2_y_static = ca.caget(pv.d2_y)
    x_size_static = ca.caget(pv.s3_xsize + ".RBV")
    y_size_static = ca.caget(pv.s3_ysize + ".RBV")
    x_centre_static = ca.caget(pv.s3_xcentre + ".RBV")
    y_centre_static = ca.caget(pv.s3_ycentre + ".RBV")
    s3_xsize_set = 0.1
    s3_ysize_set = 0.1

    # set x size, y size and move d2 diode in
    ca.caput(pv.s3_xsize, 0.1)
    print("trying to move")
    wait = ca.caget(pv.s3_xsize + ".RBV")
    while float(s3_xsize_set) != float(wait):
        print("Setting S3 X size to", s3_xsize_set, "- currently", wait, end="\r")
        time.sleep(0.5)
        wait = ca.caget(pv.s3_xsize + ".RBV")
    else:
        print("\nX size set to", s3_xsize_set, end="\n")
        pass
    ca.caput(pv.s3_ysize, 0.1)
    wait = ca.caget(pv.s3_ysize + ".RBV")
    while float(s3_ysize_set) != float(wait):
        print("Setting S3 Y size to", s3_ysize_set, "- currently", wait, end="\r")
        time.sleep(0.5)
        wait = ca.caget(pv.s3_ysize + ".RBV")
    else:
        print("\nY size set to", s3_ysize_set, end="\n")
        pass
    ca.caput(pv.d2_y, str(pv.d2_position.get("diode 1")))
    wait = ca.caget(pv.d2_y + ".RBV")
    while float(pv.d2_position.get("diode 1")) != float(wait):
        print("Moving D2 to", pv.d2_position.get("diode 1"), "- currently", wait, end="\r")
        time.sleep(0.5)
        wait = ca.caget(pv.d2_y + ".RBV")
    else:
        print("\nD2 in position, starting X Y grid scan...\n")
        pass

    # move to each x, y value and record d2 current
    x_y_d2cur = []
    for y in np.around(np.linspace(-1, -0.7, 5, endpoint=True), 2):
        ca.caput(pv.s3_ycentre, str(y))
        y_aim = ca.caget(pv.s3_ycentre + ".RBV")
        while float(y_aim) != float(y):
            print("Moving Y centre to", y, "- currently at", y_aim, end="\r")
            time.sleep(0.5)
            y_aim = float(ca.caget(pv.s3_ycentre + ".RBV"))
        else:
            print("Y at", y, end="\r")
            print("")
            pass
        for x in np.around(np.linspace(-1, -0.7, 5, endpoint=True), 2):
            ca.caput(pv.s3_xcentre, str(x))
            x_aim = ca.caget(pv.s3_xcentre + ".RBV")
            while float(x_aim) != float(x):
                print("Moving X centre to", x, "- currently at", x_aim, end="\r")
                time.sleep(0.5)
                x_aim = float(ca.caget(pv.s3_xcentre + ".RBV"))
            else:
                d2c = ca.caget(pv.d2_cur_1)
                print("\nX =", x, "Y =", y, "D2 current =", d2c, end="\n")
                x_y_d2cur.append((x, y, float(d2c)))
                pass

    # return to beginning values
    ca.caput(pv.s3_xsize, x_size_static)
    wait = ca.caget(pv.s3_xsize_dmov)
    while float(wait) != float(1):
        print("Returning S3 X size to start value", x_size_static, end="\r")
        time.sleep(0.5)
        wait = ca.caget(pv.s3_xsize_dmov)
    else:
        print("\nFinished moving X size back to", x_size_static, end="\n")
        pass
    ca.caput(pv.s3_ysize, y_size_static)
    wait = ca.caget(pv.s3_ysize_dmov)
    while float(wait) != float(1):
        print("Returning S3 Y size to start value", y_size_static, end="\r")
        time.sleep(0.5)
        wait = ca.caget(pv.s3_ysize_dmov)
    else:
        print("\nFinished moving Y size back to", y_size_static, end="\n")
        pass
    ca.caput(pv.s3_xcentre, x_centre_static)
    wait = ca.caget(pv.s3_xcentre_dmov)
    while float(wait) != float(1):
        print("Returning S3 X centre to start value", x_centre_static, end="\r")
        time.sleep(0.5)
        wait = ca.caget(pv.s3_xcentre_dmov)
    else:
        print("\nFinished moving X centre back to", x_centre_static, end="\n")
        pass
    ca.caput(pv.s3_ycentre, y_centre_static)
    wait = ca.caget(pv.s3_ycentre_dmov)
    while float(wait) != float(1):
        print("Returning S3 Y centre to start value", y_centre_static, end="\r")
        time.sleep(0.5)
        wait = ca.caget(pv.s3_ycentre_dmov)
    else:
        print("\nFinished moving Y centre back to", y_centre_static, end="\n")
        pass
    ca.caput(pv.d2_y, d2_y_static)
    wait = ca.caget(pv.d2_y + ".RBV")
    while float(wait) != float(d2_y_static):
        print("Returning D2 Y to start value", d2_y_static, end="\r")
        time.sleep(0.5)
        wait = ca.caget(pv.d2_y + ".RBV")
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
    #beam_profile.figure.savefig(dt, ".png")
    plt.show()
