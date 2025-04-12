# ExposureAuto
# 	value: Continuous
# 	range: ['Off', 'Once', 'Continuous', 'other']
# ExposureMode
# ExposureMode
# 	value: Timed
# 	range: ['Timed']
# ExposureTimeAbs
# ExposureTimeAbs
# 	value: 4035.0
# 	range: (10.0, 60000000.0)
# PixelFormat
# PixelFormat
# 	value: Mono8
# 	range: ['Mono8', 'Mono10', 'Mono12', 'Mono12Packed', 'Mono14', 'BayerGR8', 'BayerRG8', 'BayerBG8', 'BayerBG10', 'BayerGR12', 'BayerRG12', 'BayerGR12Packed', 'BayerRG12Packed', 'RGB8Packed', 'BGR8Packed', 'RGBA8Packed', 'BGRA8Packed', 'RGB10Packed', 'RGB12Packed', 'YUV411Packed', 'YUV422Packed', 'YUV444Packed']
# OffsetX
# OffsetX
# 	value: 0
# 	range: (0, 1360)
# OffsetY
# OffsetY
# 	value: 0
# 	range: (0, 1024)
# AcquisitionFrameCount
# AcquisitionFrameCount
# 	value: 1
# 	range: (1, 65535)
# AcquisitionFrameRateAbs
# AcquisitionFrameRateAbs
# 	value: 30.011104108520154
# 	range: (0.012732925961193301, 30.011104108520154)
# AcquisitionMode
# AcquisitionMode
# 	value: Continuous
# 	range: ['Continuous', 'SingleFrame', 'MultiFrame', 'Recorder']
# AcquisitionStart
# AcquisitionStart
# 	value: Cannot get or set the value of a command feature type, call the command instead.
# 	range: None
# AcquisitionStop
# AcquisitionStop
# 	value: Cannot get or set the value of a command feature type, call the command instead.
# 	range: None
# GainAuto
# GainAuto
# 	value: Off
# 	range: ['Off', 'Once', 'Continuous']
# Height
# Height
# 	value: 1024
# 	range: (1, 1024)
# HeightMax
# HeightMax
# 	value: 1024
# 	range: (0, 4294967295)
# ImageSize
# ImageSize
# 	value: 1392640
# 	range: (0, 4294967295)


import cv2
import time
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from typing import Optional
from pymba import Frame
from pymba import Vimba, VimbaException
from time import sleep
from scipy.io import savemat
from MW_source import dev_connect, output_ON, output_OFF,output_Mod_ON,output_Mod_OFF,AM_Mod, set_freq, set_power, freq_sweep, freq_sweepoff, power_sweep, power_sweepoff



directory=time.strftime("%Y-%m-%d")
parent_dir="C:/Users/batterylab/Documents/ODMR-Python-Codes"
path = os.path.join(parent_dir, directory)
path1=path+"/"


# todo add more colours
PIXEL_FORMATS_CONVERSIONS = {
    'BayerRG8': cv2.COLOR_BAYER_RG2RGB,
}

def display_frame(frame: Frame, delay: Optional[int] = 1) -> None:
    """
    Displays the acquired frame.
    :param frame: The frame object to display.
    :param delay: Display delay in milliseconds, use 0 for indefinite.
    """
    print('frame {}'.format(frame.data.frameID))

    # get a copy of the frame data
    image = frame.buffer_data_numpy()

    # convert colour space if desired
    try:
        image = cv2.cvtColor(image, PIXEL_FORMATS_CONVERSIONS[frame.pixel_format])
    except KeyError:
        pass

    # display image
    #cv2.imshow('Image', image) 
    image=np.array(image)
    cv2.waitKey(delay)
    return image
    


def camera_id():
    if __name__ == '__main__':

        with Vimba() as vimba:
            # provide camera index or id
            camera = vimba.camera(0)
            print(camera)
            print(vimba.camera_ids())
            
            
def darkcount(exposure:30.0):
    if __name__ == '__main__':

        with Vimba() as vimba:
            camera = vimba.camera(0)
            camera.open()
            camera.feature('ExposureAuto').value = 'Off'
            camera.feature('ExposureTimeAbs').value =exposure
            camera.feature('PixelFormat').value ='Mono8'
            camera.arm('SingleFrame')
            frame = camera.acquire_frame()
            darkcount_matrix=display_frame(frame, 0)
            np.save('darkcount',darkcount_matrix)
            # print(darkcount_matrix)
            # print(np.average(darkcount_matrix),np.min(darkcount_matrix),np.max(darkcount_matrix))
            plt.imshow(darkcount_matrix,cmap='jet')
            plt.colorbar()
            plt.xlabel('X')
            plt.ylabel('Y')
            sleep(1)
            camera.stop_frame_acquisition()
            camera.disarm()
            camera.close()


