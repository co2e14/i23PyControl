import time
import datetime
import os
import numpy as np
import pv
import control
from control import ca

class oneshot:
    def __init__(self, detector_position, visit, file_name, exposure_time):
        self.data_path = str(
            os.path.join("/ramdisk", "2021", str(visit), "screening/oneshot/")
        )
        self.data_path_st = self.data_path
        self.file_name = file_name
        self.detector_position = str(detector_position)
        print(self.detector_position)
        self.aquisition_period = float(exposure_time)
        self.exposure_time = float(exposure_time) - 0.003
        self.starting_energy = ca.caget(pv.dcm_energy)

    def prepare_beamline(self):
        # detector position
        detector_position_current = ca.caget(pv.pilatus_z_value)
        print("det current", str(detector_position_current))
        detector_position_end = pv.pilatus_z_positions[str(self.detector_position)]
        print("set end", str(detector_position_end))
        ca.caput(pv.pilatus_z_value, detector_position_end)
        print("Detector moving to " + str(detector_position_end), end="\r")
        while float(detector_position_end) != np.round(float(
            ca.caget(pv.pilatus_z_value + ".RBV"))
        ):
            time.sleep(0.2)
        # shutter
        ca.caput(pv.shutter_ctrl1, "Auto")
        print("Shutter done")
        # zebra
        ca.caput(pv.zebra_pc_arm_sel, "Soft")
        ca.caput(pv.zebra_pc_gate_sel, "Time")
        ca.caput(pv.zebra_pc_pulse_sel, "External")
        ca.caput(pv.zebra_pc_gate_start, 0)
        ca.caput(pv.zebra_pc_gate_wid, (self.aquisition_period * 1000))
        print("Zebra done")
        # senv
        ca.caput(pv.senv_mp_select, "Kappa Safe")
        time.sleep(0.2)
        print("Moving backlight out...")
        while ca.caget(pv.senv_mp_inpos) != "1":
            time.sleep(0.2)
        # pilatus
        ca.caput(pv.pilatus_acquire, 1)
        time.sleep(0.2)
        ca.caput(pv.pilatus_acquire, 1)
        ca.caput(pv.pilatus_acquire_time, str(self.exposure_time))
        ca.caput(pv.pilatus_acquire_period, str(self.aquisition_period))
        ca.caput(pv.pilatus_image_mode, "Single")
        ca.caput(pv.pilatus_trigger_mode, "Ext. Trigger")
        ca.caput(pv.pilatus_num_images, 1)
        ca.caputstring(pv.pilatus_file_path, str(self.data_path))
        ca.caputstring(pv.pilatus_file_name, str(self.file_name))
        ca.caput(pv.pilatus_file_number, 1)
        ca.caputstring(pv.pilatus_file_template, "%s%s%3d.cbf")
        print("Pilatus done")

    def collect(self):
        print("collecting")
        ca.caput(pv.pilatus_acquire, 1)
        time.sleep(0.2)
        ca.caput(pv.pilatus_acquire, 1)
        ca.caput(pv.zebra_pc_arm, 1)
        time.sleep(0.2)
        while str(ca.caget(pv.shutter_status)) != "Close":
            time.sleep(0.2)
        print("Finished")


    def energy_change(self, energy_request):
        if energy_request < 2700:
            id_gap = float((0.00223 * energy_request) - 0.19)
            id_gap = np.around(id_gap, 3)
            print("requesting ID gap of ", str(id_gap))
            ca.caput(pv.id_blgapmtr, id_gap)
            time.sleep(0.2)
            while id_gap != np.around(float(ca.caget(pv.id_currgapd)), 3):
                time.sleep(0.2)
        else:
            print("Not close enough to S edge to change gap")
        ca.caput(pv.dcm_energy, str(energy_request / 1000))
        time.sleep(0.2)
        while ca.caget(pv.dcm_energy_dmov) != "1":
            time.sleep(0.2)
        self.data_path = (self.data_path_st + "energyscan_")
        ca.caputstring(pv.pilatus_file_path, str(self.data_path) + "_" + str(self.file_name))
        ca.caputstring(pv.pilatus_file_name, str(self.file_name + "_" + str(int(energy_request)) + "eV_"))
        
    def check_d5_current(self):
        ca.caput(pv.senv_mp_select, "D5 In")
        time.sleep(0.2)
        while ca.caget(pv.senv_mp_inpos) != "1":
            time.sleep(0.2)
        t = 0
        d5 = 0.0
        while t < 10:
            d5_read = float(ca.caget(pv.senv_d5_ADC2valegu))
            d5 += d5_read
        d5 = d5 / 10
        self.d5values.append(d5)

    def returntonormal(self):
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
        ca.caput(pv.dcm_energy, self.starting_energy)


if __name__ == "__main__":
    print("I23 OneShot")
    # run = oneshot("out", "cm28128-4", "testing", 1)
    # run.prepare_beamline()
    # run.collect()
    # run.returntonormal()
