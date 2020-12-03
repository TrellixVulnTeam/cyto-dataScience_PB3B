# Writing the initial cropping function
import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

def init_crop_frame(frame_array):
    frame = cv2.imread(frame_array[0],0)
    dimensions = {
                "height":frame.shape[0],
                "width" :frame.shape[1]
    }
    cntr_pt = ((dimensions.get('height')/2), (dimensions.get('width')/2))
    height_range = (cntr_pt[0]/2, (cntr_pt[0]+ (cntr_pt[0]/2)))
    width_range = (cntr_pt[1]/2, (cntr_pt[1]+ (cntr_pt[1]/2)))

    crop_frame = frame[int(height_range[0]):int(height_range[1]), int(width_range[0]):int(width_range[1])]
    return crop_frame
    plt.figure('Cropped')
    plt.imshow(crop_frame, cmap='gray', vmin=0, vmax=255)
    plt.show()


print(cntr_pt)
print(width_range[1])
print(height_range[0])