def bias(exposure:10.0):
    if __name__ == '__main__':

        with Vimba() as vimba:
            camera = vimba.camera(0)
            camera.open()
            camera.feature('ExposureAuto').value = 'Off'
            camera.feature('ExposureTimeAbs').value =exposure
            camera.feature('PixelFormat').value ='Mono8'
            camera.arm('SingleFrame')
            frame = camera.acquire_frame()
            bias_matrix=display_frame(frame, 0)
            np.save('bias',bias_matrix)
            # print(darkcount_matrix)
            # print(np.average(darkcount_matrix),np.min(darkcount_matrix),np.max(darkcount_matrix))
            plt.imshow(bias_matrix,cmap='brg')
            plt.colorbar()
            plt.xlabel('X')
            plt.ylabel('Y')
            sleep(1)
            camera.stop_frame_acquisition()
            camera.disarm()
            camera.close()
            
            
            
def flat(exposure:10.0):
    if __name__ == '__main__':

        with Vimba() as vimba:
            camera = vimba.camera(0)
            camera.open()
            camera.feature('ExposureAuto').value = 'Off'
            camera.feature('ExposureTimeAbs').value =exposure
            camera.feature('PixelFormat').value ='Mono8'
            camera.arm('SingleFrame')
            frame = camera.acquire_frame()
            flat_matrix=display_frame(frame, 0)
            np.save('flat',flat_matrix)
            # print(darkcount_matrix)
            # print(np.average(darkcount_matrix),np.min(darkcount_matrix),np.max(darkcount_matrix))
            plt.imshow(flat_matrix,cmap='jet')
            plt.colorbar()
            plt.xlabel('X')
            plt.ylabel('Y')
            sleep(1)
            camera.stop_frame_acquisition()
            camera.disarm()
            camera.close()

science_matrix=np.zeros((1024,1360))
            
def science(exposure:10.0):
    if __name__ == '__main__':
        
        with Vimba() as vimba:
            
            camera = vimba.camera(0)
            camera.open()
            camera.feature('ExposureMode').value='Timed'
            camera.feature('ExposureAuto').value = 'Off'
            camera.feature('ExposureTimeAbs').value =exposure
            camera.feature('PixelFormat').value ='Mono12'
            camera.arm('SingleFrame')
            frame = camera.acquire_frame()
            
            global science_matrix
            science_matrix=display_frame(frame, 0)
            
            # print(np.shape(science_matrix))
            #np.save('flat',flat_matrix)
            # print(darkcount_matrix)
            # print(np.average(darkcount_matrix),np.min(darkcount_matrix),np.max(darkcount_matrix))
            # plt.imshow(science_matrix,cmap='brg')
            # plt.colorbar()
            # plt.xlabel('X')
            # plt.ylabel('Y')
            #sleep(1)
            camera.stop_frame_acquisition()
            
            camera.disarm()
            camera.close()
            
    return science_matrix



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
        # print(frame)
        # plt.imshow(frame)
        # plt.colorbar()
        # Power.append(np.average(frame[400:400,400:600,0:2]))
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


#bias(2000)
#flat(1000)
#darkcount(100)
dark_count=np.array(np.load('darkcount.npy',allow_pickle=True))
bias=np.array(np.load('bias.npy',allow_pickle=True))
flat=np.array(np.load('flat.npy',allow_pickle=True))

def PL(flat:flat,bias:bias,darkcount:dark_count,flag:0):
    counter=0
    intensity=0
    sub_matrix=np.zeros([1,1])
    exposure=10
    hfont={'fontname':'Times New Roman'}
    for i in range(1):
        if flag==1:
            science_image=science(exposure)
            # np.save(path1+'Science_image'+time.strftime('%Y-%m-%d-%H-%M'),science_image)
            plt.imshow(science_image,cmap='hot')
            plt.colorbar(label='Intensity(A.U)')
            plt.title('Image of diamond with CCD Camera')
            plt.xlabel('X (Pixels)')
            plt.ylabel('Y (Pixels)')
            plt.savefig(path1+'Image of Red  PL'+time.strftime("-%Y-%m-%d-%H-%M")+'.svg')
            science_image = np.array(science_image)
            # sub_matrix=sub_matrix+science_image[400:600,500:700]
            # intensity=np.amax(science_image)
            ind = np.array(np.unravel_index(np.argmax(science_image, axis=None), science_image.shape))
            # print(ind.shape)
            sub_matrix=sub_matrix+science_image[ind[0]-50:ind[0]+50,ind[1]-50:ind[1]+50]
            # plt.imshow(sub_matrix,cmap='OrRd')
            avg=np.average(sub_matrix)
            counter+=1
        else:
            science_image=science(exposure)
            science_image = np.array(science_image)
            # sub_matrix=sub_matrix+science_image[400:600,500:700]
            intensity=np.amax(science_image)
            ind = np.array(np.unravel_index(np.argmax(science_image, axis=None), science_image.shape))
            sub_matrix=sub_matrix+science_image[ind[0]-50:ind[0]+50,ind[1]-50:ind[1]+50]
            avg=np.average(sub_matrix)
            counter+=1
        # print(counter)
    intensity=intensity/counter
    # print(time.time())
    return avg


