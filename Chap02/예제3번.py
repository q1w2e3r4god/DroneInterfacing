import cv2 as cv
import sys

file_name = 'media/soccer.jpg'
file_name2 = 'media/smile_girl.jpg'
img = cv.imread(file_name)
img2 = cv.imread(file_name2)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))
    
cv.imshow('Image Disply', img)
cv.imshow('Image Dislply2', img2)
    
cv.waitKey()
cv.destroyAllWindows()    
