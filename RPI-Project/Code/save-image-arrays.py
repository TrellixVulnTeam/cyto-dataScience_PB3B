import cv2 
import numpy as np
import matplotlib.pyplot as plt
import glob
import functions as myFun
import pickle

# Create Image Arrays
Kick_1_24ft = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/24ft-Cntr/Frames/Kick-1')
Kick_2_24ft = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/24ft-Cntr/Frames/Kick-2')
Kick_3_24ft = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/24ft-Cntr/Frames/Kick-3')

Kick_1_30ft = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/30ft-Cntr/Frames/Kick-1')
Kick_2_30ft = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/30ft-Cntr/Frames/Kick-2')
Kick_3_30ft = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/30ft-Cntr/Frames/Kick-3')

Kick_1_36ft = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/36ft-Cntr/Frames/Kick-1')
Kick_2_36ft = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/36ft-Cntr/Frames/Kick-2')
Kick_3_36ft = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/36ft-Cntr/Frames/Kick-3')

Kick_1_42ft = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/42ft-Cntr/Frames/Kick-1')
Kick_2_42ft = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/42ft-Cntr/Frames/Kick-2')
Kick_3_42ft = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/42ft-Cntr/Frames/Kick-3')

Kick_1_36ft_OS_Left = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/36ft-9ftOS-Left/Frames/Kick-1')
Kick_2_36ft_OS_Left = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/36ft-9ftOS-Left/Frames/Kick-2')
Kick_3_36ft_OS_Left = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/36ft-9ftOS-Left/Frames/Kick-3')

Kick_1_36ft_OS_Right = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/36ft-9ftOS-Right/Frames/Kick-1')
Kick_2_36ft_OS_Right = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/36ft-9ftOS-Right/Frames/Kick-2')
Kick_3_36ft_OS_Right = myFun.create_img_array('/home/dan/Documents/Create/Deadeye/Image-Processing/Frames/Analysis-Video/36ft-9ftOS-Right/Frames/Kick-3')

# Save Image Arrays
myFun.save_img_array(Kick_1_24ft, '24ft-Kick1')
myFun.save_img_array(Kick_2_24ft, '24ft-Kick2')
myFun.save_img_array(Kick_3_24ft, '24ft-Kick3')

myFun.save_img_array(Kick_1_30ft, '30ft-Kick1')
myFun.save_img_array(Kick_2_30ft, '30ft-Kick2')
myFun.save_img_array(Kick_3_30ft, '30ft-Kick3')

myFun.save_img_array(Kick_1_36ft, '36ft-Kick1')
myFun.save_img_array(Kick_2_36ft, '36ft-Kick2')
myFun.save_img_array(Kick_3_36ft, '36ft-Kick3')

myFun.save_img_array(Kick_1_42ft, '42ft-Kick1')
myFun.save_img_array(Kick_2_42ft, '42ft-Kick2')
myFun.save_img_array(Kick_3_42ft, '42ft-Kick3')

myFun.save_img_array(Kick_1_36ft_OS_Right, '36ft-OS-Right-Kick1')
myFun.save_img_array(Kick_2_36ft_OS_Right, '36ft-OS-Right-Kick2')
myFun.save_img_array(Kick_3_36ft_OS_Right, '36ft-OS-Right-Kick3')

myFun.save_img_array(Kick_1_36ft_OS_Left, '36ft-OS-Left-Kick1')
myFun.save_img_array(Kick_2_36ft_OS_Left, '36ft-OS-Left-Kick2')
myFun.save_img_array(Kick_3_36ft_OS_Left, '36ft-OS-Left-Kick3')










