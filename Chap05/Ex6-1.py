import cv2 as cv
import numpy as np

# 이미지 읽기
img = cv.imread('SON.jpg')

# 옥타브 값 설정
octave = 0

# 6개의 가우시안 필터 생성
ksize = 3
sigma = 1.6
gauss_pyr = [cv.cvtColor(img, cv.COLOR_BGR2GRAY)]
for i in range(6):
    gauss_pyr.append(cv.GaussianBlur(gauss_pyr[i], (ksize, ksize), sigma))

# 5개의 DoG 필터 생성
dog_pyr = []
for i in range(5):
    dog_pyr.append(cv.absdiff(gauss_pyr[i], gauss_pyr[i+1]))

# 결과 영상 디스플레이
for i in range(6):
    cv.imshow('Gaussian Image Level ' + str(i+1), gauss_pyr[i])
for i in range(5):
    cv.imshow('DoG Image Level ' + str(i+1), dog_pyr[i])

cv.waitKey()
cv.destroyAllWindows()