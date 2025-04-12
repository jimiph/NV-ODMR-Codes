# orig_stdout = sys.stdout
# f = open('out.txt', 'w')
# sys.stdout = f
# sys.stdout = orig_stdout
# f.close()



import cv2
import time
import pyvisa
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl
from pymba import Frame
from pymba import Vimba, VimbaException
from typing import Optional
from time import sleep
# from MW_source import dev_connect, output_ON, output_OFF, set_freq, set_power, freq_sweep, freq_sweepoff, power_sweep, power_sweepoff
from CMOS_camera import display_frame, camera_id, darkcount, bias, flat, science

#bias(10)
# darkcount(30)
#flat(30)
#science=science(30)
dark_count=np.array(np.load('darkcount.npy',allow_pickle=True))
bias=np.array(np.load('bias.npy',allow_pickle=True))
flat=np.array(np.load('flat.npy',allow_pickle=True))


# todo add more colours
PIXEL_FORMATS_CONVERSIONS = {
    'BayerRG8': cv2.COLOR_BAYER_RG2RGB,
}


def PL(flat:flat,bias:bias,darkcount:dark_count):
    science_image=science(1900000)
    print(science_image)
    norm=(flat-bias)/np.average(flat-bias)
    #final_image=(science_image-darkcount)/norm
    plt.imshow(science_image,cmap='brg')
    plt.colorbar()
    #thresh=-7
    counter=0
    intensity=0
    for i in range(200,300):
        for j in range(600,800):
            #if final_image[i][j]>=thresh:
            #intensity +=final_image[i][j]
            intensity +=science_image[i][j]
            counter +=1
    intensity=intensity/counter
    return intensity


def CW_ODMR(start:1000000000.0,stop:3000000000.0,points:20): 
    frequency=np.zeros((points)) 
    PL_out=np.zeros((points))          
    for i in range(points):
        freq=start+i*(stop-start)/points
        frequency[i]=freq
        #output_ON()
        set_freq(freq)
        sleep(1)
        PL_out[i]=PL(flat,bias,dark_count,i)
    print(PL)
    print(frequency)
    plt.plot(frequency,PL_out/np.max(PL_out))
    plt.xlabel('Microwave Frequency(GHz)')
    plt.ylabel('Normalized PL(A.U)')
    plt.show()   




#CW_ODMR(2830000000.0, 2890000000.0, 10)
print(PL(flat,bias,dark_count))    
#science(190000)       



        
        
        


        