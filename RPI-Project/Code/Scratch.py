import cv2 
import numpy as np
import matplotlib.pyplot as plt
import glob
import functions as myFun
import pickle

# Load in Frames and Empty Background
rel_path = 'Blob-Detect-Images'
frames = myFun.create_img_array(rel_path)
initial_frame = frames[0]


# Blurring Operations
initial_frame_blurred = cv2.medianBlur(initial_frame,35)

# Threshold the Image ( < 70)
th, dst = cv2.threshold(initial_frame_blurred, 70, 255, cv2.THRESH_BINARY_INV)


dst_inv = cv2.bitwise_not(dst)
params = cv2.SimpleBlobDetector_Params()
 
# # Change thresholds
# params.minThreshold = 10
# params.maxThreshold = 200
params.filterByInertia = False
params.filterByConvexity = False
params.filterByCircularity = True
params.minCircularity = 0.4
params.maxCircularity = 0.9
params.filterByColor = True
params.blobColor = 0
# Filter by Area.
params.filterByArea = True
params.minArea =800
params.maxArea = 8000
 

# Create Blob Detector
detector = cv2.SimpleBlobDetector_create(params)
# Run Blob Detector
keypoints = detector.detect(dst_inv)
print(keypoints)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(dst_inv, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)

myFun.show_im_plt_gray(initial_frame)
myFun.show_im_plt_gray(initial_frame_blurred)
myFun.show_im_plt_gray(dst)
plt.show()