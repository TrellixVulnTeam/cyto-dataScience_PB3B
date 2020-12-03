import cv2
import matplotlib.pyplot as plt
import sys
sys.path.append('/home/dan/Dropbox/Create/ThinAir/CytoDynamic/master')
import image as img
import copy
import numpy as np
import pandas as pd
from waveform import *


wv = Waveform_2D(M=512, N=512)

wv.gen_sinusoid_2D(
     {'dim':'y', 'amp':2, 'form':'sin', 'k_y':6},
     {'dim':'y', 'amp':4, 'form':'sin', 'k_y':3},
     {'dim':'x', 'amp':2, 'form':'cos', 'k_x':6},
     {'dim':'x', 'amp':4, 'form':'cos', 'k_x':3})

cropped = wv.grab_area()

# Show fft of original image
wv.fft2d()
wv.show_im(wv.g_XY_mag_shift, 'Normal Image FFT')

# Show fft of cropped image
cropped.fft2d()
cropped.show_im(cropped.g_XY_mag_shift, 'Cropped Image FFT')

# cropped.show_im(cropped.g_xy, 'Image')
plt.show()


# new_wave = wv.grab_area()

# print(new_wave.M)



















