# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:22:54 2024

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


directory=time.strftime("%Y-%m-%d")
parent_dir="C:/Users/batterylab/Documents/ODMR-Python-Codes"
path = os.path.join(parent_dir, directory)
path1=path+"/"

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




def CW_ODMR(start:1000000000.0,stop:3000000000.0,points:20): 
    # sleep(5)
    # B=9.8907*I_coil
    frequency=[]
    PL_out=[]
    Power=[]
    time_array=[]
    voltage_pd=[]
    set_power(0.0)  
    output_ON()        
    for i in range(points):
        print(i+1)
        freq=start+i*(stop-start)/points
        frequency.append(freq)
        set_freq(freq)
        voltage_pd.append(voltage())
        fig, (ax1) = plt.subplots(1)
        ax1.plot(frequency, voltage_pd)
        ax1.axvline(x=2870000000.0,color='r')
        ax1.set_title('CW ODMR spectrum')
        ax1.set_xlabel('Microwave Frequency(GHz)')
        ax1.set_ylabel('Voltage(mV)')
        fig.tight_layout()
        plt.pause(0.01)
        
        
        # label='B={:.2f} (mT)'.format(B)
        # fig, (ax1, ax2) = plt.subplots(2)
        # ax1.plot(time_array, Power,c='r')
        # ax2.plot(frequency, PL_out,label='B={:.2f} (mT)'.format(B))
        # ax1.set_title('Laser Power')
        # ax2.set_title('CW ODMR spectrum')
        # ax1.set_xlabel('Time(s)')
        # ax2.set_xlabel('Microwave Frequency(GHz)')
        # ax1.set_ylabel('Laser power(A.U)')
        # ax2.set_ylabel('PL(A.U)')
        # ax2.legend(loc='lower left')
        # fig.tight_layout()
        # plt.pause(0.01)
       
    ######
    
    fig, (ax1) = plt.subplots(1)
    ax1.plot(frequency, voltage_pd)
    ax1.axvline(x=2870000000.0,color='r')
    ax1.set_title('CW ODMR spectrum')
    ax1.set_xlabel('Microwave Frequency(GHz)')
    ax1.set_ylabel('Voltage(mV)')
    fig.tight_layout()
    plt.savefig(path1+'ODMR Spectrum-Photodiode'+time.strftime("-%Y-%m-%d-%H-%M")+'.jpeg')
    plt.show()
    frequency=np.array(frequency)
    voltage_pd=np.array(voltage_pd)
    np.save(path1+'ODMR frequency data'+time.strftime('%Y-%m-%d-%H-%M'),frequency)
    np.save(path1+'ODMR voltage data-'+time.strftime('%Y-%m-%d-%H-%M'),voltage_pd)
    
    
    # fig, (ax1, ax2) = plt.subplots(2)
    # ax1.plot(time_array, Power,c='r')
    # ax2.plot(frequency, PL_out,label='B={:.2f} (mT)'.format(B))
    # ax2.axvline(x=2870000000.0,color='r')
    # ax1.set_title('Laser Power')
    # ax2.set_title('CW ODMR spectrum')
    # ax1.set_xlabel('Time(s)')
    # ax2.set_xlabel('Microwave Frequency(GHz)')
    # ax1.set_ylabel('Laser power(A.U)')
    # ax2.set_ylabel('PL(A.U)')
    # ax2.legend(loc='lower left')
    # fig.tight_layout()
    # plt.savefig(path1+'ODMR Spectrum'+time.strftime("-%Y-%m-%d-%H-%M")+'.jpeg')
    # plt.show()  
    # time_array=np.array(time_array)
    # Power=np.array(Power)
    # PL_out=np.array(PL_out)
    # frequency=np.array(frequency)
    # np.save(path1+'ODMR frequency data'+time.strftime('%Y-%m-%d-%H-%M'),frequency)
    # np.save(path1+'ODMR PL data-'+time.strftime('%Y-%m-%d-%H-%M'),PL_out)
    # np.save(path1+'ODMR Power data-'+time.strftime('%Y-%m-%d-%H-%M'),Power)
    # np.save(path1+'ODMR time data-'+time.strftime('%Y-%m-%d-%H-%M'),time_array)
    # if flag_image==1:
    #     np.save(path1+'Image data'+time.strftime('%Y-%m-%d-%H-%M'),Image_matrix)



# os.mkdir(path)
# print(path)
# num_points=100
# CW_ODMR(2700000000.0,3040000000.0,num_points)
print(voltage())