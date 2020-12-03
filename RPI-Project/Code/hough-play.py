from functions import find_ball
import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('frame0001.png',0)
crop_img = img[300:600, 850:1350]
img2 = cv2.imread('frame0107.png',0)
crop_img2 = img2[300:600, 850:1350]
img3 = cv2.imread('frame0127.png',0)
crop_img3 = img3[300:600, 850:1350]
plt.figure('im3')
plt.imshow(crop_img3, cmap='gray', vmin=0, vmax=255)
plt.show()
# find_ball(crop_img, 32,50)
# find_ball(crop_img2, 32,25)
find_ball(crop_img3, 300, 40)


