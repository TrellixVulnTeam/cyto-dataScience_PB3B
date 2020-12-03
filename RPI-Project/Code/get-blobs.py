import cv2 
import numpy as np
import matplotlib.pyplot as plt
import glob
import functions as myFun
import pickle

# Create Initial Image Array
rel_path = 'Blob-Detect-Images'
im_array = myFun.create_img_array(rel_path)

# Blur Images
for i in range(0,len(im_array)):
    im_array[i] = cv2.medianBlur(im_array[i],35)

# Threshold to Binary
blob_array = []
for image in im_array:
    th, dst = cv2.threshold(image, 70, 255, cv2.THRESH_BINARY_INV)
    blob_array.append(dst)
myFun.show_im_plt_gray(blob_array[0])
plt.show()

# ****** Detect Athlete (Blob Detection) ******
# Discuss the reason for your blob detection work. Need to write orientation filter 
for image in blob_array:
    dst_inv = cv2.bitwise_not(image)
    params = cv2.SimpleBlobDetector_Params()
    # Define Parameters
    params.filterByConvexity = False
    # Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.4
    params.maxCircularity = 0.9
    # Color
    params.filterByColor = True
    params.blobColor = 0
    # Area
    params.filterByArea = True
    params.minArea = 800
    params.maxArea = 8000
    # Inertia
    params.filterByInertia = True
    params.maxInertiaRatio = .3

    detector = cv2.SimpleBlobDetector_create(params)

    keypoints = detector.detect(dst_inv)
    print(keypoints)

    im_with_keypoints = cv2.drawKeypoints(dst_inv, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # Show keypoints
    # cv2.imshow("Keypoints", im_with_keypoints)
    # cv2.waitKey(0)
# **************************************************************

# ****** Blob Detection 2 ********
# im = blob_array[0]
# useless, contours,hierarchy = cv2.findContours(im, 1, 2)
# cnt = contours[0]
# ellipse = cv2.fitEllipse(cnt)
# im = cv2.ellipse(im,ellipse,(0,255,0),2)

# cv2.imshow("Keypoints", im)
# cv2.waitKey(0)



# Show Images
# for image in blob_array:
#     plt.figure()
#     plt.imshow(image, cmap='gray', vmin=0, vmax=255)
# for image in im_array:
#     plt.figure()
#     plt.imshow(image, cmap='gray', vmin=0, vmax=255)

# plt.show()




# initial_frame_blurred = cv2.medianBlur(initial_frame,35)
