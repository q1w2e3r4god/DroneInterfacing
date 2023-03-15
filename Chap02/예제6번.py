import cv2 as cv
import sys

file_name = 'media/smile_girl.jpg' # for jupyter or ipython(spyder)
img = cv.imread(file_name)

if img is None:
    sys.exit('파일({0})을 찾을 수 없습니다.'.format(file_name))

cv.rectangle(img, (580,100), (880,530), (0,0,255), 2)
cv.putText(img, 'smile', (580,94), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)

cv.imshow('Draw', img)
cv.waitKey()
cv.destroyAllWindows()    