def Image(flat:flat,bias:bias,darkcount:dark_count):
    science_image=np.zeros((1024,1360))
    exposure=10
    counter=10
    for i in range(counter):
        science_image=np.array(science(exposure))+science_image
        # science_image = np.array(science_image)
    science_image=science_image/counter
    return science_image


# Image_matrix

def CW_ODMR(start:1000000000.0,stop:3000000000.0,points:20,I_coil:0,flag_PL:0,flag_image,Image_matrix): 
    # sleep(5)
    # B=9.8907*I_coil
    frequency=[]
    PL_out=[]
    # Power=[]
    # time_array=[]
    # cap=cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_EXPOSURE,0)
    set_power(0.0)  
    output_ON()        
    for i in range(points):
        print(i+1)
        freq=start+i*(stop-start)/points
        frequency.append(freq)
        set_freq(freq)
        ##### this part is related to Hawyear Camera (Measuring Laser power)
        # ret, frame= cap.read()
        # frame=np.array(frame)
        # Power.append(np.average(frame[200:400,500:700,0:2]))
        # if i==0:
        #     time_set=time.time()
        #     time_array.append(0)
        # else:
        #     time_array.append(time.time()-time_set)
        ####
        PL_out.append(PL(flat,bias,dark_count,flag_PL))
        if flag_image==1:
            Image_matrix[:,:,i]=Image(flat,bias,dark_count)
        else:
            pass
        
        # print(frequency)
        # print(PL_out)
        # print(time_array)
        # print(Power)
        
        fig, (ax1) = plt.subplots(1)
        # ax1.plot(time_array, Power,c='r')
        ax1.plot(frequency, PL_out)
        ax1.axvline(x=2870000000.0,color='r')
        ax1.set_title('CW ODMR spectrum')
        # ax2.set_title('CW ODMR spectrum')
        # ax1.set_xlabel('Time(s)')
        ax1.set_xlabel('Microwave Frequency(GHz)')
        # ax1.set_ylabel('Laser power(A.U)')
        ax1.set_ylabel('PL(A.U)')
        # ax2.legend(loc='lower left')
        fig.tight_layout()
        plt.pause(0.01)
       
    ######
    
    fig, (ax1) = plt.subplots(1)
    # ax1.plot(time_array, Power,c='r')
    ax1.plot(frequency, PL_out)
    # label='B={:.2f} (mT)'.format(B)
    ax1.axvline(x=2870000000.0,color='r')
    # ax1.set_title('Laser Power')
    ax1.set_title('CW ODMR spectrum')
    # ax1.set_xlabel('Time(s)')
    ax1.set_xlabel('Microwave Frequency(GHz)')
    # ax1.set_ylabel('Laser power(A.U)')
    ax1.set_ylabel('PL(A.U)')
    ax1.legend(loc='lower left')
    fig.tight_layout()
    plt.savefig(path1+'ODMR Spectrum'+time.strftime("-%Y-%m-%d-%H-%M")+'.jpeg')
    plt.show()  
    # time_array=np.array(time_array)
    # Power=np.array(Power)
    PL_out=np.array(PL_out)
    frequency=np.array(frequency)
    np.save(path1+'ODMR frequency data'+time.strftime('%Y-%m-%d-%H-%M'),frequency)
    np.save(path1+'ODMR PL data-'+time.strftime('%Y-%m-%d-%H-%M'),PL_out)
    # np.save(path1+'ODMR Power data-'+time.strftime('%Y-%m-%d-%H-%M'),Power)
    # np.save(path1+'ODMR time data-'+time.strftime('%Y-%m-%d-%H-%M'),time_array)
    if flag_image==1:
        np.save(path1+'Image data'+time.strftime('%Y-%m-%d-%H-%M'),Image_matrix)
 
    
# os.mkdir(path)
# print(path)


flag_PL=1
flag_image=1
I_coil=0
num_points=100
Image_matrix=np.zeros((1024,1360,num_points))
print(PL(flat,bias,dark_count,flag_PL))  
CW_ODMR(2700000000.0,3040000000.0,num_points,I_coil,flag_PL,flag_image,Image_matrix)


# output_Mod_ON()
# output_Mod_OFF()
# A=np.array(np.load('Image data2023-08-08-11-07.npy',allow_pickle=True))
# dic={"A":A}
# savemat("image_matrix.mat", dic)