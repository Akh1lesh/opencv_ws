import urllib
import cv2
import numpy as np
import os

def create_pos_n_neg():
    for file_type in ['/home/thanos/opencv_ws/info']:
        
        for img in os.listdir(file_type):

            if file_type == '/home/thanos/opencv_ws/info':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
create_pos_n_neg()