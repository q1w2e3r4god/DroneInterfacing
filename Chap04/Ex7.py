import cv2 as cv

img=cv.imread('soccer.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

grad_x=cv.Sobel(gray,cv.CV_32F,1,0,ksize=3) # 소벨 연산자 적용
grad_y=cv.Sobel(gray,cv.CV_32F,0,1,ksize=3)

sobel_x=cv.convertScaleAbs(grad_x) # 절대값을 취해 양수 영상으로 변환
sobel_y=cv.convertScaleAbs(grad_y)

scharr_x = cv.Scharr(gray,cv.CV_32F,1,0)
scharr_y = cv.Scharr(gray,cv.CV_32F,0,1)

sobel_x=cv.convertScaleAbs(grad_x) # 절대값을 취해 양수 영상으로 변환
sobel_y=cv.convertScaleAbs(grad_y)
scharr_x = cv.convertScaleAbs(scharr_x)
scharr_y = cv.convertScaleAbs(scharr_y)

edge_strength_sobel=cv.addWeighted(sobel_x,0.5,sobel_y,0.5,0) # 소벨 에지 강도 계산
edge_strength_scharr=cv.addWeighted(scharr_x,0.5,scharr_y,0.5,0) # 샤르 에지 강도 계산

cv.imshow('sobelx',sobel_x)
cv.imshow('sobely',sobel_y)
cv.imshow('edge strength (Sobel)',edge_strength_sobel)
cv.imshow('scharrx',scharr_x)
cv.imshow('scharry',scharr_y)
cv.imshow('edge strength (Scharr)',edge_strength_scharr)

cv.waitKey()
cv.destroyAllWindows()

# Scharr 연산자는 이미지의 엣지를 검출하는데 사용되는 컨볼루션 필터 중 하나이다.
# Sobel 연산자와 다르게 3x3 크기의 필터 뿐만 아닌 5x5 크기의 필터 모두를 사용한다.
# 따라서, Scharr 연산자가 Sobel 연산자보다 엣지 검출의 정확도가 더 높은 것을 알 수 있다.