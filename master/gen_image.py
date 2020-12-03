import cv2 
import numpy as np
import matplotlib.pyplot as plt
import glob
import pickle
import copy

class GenImage():
    """ Image class created for generated images """

    def __init__(self, height, width, data_type):
        self.height = height
        self.width = width
        self.data_type = data_type
        self.image = np.zeros((height,width), data_type)
    
    def bw_half_n_half(self, orientation="vertical"):
        # Reset to Zeros
        self.image = np.zeros((self.height, self.width), np.uint8)

        # Set Geometry
        if orientation == "vertical":
            self.image[: ,0:self.width//2] = (255)
            self.image[:,self.width//2:self.width] = (0)
        if orientation == "horizontal":
            self.image[0:self.height//2, :] = (255)
            self.image[self.height//2:self.height,:] = (0)
    
    def bw_checkerboard(self, square_size):
        # Reset to Zeros
        self.image = np.zeros((self.height, self.width), np.uint8)

        # Set Geometry
        cycles = self.height // square_size

        for i in range(0, cycles):
            row = i*square_size
            for j in range(0, self.height, square_size*2):
                if (row%(square_size*2)) == 0:
                    self.image[row:row+square_size, j:j+square_size] = (255)
                else:
                    self.image[row:row+square_size, j+square_size:j+(square_size*2)] = (255)

    def show_im(self, figure_name=''):
        plt.figure(figure_name)
        plt.imshow(self.image, cmap='gray', vmin=0, vmax=255)
        plt.show()
    
    def show_fft(self):
        f = np.fft.fft2(self.image)
    
    # def grayscale_cos(self, f)
 