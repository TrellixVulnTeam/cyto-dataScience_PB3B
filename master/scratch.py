import cv2 
import numpy as np
import matplotlib.pyplot as plt
import glob
import pickle
import copy

class Test():
    def __init__(self, cheese, var="gray"):
        
        self.cheese = cheese
        self.var = var
        
        # switcher = {
        #     'gray': {'ice': testFun},
        #     'color': 1,
        #     'unchanged': -1
        # }
        # flag = switcher.get(var, 0)
        # print(flag)
        # self.img = flag
    
    def switcherMeth(self, ice):
        
        def testFun():
            self.cheese = 37
        

        switcher2 = {
            'gray': {'cream': testFun} 
        }

        runFun = switcher2[self.var][ice]
        runFun()


class Test2():
    pass

pecker = Test('cheddar')
pecker.switcherMeth('cream')

print(pecker.cheese)


