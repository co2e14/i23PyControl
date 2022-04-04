#!/usr/bin/env /dls/science/groups/i23/pyenvs/ctrl_conda/bin/python
# C. Orr 2022
from control import ca
import pv
import time

while True:
    if ca.caget(pv.senv_mp_select) == "Backlight":
        #time.sleep(0.1)
        if ca.caget(pv.senv_backlight_status) == "ON":
            ca.caput(pv.oav_cam_mp, "backlight")            
        else:
            pass
    else:
        ca.caput(pv.oav_cam_mp, "blue led")
    time.sleep(5)