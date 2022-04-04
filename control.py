#!/bin/env python3
import pv
import subprocess
import os
from subprocess import Popen, PIPE


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
            except:
                print("Exception in ca_py3.py caget, maybe this PV doesnt exist:", pv)
                pass
        return val

    def caput(pv, new_val):
        check = Popen(["cainfo", pv], stdout=PIPE, stderr=PIPE)
        check_stdout, check_stderr = check.communicate()
        a = Popen(["caput", pv, str(new_val)], stdout=PIPE, stderr=PIPE)
        a_stdout, a_stderr = a.communicate()

    def caputstring(pv, new_val):
        check = Popen(["cainfo", pv], stdout=PIPE, stderr=PIPE)
        check_stdout, check_stderr = check.communicate()
        a = Popen(["caput", "-S", pv, str(new_val)])
        a_stdout, a_stderr = a.communicate()


class control:
    def __init__(self):
        print("V0.1")

    def get_value(self, pv):
        subprocess.run(("caget", pv))

    def push_value(self, pv):
        subprocess.run(("caput", pv))


class returntonormal:
    def __init__(self):
        print(
            "Returning beamline to standard data collection parameters and positions..."
        )
        ca.caput(pv.zebra_pc_disarm, 1)
        ca.caput(pv.zebra_pc_gate_sel, "Position")
        ca.caput(pv.zebra_pc_pulse_sel, "Time")
        ca.caput(pv.zebra_pc_arm_sel, "Soft")
        ca.caput(pv.zebra_pc_disarm, 1)
        ca.caput(pv.pilatus_image_mode, "Continuous")
        ca.caput(pv.pilatus_trigger_mode, "Ext. Trigger")
        ca.caput(pv.shutter_ctrl1, "Manual")


if __name__ == "__main__":
    print("Python3 I23 Controls")
