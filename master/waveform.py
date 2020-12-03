import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

class Waveform():
    """ A class representing a 1D waveform """
    def __init__(self, N, wavename=""):

        self.N        = N
        self.wavename = wavename
        self.n        = np.arange(self.N)
        self.x        = np.zeros(N, float) 
        self.n_shift  = (self.n - (self.N/2)).astype(int) 

    # Waveform generation methods
    def gen_sinusoid(self, *waves):
        for wave in waves:
            if wave['form'] == 'cos':
                self.x[self.n] = self.x[self.n] + \
                wave['amp']*np.cos(2*np.pi*wave['f']*(self.n/self.N)) 
            if wave['form'] == 'sin':
                self.x[self.n] = self.x[self.n] + \
                wave['amp']*np.sin(2*np.pi*wave['f']*(self.n/self.N))

    # Plotting related methods 
    def plot_waveform(self, waveform, fig_name='Figure'):
        print(self.n)
        plt.figure(fig_name)
        plt.stem(self.n, waveform, use_line_collection=True)

    def plot_waveform_centered(self, waveform, fig_name='Figure'):
        print(self.n)
        plt.figure(fig_name)
        plt.stem(self.n_shift, waveform, use_line_collection=True)   

    def plot_norm_fft_comparison(wave_a, wave_b):
        # Check which is the larger waveform and sort
        if wave_a.N != wave_b.N:
            if wave_a.N > wave_b.N:
                wave_g = wave_a
                wave_l = wave_b
            elif wave_a.N < wave_b.N:
                wave_g = wave_b
                wave_l = wave_a

            # Plot on same scale
            plt.figure(wave_g.wavename)
            plt.stem(wave_l.n_shift, wave_g.X_mag_shift[int(wave_l.N/2):int(wave_l.N/2+wave_l.N)], \
                use_line_collection=True)

            plt.figure(wave_l.wavename)
            plt.stem(wave_l.n_shift, wave_l.X_mag_shift, \
                use_line_collection=True)
        else:
            # Plot Normally
            plt.figure(wave_a.wavename)
            plt.stem(wave_a.n_shift, wave_a.X_mag_shift, use_line_collection=True)

            plt.figure(wave_b.wavename)
            plt.stem(wave_b.n_shift, wave_b.X_mag_shift, use_line_collection=True)

    def dft(self):
        self.X = np.fft.fft(self.x)
        self.X_mag = (np.abs(self.X))/(self.N/2) 
        self.X_mag_shift = np.fft.fftshift(self.X_mag)

    def show_table(self):
        X_table = pd.DataFrame(data=self.X_split)
        return X_table
    

class Waveform_2D():
    """ A Class representing a 2D Waveform"""
    def __init__(self, wave=None, M=None, N=None, wavename=''):
        if wave is None: 
            self.M        = M
            self.N        = N
            self.m        = np.arange(self.M)
            self.n        = np.arange(self.N)
            self.x        = self.m              # Optional reference to x coordinate
            self.y        = self.n              # Optional reference to y coordinate
            self.g_xy     = np.zeros((self.M,self.N), float)
            self.wavename = wavename
        else:
            self.M        = wave.shape[0]
            self.N        = wave.shape[1]
            self.m        = np.arange(self.M)
            self.n        = np.arange(self.N)
            self.x        = self.m
            self.y        = self.n
            self.g_xy     = wave
            self.wavename = wavename   
    def print_shape(self):
        print(self.g_xy.shape)
        print(self.g_xy)
        print(type(self.g_xy))

    def show_matrix(self):
        df = pd.DataFrame(data=self.g_xy)
        df
        return df
    
    def gen_sinusoid_2D(self, *waves):
        """Generate a 2D waveform to act as a control for fourier analysis.
        
         """
        for wave in waves:
            if wave['dim'] == 'x':
                if wave['form'] == 'cos':
                    for j in range(0, self.N):
                        self.g_xy[:,j] = self.g_xy[:,j] + \
                            wave['amp']*np.cos(2*np.pi*wave['k_x']*(self.x/self.M))
                if wave['form'] == 'sin':
                    for j in range(0, self.N):
                        self.g_xy[:,j] = self.g_xy[:,j] + \
                            wave['amp']*np.cos(2*np.pi*wave['k_x']*(self.x/self.M))
                        
            if wave['dim'] == 'y':
                if wave['form'] == 'cos':
                    for i in range(0, self.M):
                        self.g_xy[i,:] = self.g_xy[i,:] + \
                            wave['amp']*np.cos(2*np.pi*wave['k_y']*(self.y/self.N))
                if wave['form'] == 'sin':
                    for i in range(0,self.M):
                        self.g_xy[i, :] = self.g_xy[i, :] + \
                            wave['amp']*np.sin(2*np.pi*wave['k_y']*(self.y/self.N))

    def fft2d(self):
        """Get 2D fft of object and store it as the following attributes:
        g_XY = as is FFT
        g_XY_mag = FFT magnitude
        g_XY_mag_shift = FFT magnitude centered about 0
                            
        G_xy[k_x, k_y] = (N-1)Sum(y=0) (M-1)Sum(x=0) A*e^-j(2*pi*k_x*(x/M)+2*pi*k_y*(y/N))
        
        """
        self.g_XY           = np.fft.fft2(self.g_xy)
        self.g_XY_mag       = (np.abs(self.g_XY))/((self.N*self.M)/2) 
        self.g_XY_mag_shift = np.fft.fftshift(self.g_XY_mag)        

    
    def show_im(self, waveform, wavename=''):
        # maxval = np.amax(waveform)
        # print(maxval)
        # minval = np.amin(waveform)
        # print(minval)
        plt.figure(wavename)
        plt.imshow(waveform, cmap='gray', vmin=0, vmax=1)


    def grab_area(self):
        # Get ROI of image
        (x_0, y_0, x_os, y_os) = cv2.selectROI("Original Image", self.g_xy,\
            True, False)

        # Crop image to ROI and create new image
        g_xy_crop = self.g_xy[ y_0:(y_0+y_os), x_0:(x_0+x_os) ]
        g_xy_crop = Waveform_2D(wave=g_xy_crop)
        return g_xy_crop





















