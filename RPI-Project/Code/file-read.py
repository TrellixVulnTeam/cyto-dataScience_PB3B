import cv2 
import numpy as np
import matplotlib.pyplot as plt
import glob

def create_img_array(file_path):
    frames = []
    files = glob.glob (file_path + "/*.png")
    for myFile in files:
        image = cv2.imread(myFile,0)
        frames.append(image)

    for frame in frames:
        plt.figure()
        plt.imshow(frame, cmap='gray', vmin=0, vmax=255)
    return frames