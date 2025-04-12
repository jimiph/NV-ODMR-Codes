import cv2
from matplotlib import pyplot as plt
from scipy.fft import fft, fftfreq
import numpy as np
import time
import math
import os

directory=time.strftime("%Y-%m-%d")
parent_dir="C:/Users/batterylab/Documents/ODMR-Python-Codes"
path = os.path.join(parent_dir, directory)
path1=path+"/"


def take_photo(number:10):
    cap=cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_EXPOSURE,0)
    Power=[]
    time_array=[]
    for i in range(number):
        print(i+1)
        # print(time.time())
        ret, frame= cap.read()
        frame=np.array(frame)
        # print(time.time())
        # print(frame.shape)
        print(frame)
        # plt.imshow(frame)
        # plt.colorbar()
        # Power.append(np.average(frame[200:400,500:700,0:2]))
        if i==0:
            time_set=time.time()
            time_array.append(0)
        else:
            time_array.append(time.time()-time_set)
        plt.xlabel('time(s)')
        plt.ylabel('Laser power(A.U)')
        plt.plot(time_array,Power)
        plt.title('Laser power vs time')
        plt.pause(0.01)
    plt.xlabel('time(s)')
    plt.ylabel('Laser power(A.U)')
    plt.plot(time_array,Power)
    plt.title('Laser power vs time')
    plt.savefig(path1+"Laser power vs time-"+time.strftime("%Y-%m-%d-%H-%M")+".jpeg")
    np.save(path1+'laser power data-'+time.strftime('%Y-%m-%d-%H-%M'),Power)
    np.save(path1+'time data-'+time.strftime('%Y-%m-%d-%H-%M'),time_array)
    cap.release()
    return Power


# os.mkdir(path)
# print(path)
t=1000
take_photo(t)
# t1=time.time()


