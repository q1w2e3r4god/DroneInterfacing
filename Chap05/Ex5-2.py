import cv2 as cv

img=cv.imread('mot_color70.jpg') # 영상 읽기
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

nfeatures = [2, 4, 8, 16, 32, 64, 128, 256, 512] # 키포인트 수 리스트

for n in nfeatures:
    sift=cv.SIFT_create(nfeatures=n) 
    kp,des=sift.detectAndCompute(gray,None)
    
    img_with_kp = cv.drawKeypoints(gray, kp, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv.imshow('sift_{}'.format(n), img_with_kp)

k=cv.waitKey()
cv.destroyAllWindows()
