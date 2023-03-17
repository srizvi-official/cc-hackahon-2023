import cv2 as cv
import time
import gtts
from playsound import playsound

def readImage(path):
	img = cv.imread(path)
	return img

def convertToGrayScale(img):
	gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	return gray_image

def printImage(img):
	print(img)
	cv.imshow('image',img)
	cv.waitKey(0)
	cv.destroyAllWindows()

def recordVideo():

	now = str(int(time.time()))
	filename = 'video_' + now +'.mp4'
	cap=cv.VideoCapture(0)
	width= int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
	height= int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
	writer= cv.VideoWriter(filename, cv.VideoWriter_fourcc(*'DIVX'), 20, (width,height))

	while True:
	    ret,frame= cap.read()
	    writer.write(frame)
	    cv.imshow('frame', frame)
	    if cv.waitKey(1) & 0xFF == 27:
	        break

	cap.release()
	writer.release()
	cv.destroyAllWindows()


def speak(text):
	now = str(int(time.time()))
	filename = 'audio_' + now +'.mp3'
	tts = gtts.gTTS(text)
	tts.save(filename)
	playsound(filename)


def testDrive():
	#recordVideo()
	#speak('Hi My name is Rubab')

testDrive()
