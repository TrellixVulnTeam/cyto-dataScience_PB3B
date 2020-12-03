import cv2 
import numpy as np
import matplotlib.pyplot as plt
import glob
import functions as myFun
import pickle


rel_path = "Image-Arrays/24ft-Kick2"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('24ft-Kick2.png',im_array[0])

rel_path = "Image-Arrays/24ft-Kick3"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('24ft-Kick3.png',im_array[0])

rel_path = "Image-Arrays/30ft-Kick1"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('30ft-Kick1.png',im_array[0])

rel_path = "Image-Arrays/30ft-Kick2"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('30ft-Kick2.png',im_array[0])

rel_path = "Image-Arrays/30ft-Kick3"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('30ft-Kick3.png',im_array[0])

rel_path = "Image-Arrays/36ft-Kick1"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('36ft-Kick1.png',im_array[0])

rel_path = "Image-Arrays/36ft-Kick2"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('36ft-Kick2.png',im_array[0])

rel_path = "Image-Arrays/36ft-Kick3"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('36ft-Kick3.png',im_array[0])

rel_path = "Image-Arrays/42ft-Kick1"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('42ft-Kick1.png',im_array[0])

rel_path = "Image-Arrays/42ft-Kick2"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('42ft-Kick2.png',im_array[0])

rel_path = "Image-Arrays/42ft-Kick3"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('42ft-Kick3.png',im_array[0])

rel_path = "Image-Arrays/36ft-OS-Left-Kick1"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('36ft-OS-Left-Kick1.png',im_array[0])

rel_path = "Image-Arrays/36ft-OS-Left-Kick2"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('36ft-OS-Left-Kick2.png',im_array[0])

rel_path = "Image-Arrays/36ft-OS-Left-Kick3"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('36ft-OS-Left-Kick3.png',im_array[0])

rel_path = "Image-Arrays/36ft-OS-Right-Kick1"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('36ft-OS-Right-Kick1.png',im_array[0])

rel_path = "Image-Arrays/36ft-OS-Right-Kick2"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('36ft-OS-Right-Kick2.png',im_array[0])

rel_path = "Image-Arrays/36ft-OS-Right-Kick3"
im_array = myFun.load_img_array(rel_path)
cv2.imwrite('36ft-OS-Right-Kick3.png',im_array[0])

# Come back, save initial images to folder, do regionprops and get averages so that you can blob detect for every frame
# 


# cv2.imwrite('messigray.png',img)