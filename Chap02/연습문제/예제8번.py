# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 04:49:20 2023

@author: hwlee

GUI

"""
import cv2 as cv
import sys

#file_name = './Chap02/smile_girl.jpg' # for VSCODE working directory is Chap02
file_name = './smile_girl.jpg' # for jupyter or ipython(spyder)
img = cv.imread(file_name)
img0 = cv.imread(file_name)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))
def draw(event, x, y, flags, param):
    global ix, iy
    if event == cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        img[:,:,:] = img0[:,:,:]
        cv.rectangle(img, (ix,iy), (x, y), (255, 0, 255), 2)
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img, (ix,iy), (x, y), (0, 0, 255), 2)
    cv.imshow('Drawing', img)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)

cv.setMouseCallback('Drawing', draw)

while(True):
    if cv.waitKey(1) == ord('q'):        
        cv.destroyAllWindows()
        break
