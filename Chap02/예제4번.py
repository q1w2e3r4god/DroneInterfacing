# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 04:49:20 2023

@author: hwlee

change images

"""
import cv2 as cv
import sys

file_name = './soccer.jpg'
img = cv.imread(file_name)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, dsize=(0,0), fx=0.5, fy=0.5)

cv.imwrite('./soccer_gray.jpg', gray)
cv.imwrite('./soccer_gray_small.jpg', gray_small)
cv.imwrite('./soccer_gray.png', gray)
cv.imwrite('./soccer_gray_small.png', gray_small)
    
cv.imshow('Color Image', img)
cv.imshow('Gray Image', gray)
cv.imshow('Gray Image Small', gray_small)
    
cv.waitKey()
cv.destroyAllWindows()    
