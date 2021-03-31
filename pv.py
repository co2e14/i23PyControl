#!/usr/bin/python
import os
import sys
import time


def pv_name(name):
    for pv in globals():
        if name[:2].lower() in pv.lower():
            print("PV:", pv[:])


def pv_return():
    return globals()


# S3
s3_xcentre = "BL23I-AL-SLITS-03:X:CENTRE"
s3_ycentre = "BL23I-AL-SLITS-03:Y:CENTRE"
s3_xsize = "BL23I-AL-SLITS-03:X:SIZE"
s3_ysize = "BL23I-AL-SLITS-03:Y:SIZE"

# D2
d2_positionin = "BL23I-DI-PHDGN-02:F1:MP:SELECT"
d2_filter1value = "BL23I-DI-PHDGN-02:POS1:UPD.D"
d2_cur_1 = "BL23I-DI-PHDGN-02:OPT1:DIODE1:I:ADC1_VALEGU"
d2_cur_2 = "BL23I-DI-PHDGN-02:OPT1:DIODE2:I:ADC2_VALEGU"
d2_cur_3 = "BL23I-DI-PHDGN-02:OPT1:DIODE3:I:ADC1_VALEGU"
d2_filter_positioner = {
    "empty": -145.00,
    "diode 1": -53.30,
    "diode 2": -27.90,
    "diode 3": -2.50,
}
