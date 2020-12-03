import cv2 
import numpy as np
import matplotlib.pyplot as plt
import image as img

im = img.Image('RK1.jpg', 0)
im_crop = im.crop_image(0,0,384,384)
# Get image shapes
im_shape = (im.image.shape)
im_crop_shape = (im_crop.image.shape)
# Get Image normalization factors
im_norm_C = (im_shape[0]/2)*(im_shape[1]/2)
im_crop_norm_C = (im_crop_shape[0]/2)*(im_crop_shape[1]/2)
print(im_norm_C)
print(im_crop_norm_C)
# Perform FFTs
im_f = np.fft.fft2(im.image)
im_crop_f = np.fft.fft2(im_crop.image)
# Compute magnitudes and normalize
im_mag = (np.abs(im_f))/im_norm_C
im_crop_mag = (np.abs(im_crop_f))/im_crop_norm_C

np.savetxt('im_mag.csv', im_mag, delimiter=',')

fig, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=True)
axs[0,0].imshow(im_crop.image, cmap='gray')
axs[0,0].set_title('Crop Image')

axs[0,1].imshow(im.image, cmap='gray')
axs[0,1].set_title('Image')

axs[1,0].imshow(im_mag, cmap='gray')
axs[1,0].set_title('Crop Image FFT')

axs[1,1].imshow(im_crop_mag, cmap='gray')
axs[1,1].set_title('Image FFT')

plt.show()








