import cv2 as cv
import numpy as np

img1=cv.imread('Children.jpg')[0:350,0:580] # 버스를 크롭하여 모델 영상으로 사용
gray1=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
img2=cv.imread('Child.jpg')			     # 장면 영상
gray2=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

sift=cv.SIFT_create()
kp1,des1=sift.detectAndCompute(gray1,None)
kp2,des2=sift.detectAndCompute(gray2,None)

flann_matcher=cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
knn_match=flann_matcher.knnMatch(des1,des2,2)	# 최근접 2개

T=0.7
good_match=[]
for nearest1,nearest2 in knn_match:
    if (nearest1.distance/nearest2.distance)<T:
        good_match.append(nearest1)

points1=np.float32([kp1[gm.queryIdx].pt for gm in good_match]) # 첫 번째 영상의 특징점들의 좌표
points2=np.float32([kp2[gm.trainIdx].pt for gm in good_match]) # 두 번째 영상의 특징점들의 좌표

H,_=cv.findHomography(points1,points2,cv.RANSAC) # 호모그래피 행렬 추가

h1,w1=img1.shape[0],img1.shape[1] 		# 첫 번째 영상의 크기
h2,w2=img2.shape[0],img2.shape[1] 		# 두 번째 영상의 크기

box1=np.float32([[0,0],[0,h1-1],[w1-1,h1-1],[w1-1,0]]).reshape(4,1,2) # 네 구석의 좌표를 box1에 저장
box2=cv.perspectiveTransform(box1,H) # 네 구석의 좌표를 호모그래피 행렬을 적용하여 두 번째 영상으로 투영한 결과를 box2에 저장

img2=cv.polylines(img2,[np.int32(box2)],True,(0,255,0),8) # box2를 영상에 그린다.

img_match=np.empty((max(h1,h2),w1+w2,3),dtype=np.uint8) # 두 영상을 옆으로 배치한다.
cv.drawMatches(img1,kp1,img2,kp2,good_match,img_match,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS) # 특징점 정보와 매칭 정보를 그린다.
   
cv.imshow('Matches and Homography',img_match)

k=cv.waitKey()
cv.destroyAllWindows()