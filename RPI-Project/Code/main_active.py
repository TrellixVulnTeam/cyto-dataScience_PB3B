# Declare imports
import cv2 
import numpy as np
import matplotlib.pyplot as plt
import glob
import functions as myFun


# Read in image array
frames = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image Processing/Frames/Algo-Test1')
initial_frame = myFun.init_crop_frame(frames)
initial_frame = cv2.medianBlur(initial_frame, 7)
acc_thresh = 20
min_rad = 10
circles, frame_circles = myFun.find_ball(initial_frame, acc_thresh, min_rad, canny_thresh=200)
print(circles)
plt.figure()
plt.imshow(initial_frame, cmap='gray', vmin=0, vmax=255)
plt.figure()
plt.imshow(frame_circles, cmap='gray', vmin=0,vmax=255)
plt.show()



