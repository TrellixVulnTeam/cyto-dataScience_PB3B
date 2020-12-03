import cv2 
import numpy as np
import matplotlib.pyplot as plt
import glob
import pickle
import copy

class Image():
    """ This is an image class designed to give basic image functionality
    including showing, getting basic info, duplicate, crop, and perform 
    other basic functionality on images.
    """

    """Create class attributes"""
    cv_flags = {
        'gray'      :  0,
        'color'     :  1,
        'unchanged' : -1
    }

    def __init__( self, image_filename, image_name, color_model='gray' ):
        """ Initialize instance attributes to describe an image """
        cv_flag             = Image.cv_flags.get(color_model, 'gray')
        self.image_filename = image_filename
        self.image_name     = image_name
        self.image          = cv2.imread(image_filename, cv_flag)
        self.shape          = self.image.shape
        self.height         = self.shape[0]
        self.width          = self.shape[1]
        if len(self.shape) > 2:
            self.channel_cnt    = self.shape[2]
        else:
            self.channel_cnt    = 1
        if 1 < self.channel_cnt < 4:     # Set default colorspace to RGB
            self.image       = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.color_space = 'RGB'
        elif self.channel_cnt > 3:
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGRA2RGBA)
            self.color_space = 'RGBA'
        else:
            self.color_space = 'Grayscale'
        # self.histr = cv2.calcHist([self.image], [0], None, [256], [0,256])
    
    def print_info(self):
        """ Print a statement with basic image info."""
        # Note: change Image Info to something more descriptive
        line_len = len(self.image_name) + 10
        print("-"*line_len)
        print("---- " + self.image_name + " ----")
        print("-"*line_len)
        print("Original Filename : " + self.image_filename)
        print("Height            : " + str(self.height))
        print("Width             : " + str(self.width))
        print("Color Channels    : " + str(self.channel_cnt))
        print("Color Space       : " + self.color_space)
        print("")

    def cvt_color(self, color='RGB'):
        """ Create a convert color function keyword switch """

        def RGBtoBGR(color=color):
            self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
            self.color_space = 'BGR'     
        
        def BGRtoRGB(color=color):
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.color_space = 'RGB'
        
        def RGBAtoRGB(color=color):
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGRA2BGR)
            self.color_space = 'RGB'

        cvtColorSwitcher = {
            'RGB': {'RGB': RGBtoBGR},
            'RGBA': {'RGB': RGBAtoRGB}
        }

        function = cvtColorSwitcher[self.color_space][color]
        function()
        


    def show_gray_im(self, figure_name=''):
        plt.figure(figure_name)
        plt.imshow(self.image, cmap='gray', vmin=0, vmax=255)
 
    def show_hist(self):
        plt.figure('Image Histogram')
        plt.plot(self.histr)
        plt.xlim([0,256])

    def simple_stretch(self, L, H):
        stretch = copy.deepcopy(self)
        stretch.image = ((255/(H-L))*(stretch.image-L))
        stretch.image = stretch.image.astype(np.uint8)
        stretch.image[stretch.image > 255] = 255
        stretch.image[stretch.image < 0] = 0
        stretch.histr = cv2.calcHist([stretch.image], [0], None, [256], [0,256])
        return stretch

    def crop_image(self, start_x, start_y, end_x, end_y):
        crop = copy.deepcopy(self)
        crop.image = crop.image[start_y:end_y, start_x:end_x]
        crop.image = crop.image.astype(np.uint8)
        return crop 
    
    def grab_area(self):
        # Get ROI of image
        (x_0, y_0, x_os, y_os) = cv2.selectROI("Original Image", self.g_xy,\
        True, False)

        # Crop image to ROI and create new image
        g_xy_crop = self.g_xy[ y_0:(y_0+y_os), x_0:(x_0+x_os) ]
        g_xy_crop = Waveform_2D(wave=g_xy_crop)
        return g_xy_crop       

cells = Image('RK1.jpg', 'Original Cell Image', color_model='color')
cells.print_info()

png = Image('Blueprint_Cut.png', 'Blueprint Translucent PNG', color_model='unchanged')
png.print_info()

png_gray = Image('Blueprint_Cut.png', 'Blueprint Grayscale', color_model='gray')
png_gray.print_info()

png.cvt_color('RGB')
png.print_info()

print(png.shape)
