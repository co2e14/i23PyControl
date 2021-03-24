#!/usr/bin/python
import os
import sys
import time

def pv_name(name):
    for pv in globals():
        if name[:2].lower() in pv.lower():
            print('Full PVs:', pv)

#S3
S3_Ytop = "BL23I-AL-SLITS-03:Y:PLUS"
S3_Ytop_rbv = "BL23I-AL-SLITS-03:Y:PLUS.RBV"
S3_Ybottom = "BL23I-AL-SLITS-03:Y:MINUS"
S3_Ybottom_rbv = "BL23I-AL-SLITS-03:Y:MINUS.RBV"
S3_Xinboard = "BL23I-AL-SLITS-03:X:MINUS"
S3_Xinboard_rbv = "BL23I-AL-SLITS-03:X:MINUS.RBV"
S3_Xoutboard = "BL23I-AL-SLITS-03:X:PLUS"
S3_Xoutboard_rbv = "BL23I-AL-SLITS-03:X:PLUS.RBV"
S3_Xcentre = "BL23I-AL-SLITS-03:X:CENTRE"
S3_Xcentre_rbv = "BL23I-AL-SLITS-03:X:CENTRE.RBV"
S3_Ycentre = "BL23I-AL-SLITS-03:Y:CENTRE"
S3_Ycentre_rbv = "BL23I-AL-SLITS-03:Y:CENTRE.RBV"
S3_Xsize = "BL23I-AL-SLITS-03:X:SIZE"
S3_Xsize_rbv = "BL23I-AL-SLITS-03:X:SIZE.RBV"
S3_Ysize = "BL23I-AL-SLITS-03:Y:SIZE"
S3_Ysize_rbv = "BL23I-AL-SLITS-03:Y:SIZE.RBV"

#D2
D2_positionIn = "BL23I-DI-PHDGN-02:F1:MP:SELECT"
D2_position_rbv = "BL23I-DI-PHDGN-02:FILTER:1.RBV"
D2_femto1Current = "BL23I-DI-PHDGN-02:OPT1:DIODE1:I:ADC1_VALEGU"
D2_femto2Current = "BL23I-DI-PHDGN-02:OPT1:DIODE2:I:ADC2_VALEGU"
D2_femto3Current = "BL23I-DI-PHDGN-02:OPT1:DIODE3:I:ADC1_VALEGU"
