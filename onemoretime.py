# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:28:21 2018

@author: krete
"""

import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import time
from tkinter import TclError
import audioop


from scipy.fftpack import fft
CHUNK = 1024 * 14       # size of the data 
FORMAT = pyaudio.paInt16     
CHANNELS = 1             
RATE = 44100    



# create matplotlib figure and axes
fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 7))


p = pyaudio.PyAudio()

# listen to the enviroment
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)


x = np.arange(0, 2 * CHUNK, 2)       
xf = np.linspace(0, RATE, CHUNK)     # frequencies (spectrum)



# create a line object with random data
line, = ax1.plot(x, np.random.rand(CHUNK), '-', lw=2)

# create semilogx line for spectrum
line_fft, = ax2.semilogx(xf, np.random.rand(CHUNK), '-', lw=2)
#line_fft, = ax2.plot(xf,np.random.rand(CHUNK), '-', lw=2 )

# format waveform axes
ax1.set_title('AUDIO WAVEFORM')
ax1.set_xlabel('samples')
ax1.set_ylabel('volume')
ax1.set_ylim(0, 255)
ax1.set_xlim(0, 2 * CHUNK)
plt.setp(ax1, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])

# format spectrum axes
ax2.set_xlim(20, RATE / 2)


# for measuring frame rate
frame_count = 0
start_time = time.time()

while True:
    
    # binary data
    data = stream.read(CHUNK)  
    
    # convert data to integers, make np array, then offset it by 127
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
    
    # create np array and offset by 128 = padding the data 
    data_np = np.array(data_int, dtype='b')[::2] + 128
    
    line.set_ydata(data_np)
    rms = audioop.rms(data,2)
    #print(rms)
    # no boundaries for the array display
    np.set_printoptions(threshold=np.nan)
    # the decible, if more than 400 then records and do the fft on the data 
    if rms > 100:
    # compute FFT and update 
        range_of_xf = 2*len(xf)
        temp = [0] * range_of_xf
        maxAmpIndex=0
        maxAmpValue=0
    
    
        #for i in range (0,len(xf),2):
         #   #print("dupa")
          #  temp[i] = xf[i]
           # temp[i+1] = xf[i]
            
        
        yt_trunk = data_int[0:1024]
       
        yt_trunk_fft = fft(yt_trunk)
        yf = fft(data_int)
        
        line_fft.set_ydata(np.abs(yf[0:CHUNK])  / (128 * CHUNK))
        
        temp = np.abs(yf[0:CHUNK])  / (128 * CHUNK)
        #line_fft.set_ydata(np.abs(yt_trunk_fft[0:CHUNK])  / (128 * CHUNK))
        abba = np.log(yf)
        absolute=np.abs(abba)
        maxim = np.max(np.abs(yf))
        maximo = np.max(np.abs(yf[0:CHUNK])  / (128 * CHUNK))
        
        logmax = np.abs(yf[0:CHUNK])  / (128 * CHUNK)
        
       
        xf_log = np.log(xf)
       
        #print((xf_log))
    
        """
        print("maxim:", maxim)
        print("maximo", maximo)  
        print("log:", logmax)
        """
        #print(temp)
        #print(temp[133])
        #print(temp[132])
        #print(temp[124])
        #print(len(logmax))
        #print(len(yf))
        #print(logmax)
        
        #line=plt.gca().get_lines()[xflen]
        xd=line.get_xdata()
        yd=line.get_ydata()
        
       
        for i in range (1,len(logmax)):
            #print(i)
            #print(logmax[i])
            if logmax[i] > maxAmpValue:
                maxAmpValue=logmax[i]
                maxAmpIndex=i
        
        abso=np.abs(yf)
        maxPeakFreq=xd[maxAmpIndex]
        
        
        
        #print(temp[maxAmpIndex])
        #print(xf)
        #print(len(xf))
        #print(len(abba))
        #print(temp)
        
        #print(maxAmpValue)
        print("fre", maxPeakFreq)
      
    # update figure canvas
    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame_count += 1
        
    except TclError:
        
        # calculate average frame rate
        frame_rate = frame_count / (time.time() - start_time)
        
        
        #breakrame rate = {:.0f} FPS'.format(frame_rate))
        break
    