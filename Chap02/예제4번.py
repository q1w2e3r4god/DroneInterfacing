import cv2 as cv
import sys

file_name = 'media/soccer.jpg'
img = cv.imread(file_name)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, dsize=(0,0), fx=0.1, fy=0.1)
gray_small2 = cv.resize(gray, dsize=(0,0), fx=0.2, fy=0.2)
gray_small3 = cv.resize(gray, dsize=(0,0), fx=0.3, fy=0.3)
gray_small4 = cv.resize(gray, dsize=(0,0), fx=0.4, fy=0.4)
gray_small5 = cv.resize(gray, dsize=(0,0), fx=0.5, fy=0.5)
gray_small6 = cv.resize(gray, dsize=(0,0), fx=0.6, fy=0.6)
gray_small7 = cv.resize(gray, dsize=(0,0), fx=0.7, fy=0.7)
gray_small8 = cv.resize(gray, dsize=(0,0), fx=0.8, fy=0.8)
gray_small9 = cv.resize(gray, dsize=(0,0), fx=0.9, fy=0.9)




cv.imwrite('media/soccer_gray.jpg', gray)
cv.imwrite('media/soccer_gray_small.jpg', gray_small)
cv.imwrite('media/soccer_gray.png', gray)
cv.imwrite('media/soccer_gray_small.png', gray_small)
    
cv.imshow('Color Image', img)
cv.imshow('Gray Image', gray)
cv.imshow('Gray Image Small', gray_small)
cv.imshow('Gray Image Small2', gray_small2)
cv.imshow('Gray Image Small3', gray_small3)
cv.imshow('Gray Image Small4', gray_small4)
cv.imshow('Gray Image Small5', gray_small5)
cv.imshow('Gray Image Small6', gray_small6)
cv.imshow('Gray Image Small7', gray_small7)
cv.imshow('Gray Image Small8', gray_small8)
cv.imshow('Gray Image Small9', gray_small9)
    
cv.waitKey()
cv.destroyAllWindows()    
