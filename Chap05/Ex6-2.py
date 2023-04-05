import cv2 as cv
import numpy as np

# 이미지 읽기
img = cv.imread('SON.jpg')

# 옥타브 값 설정
octave = 0
n_levels = 3

# 가우시안 필터 생성
ksize = 3
sigma = 1.6
gauss_pyr = [cv.cvtColor(img, cv.COLOR_BGR2GRAY)]

for i in range(n_levels-1):
    sigma_f = np.sqrt(sigma ** 2 - (sigma / 2) ** 2)  # 다음 레벨의 시그마 계산
    ksize_f = int(2 * np.ceil(3 * sigma_f) + 1)  # 커널 사이즈 계산
    gauss_pyr.append(cv.GaussianBlur(gauss_pyr[i], (ksize_f, ksize_f), sigma_f))

# DoG 필터 생성
dog_pyr = []
for i in range(n_levels-1):
    dog_pyr.append(cv.absdiff(gauss_pyr[i], gauss_pyr[i+1]))

# 결과 영상 디스플레이
for i in range(n_levels):
    cv.imshow('Gaussian Image Level ' + str(i+1), gauss_pyr[i])
for i in range(n_levels-1):
    cv.imshow('DoG Image Level ' + str(i+1), dog_pyr[i])

cv.waitKey()
cv.destroyAllWindows()
