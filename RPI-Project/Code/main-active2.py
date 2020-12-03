# Declare imports
import cv2 
import numpy as np
import matplotlib.pyplot as plt
import glob
import functions as myFun

# Set Active Video
filename = 'Image-Arrays/24ft-Kick2'

#Initialize Variables
ball_parameters = []

# Read in image array=
frames = myFun.load_img_array(filename)
plt.figure('Initial-Frame')
plt.imshow(frames[0], cmap='gray', vmin=0, vmax=255)
plt.show()
# Get initial cropped frame
initial_frame, crop_info  = myFun.init_crop_frame(frames[0])
plt.figure('Initial-Frame')
plt.imshow(initial_frame, cmap='gray', vmin=0, vmax=255)
plt.show()
initial_frame = cv2.medianBlur(initial_frame, 5)
# initial_frame = cv2.bilateralFilter(initial_frame,9,75,75)
# ret,thresh4 = cv2.threshold(initial_frame,60,255,cv2.THRESH_TOZERO_INV)
plt.figure('Initial-Frame')
plt.imshow(initial_frame, cmap='gray', vmin=0, vmax=255)
plt.show()
# Find Initial Ball
circles, frame_circles = myFun.find_ball(initial_frame, acc_thresh=15, min_rad=10,max_rad=20, canny_thresh=240)
plt.figure('New Frame Circle')
plt.imshow(frame_circles, cmap='gray', vmin=0, vmax=255)
plt.show()
# Find Initial Definite Location of Ball
ball_info = myFun.get_ball_info(circles,crop_info)
print('Ball Coordinates:' + str(ball_info.get('coordinates')))
print('Ball Radius:' + str(ball_info.get('radius')))

for i in range(1, 40):
    # Crop to Ball
    new_frame, crop_info = myFun.crop_to_ball(frames[i], ball_info)
    
    circles, frame_circles = myFun.find_ball(new_frame, acc_thresh=15, min_rad=3, canny_thresh=220)
    ball_info = myFun.get_ball_info(circles,crop_info)
    plt.figure('New Frame Circle'+ str(i))
    plt.imshow(frame_circles, cmap='gray', vmin=0, vmax=255)
    plt.show()





# plt.figure('New Frame')
# plt.imshow(new_frame, cmap='gray', vmin=0, vmax=255)
# plt.figure('New Frame Circle')
# plt.imshow(frame_circles, cmap='gray', vmin=0, vmax=255)
# plt.show()






