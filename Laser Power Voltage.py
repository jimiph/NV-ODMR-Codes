# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 11:17:59 2024

@author: batterylab
"""

import time
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from MW_source import dev_connect, output_ON, output_OFF, set_freq, set_power, freq_sweep, freq_sweepoff, power_sweep, power_sweepoff
import redpitaya_scpi as scpi

IP = 'rp-f0a8d0.local'
rp_s = scpi.scpi(IP)

def voltage():
    rp_s.tx_txt('ACQ:RST')

    rp_s.tx_txt('ACQ:DEC 8192')
    rp_s.tx_txt('ACQ:START')
    # rp_s.tx_txt('ACQ:TRig:LEV 0.400 V')
    rp_s.tx_txt('ACQ:TRig NOW')

    while 1:
        rp_s.tx_txt('ACQ:TRig:STAT?')
        if rp_s.rx_txt() == 'TD':
            break

    ## ! OS 2.00 or higher only ! ##
    while 1:
        rp_s.tx_txt('ACQ:TRig:FILL?')
        if rp_s.rx_txt() == '1':
            break

    rp_s.tx_txt('ACQ:SOUR1:DATA?')
    buff_string = rp_s.rx_txt()
    buff_string = buff_string.strip('{}\n\r').replace("  ", "").split(',')
    buff = list(map(float, buff_string))

    voltage1=np.array(buff)
    return np.average(voltage1)


def voltage_laser(points:200):
    time_array=[]
    voltage_pd=[]
    for i in range(points):
        print(i+1)
        voltage_pd.append(voltage())
        time_array.append(time.time())
        plt.plot(time_array,voltage_pd)
        plt.tight_layout()
        plt.pause(0.01)
        
        
voltage_laser(2000)
