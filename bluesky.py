import bluesky
import ophyd
from ophyd import EpicsMotor


S3_x = EpicsMotor("BL23I-AL-SLITS-03:X:CENTRE", name="S3_x")

S3_x.wait_for_connection()
S3_x.summary()
