#!/bin/env python3
import pv
import subprocess
import os
from subprocess import Popen, PIPE
import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


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
            a = Popen(["caput", "-S", pv, str(new_val)], stdout=PIPE, stderr=PIPE)
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
    # store all current values to return to at the end
    d2_position_static = ca.caget(pv.d2_filter1value)
    x_size_static = ca.caget(pv.s3_xsize + ".RBV")
    y_size_static = ca.caget(pv.s3_ysize + ".RBV")
    x_centre_static = ca.caget(pv.s3_xcentre + ".RBV")
    y_centre_static = ca.caget(pv.s3_ycentre + ".RBV")

    # set x size, y size and move d2 diode in
    ca.caput(pv.s3_xsize, 0.1)
    ca.caput(pv.s3_ysize, 0.1)
    ca.caput(pv.d2_filter1value, pv.d2_filter_positioner.get("diode 1"))

    # move to each x, y value and record d2 current
    x_y_d2cur = []
    for y in range(-1, 2, 1):
        ca.caput(pv.s3_ycentre, y)
        y_aim = ca.caget(pv.s3_ycentre + ".RBV")
        while float(x_aim) != float(y):
            print("Moving Y centre...")
            time.sleep(2)
            y_aim = float(ca.caget(pv.s3_ycentre + ".RBV"))
        else:
            print("Y in place")
            pass
        for x in range(-1, 2, 1):
            ca.caput(pv.s3_xcentre, x)
            x_aim = ca.caget(pv.s3_xcentre + ".RBV")
            while float(x_aim) != float(x):
                print("Moving X centre...")
                time.sleep(2)
                x_aim = float(ca.caget(pv.s3_xcentre + ".RBV"))
            else:
                print("X in place, reading D2 current...")
                d2c2 = ca.caget(pv.d2_cur_2)
                x_y_d2cur.append([(x, y, d2c2)])
                print(str(d2c2))
                pass

    # return to beginning values
    ca.caput(pv.s3_xsize, x_size_static)
    ca.caput(pv.s3_ysize, y_size_static)
    ca.caput(pv.s3_xcentre, x_centre_static)
    ca.caput(pv.s3_ycentre, y_centre_static)
    ca.caput(pv.d2_filter1value, d2_position_static)

    df = pd.DataFrame(x_y_d2cur, columns=("X", "Y", "D2"))
    df = df.pivot('X', 'Y', 'D2')
    sns.heatmap(df, cmap='RdBu')
    plt.show()