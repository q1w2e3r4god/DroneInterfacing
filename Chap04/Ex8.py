import cv2 as cv

img=cv.imread('soccer.jpg')	# 영상 읽기

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

canny1=cv.Canny(gray, 50, 100, apertureSize = 3, L2gradient = False)	
canny2=cv.Canny(gray, 50, 200, apertureSize = 3, L2gradient = False)	

cv.imshow('Original',gray)
cv.imshow('Canny1',canny1)
cv.imshow('Canny2',canny2)

cv.waitKey()
cv.destroyAllWindows()

# image : 입력 영상이다.
# edges : 출력 매개변수로 Canny 알고리즘에 의해 검출된 edge를 저장한다.
# threshold1: 이진화를 위한 첫 번째 임계값이다. 이 값보다 큰 Gradient 값 중, 이웃한 픽셀과 차이가 threshold2보다 큰 픽셀을 Edge로 인식한다.
# threshold2: 이진화를 위한 두 번째 임계값이다. 이 값보다 작은 Gradient 값 중, 이웃한 픽셀과 차이가 threshold1보다 큰 픽셀을 Edge로 인식한다.
# apertureSize: edge 검출을 위한 Sobel 커널의 크기이다. 기본값은 3이다.
# L2gradient: Sobel 커널의 크기를 이용하여 Gradient 크기를 계산할 때, L1 노름 또는 L2 노름을 사용할 지 여부를 결정한다. 본값은 False이며, True로 설정하면 L2 노름을 사용한다.

# threshold1의 값을 높일수록 엣지로 인식되기 위한 경계값이 높아져서 더 강한 엣지만 검출하게된다.
# 따라서, threshold1의 값을 높일수록 노이즈가 줄어들고 더 정확한 엣지를 검출할 수 있다.

# threshold2의 값을 높일수록 엣지 검출 결과가 더욱 강력해진다.

# apertureSize의 값을 높일수록 엣지 감지를 위한 Sobel 커널의 크기가 커지게 된다.
# 따라서, 더 넓은 영역을 고려하여 엣지를 검출하게된다.

# L2gradient의 값이 False 일 때는 일반적인 이미지 경계 검출이지만
# L2gradient의 값이 True 일 때는 더욱 부드러운 경계를 검출한다.

