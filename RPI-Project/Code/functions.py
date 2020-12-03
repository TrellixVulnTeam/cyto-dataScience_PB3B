import cv2 
import numpy as np
import matplotlib.pyplot as plt
import glob
import pickle

# Hough Circles Implementation
def find_ball(img,acc_thresh=20,min_rad=5,max_rad=30, canny_thresh=10 , min_dist=20):
    img_circles = img.copy()
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,min_dist,param1=canny_thresh,
                               param2=acc_thresh,minRadius=min_rad,maxRadius=max_rad)
    try:
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(img_circles,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(img_circles,(i[0],i[1]),2,(0,0,255))
    except:
        pass
    return circles, img_circles

# Get Definite Frame Ball Location
def get_ball_info(circles, crop_info):
    ball_crop_loc = (circles[0][0][0],circles[0][0][1])
    x_ball_cntr =  (crop_info.get('crop_cntr')[0])-(crop_info.get('xy_offset')[0]) + ball_crop_loc[0]
    y_ball_cntr =  (crop_info.get('crop_cntr')[1])-(crop_info.get('xy_offset')[1]) + ball_crop_loc[1]
    ball_radius = circles[0][0][2]
    ball_info = {
                "coordinates":(x_ball_cntr, y_ball_cntr),
                "radius" :ball_radius
    }
    return ball_info

# Create image array from file location (grayscale)
def create_img_array(file_path):
    frames = []
    files = sorted(glob.glob (file_path + "/*.png"))
    for myFile in files:
        image = cv2.imread(myFile,0)
        frames.append(image)
    return frames

# Create image array from file location (color)
def create_img_array_color(file_path):
    frames = []
    files = sorted(glob.glob (file_path + "/*.png"))
    for myFile in files:
        image = cv2.imread(myFile,1)
        frames.append(image)
    return frames


# Save Image Array as File (Don't Reload Every Time)
def save_img_array(image_array, filename):
    with open(filename, 'wb') as f:
        pickle.dump(image_array, f)

# Load Image Array from File
def load_img_array(filename):
    with open(filename, 'rb') as f:
        frames = pickle.load(f)
    return frames


# # Get initial cropped frame (Deprecated--> Used Image Center)
# def init_crop_frame(frames):
#     dimensions = {
#                 "height":frames[0].shape[0],
#                 "width" :frames[0].shape[1]
#     }
#     cntr_pt_im = ((dimensions.get('height')/2), (dimensions.get('width')/2))
#     height_range = (cntr_pt[0]/2, (cntr_pt[0]+ (cntr_pt[0]/2)))
#     width_range = (cntr_pt[1]/2, (cntr_pt[1]+ (cntr_pt[1]/2)))

#     crop_frame = frames[0][int(height_range[0]):int(height_range[1]), int(width_range[0]):int(width_range[1])]
#     return crop_frame

# Get initial cropped frame
def init_crop_frame(frame):
    # Hard-coded Average Blob Center
    x_cntr = 1037
    y_cntr = 379
    x_offset = 200
    y_offset = 100

    height_range = ((y_cntr - 100), (y_cntr + 300))
    width_range = ((x_cntr - 200), (x_cntr + 200))

    crop_frame = frame[int(height_range[0]):int(height_range[1]), int(width_range[0]):int(width_range[1])]

    crop_info = {
                "xy_offset":(x_offset, y_offset),
                "crop_cntr" : (x_cntr, y_cntr)
    }

    return crop_frame, crop_info

# This function needs to be reworked to automatically find the ROI
def crop_frame(frame):
    dimensions = {
                "height":frame.shape[0],
                "width" :frame.shape[1]
    }
    cntr_pt = ((dimensions.get('height')/2), (dimensions.get('width')/2))
    height_range = (cntr_pt[0]/2, (cntr_pt[0]+ (cntr_pt[0]/2)))
    width_range = (cntr_pt[1]/2, (cntr_pt[1]+ (cntr_pt[1]/2)))

    crop_frame = frame[int(height_range[0]):int(height_range[1]), int(width_range[0]):int(width_range[1])]
    return crop_frame

# Crop to Ball Location
def crop_to_ball(frame, ball_info):
    cntr_pt = ball_info.get('coordinates')
    # box_dim = (ball_info.get('radius')*6)
    x_offset = 100
    y_offset = 100
    width = ((cntr_pt[0]-x_offset), (cntr_pt[0] + x_offset))
    height =((cntr_pt[1]-y_offset), (cntr_pt[1] + y_offset))
    crop_frame = frame[int(height[0]):int(height[1]), int(width[0]):int(width[1])]

    crop_info = {
                "xy_offset": (x_offset, y_offset),
                "crop_cntr" : (cntr_pt[0], cntr_pt[1])
    }

    return crop_frame, crop_info

# Show Image Matplotlib
def show_im_plt_gray(image,figure_name=''):
    plt.figure()
    plt.imshow(image, cmap='gray', vmin=0,vmax=255)

# Show Color Image Matplotlib


    

