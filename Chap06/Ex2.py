from PyQt5.QtWidgets import *
import sys
import cv2 as cv
import numpy as np

class Video(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle('비디오에서 프레임 수집')	# 윈도우 이름과 위치 지정
        self.setGeometry(200,200,550,100)

        videoButton=QPushButton('비디오 켜기',self)	# 버튼 생성
        captureButton=QPushButton('프레임 잡기',self)
        saveButton=QPushButton('프레임 저장',self)
        multiCaptureButton=QPushButton('여러 프레임 잡기',self)
        quitButton=QPushButton('나가기',self)
        
        videoButton.setGeometry(10,10,100,30)		# 버튼 위치와 크기 지정
        captureButton.setGeometry(110,10,100,30)
        saveButton.setGeometry(210,10,100,30)
        multiCaptureButton.setGeometry(310,10,100,30)
        quitButton.setGeometry(410,10,100,30)
        
        videoButton.clicked.connect(self.videoFunction) # 콜백 함수 지정
        captureButton.clicked.connect(self.captureFunction)         
        saveButton.clicked.connect(self.saveFunction)
        multiCaptureButton.clicked.connect(self.multiCaptureFunction)
        quitButton.clicked.connect(self.quitFunction)
       
    def videoFunction(self):
        self.cap=cv.VideoCapture(0,cv.CAP_DSHOW)	# 카메라와 연결 시도
        if not self.cap.isOpened(): self.close()
            
        while True:
            ret,self.frame=self.cap.read() 
            if not ret: break            
            cv.imshow('video display',self.frame)
            cv.waitKey(1)
        
    def captureFunction(self):
        self.capturedFrame=self.frame
        cv.imshow('Captured Frame',self.capturedFrame)
        
    def saveFunction(self):				# 파일 저장
        fname=QFileDialog.getSaveFileName(self,'파일 저장','./')
        cv.imwrite(fname[0],self.capturedFrame)
        
    def multiCaptureFunction(self):
        self.capturedFrames = []     # 캡처된 프레임들을 저장하는 리스트 초기화
        
        while True:
            ret,frame = self.cap.read() 
            if not ret: break            
            cv.imshow('video display',frame)
            cv.waitKey(1)
            
            # c키를 누르면 현재 프레임을 캡처하고 리스트 추가
            key = cv.waitKey(25)
            if key == ord('c'):
                self.capturedFrames.append(frame)
                print('캡쳐되었습니다.')
            elif key == ord('q'):
                break
                
        # 모든 프레임을 이어붙임
        result = np.concatenate(self.capturedFrames, axis=1)
        cv.imshow('Captured Frames',result)
        self.capturedFrame = result    # 이어붙인 결과를 최종 프레임으로 저장
        
        
    def saveFunction(self):				# 파일 저장
        fname=QFileDialog.getSaveFileName(self,'파일 저장','./')
        cv.imwrite(fname[0],self.capturedFrame)
        
    def quitFunction(self):
        self.cap.release()				# 카메라와 연결을 끊음
        cv.destroyAllWindows()
        self.close()
                
app=QApplication(sys.argv) 
win=Video() 
win.show()
app.exec_()