import cv2
import matplotlib.pyplot as plt
import sys
sys.path.append('/home/dan/Dropbox/Create/ThinAir/CytoDynamic/master')
import image as img
import copy
import numpy as np
import pandas as pd
from waveform import *

# Create image
im = img.Image('RK1.jpg', 0)

# Set image to 2D Waveform object
im_2D = Waveform_2D(wave = im.image )

# Get FFTs of Waveforms
im_2D.fft2d()

# Show FFT
im_2D.g_XY_mag_shift[768, 1024] = 0
im_2D.show_im(im_2D.g_XY_mag_shift)
result = np.where(im_2D.g_XY_mag_shift == np.amax(im_2D.g_XY_mag_shift))
print(result)
print(im_2D.g_XY_mag_shift[1024, 768])

plt.show()





