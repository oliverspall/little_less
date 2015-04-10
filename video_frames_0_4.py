##This is the second piece of code that I have written for
##my minor project.
##
##Preferably, if you could read the code with the following software
##and visual treatment, it may hurt your eyes less. It will also make me
##feel a sort of godly power over you.
##Please use: Sublime Text 3
##Please view in: iPlastic Colour Scheme.
##
##Thank you.
##
##This aims to test out whether it is possible to import video
##into the application and break out frames from the live video 
##for analysis.
##It is the result of 2 weeks of rebuilding and rebuilding two
##machines that just wouldn't behave.
##
##An overview of how one of these machines fared can be found in
##the syslog file that is part of this documentation. I have found
##the command line work invigorating as I now have a good understanding
##of the Linux file system, and a lot more knowledge about the kernel.
##
##What I now plan on doing is to read this book by Robert Love: 
##"Linux Kernel Development" - available here: http://www.amazon.com/
##Linux-Kernel-Development-Robert-Love/dp/0672329468/ref=sr_1_1?s=books
##&ie=UTF8&qid=1425567602&sr=1-1&keywords=linux+kernel+love
##
##
##
##Dependencies for this script are as follows:
##1) OpenCV - this is pretty much what drives this. more detail on opencv
##here: www.opencv.org, but in brief, it is an open source computer vision
##and machine learning platform, written in C++ but with Python bindings. I'm
##curious at this point whether what I will end up doing is writing in Python 
##(most familiar with this language) or if I will need to drop down a level to
##experience the joy of writing C. We will find out.
##2) Numpy - which is a Python mathematics module that operates in a similar way
##to MATLAB. This is for visualising mathematical calculations on stuff like photos
##video, images etc. I hope that I will not need to do too much with this library
##and that it works out of the box. Doubtful, but I am an ever-persistent optimist.
##
##Something to mention is that this code bears a world of debt to the excellent
##documentation at docs.opencv.org
##
##I would be lost without this.
##
##
##here we go.
##
##Version 0_1: simple initiation of video, face detection in images.
##Version 0_2: added bounding box where face is detected. Save image w/ box identifying face
##Version 0_3: crop to box to show only face detected.
##Version 0_4: output to specified directory and include Haarcascade file in setup rather than on command line.

##Dependencies:
import cv2
import cv
import numpy
import datetime
import time
import sys
import os

##this sets up how the video is captured. it should allow me to change frame rate etc. - but it doesn't.
#if os.path.exists("/home/imiant/opencv/OpenCV/opencv-2.4.9/data/haarcascades/haarcascade_frontalface_default.xml"):
#	cascPath = os.path.join("home/imiant/opencv/OpenCV/opencv-2.4.9/data/haarcascades", "haarcascade_frontalface_default.xml")
cascPath = sys.argv[1]
print cascPath
cap = cv2.VideoCapture(0)
ramp_frames = 30
faceCascade = cv2.CascadeClassifier(cascPath)
if os.path.exists("/home/imiant/Documents/little_less/crops/") == False:
	print os.path.exists("/home/imiant/Documents/little_less/crops/")
	dirname = 'crops'
	os.mkdir(dirname)
else:
	dirname = 'crops'


#else:
#	print "error - no facial recognition cascade"


#what this does is it sets where the script will look for a camera source. As most machines
##only have 1 camera, you usually need to pass either 0 or 1. If you want to use a file
##you can specify the source here. it also discards 30 frames to allow for the webcam to adjust
##
def face_rec():
	while(True):
		#this captures frames
		#retval, im = cap.read()
		#time.sleep(1)
		#here is what we are going to do with these frames to make them readable:
		
		#funnily enough, the greyscale is pretty important to make recognising faces
		#even possible - it has all sorts of links to the greyness or 'boringness' of
		#other media systems. More later on that.

		#next we will show the frame we have captured:
		#cv2.imshow('im', gray)

		#this saves the frames as individual files with a timestamp and as a jpeg:
		rolling = True
		while rolling:
			timestamp = str(datetime.datetime.now())
			rolling, image = cap.read()
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			#cv2.imshow(image, gray)
			# Detect faces in the image using the OpenCV XML facial recognition cascade.
			faces = faceCascade.detectMultiScale(
			    gray,
			    scaleFactor=1.1,
			    minNeighbors=5,
			    minSize=(30, 30),
			    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
			)
			print "Found {0} faces".format(len(faces))
	#this part below prints a square onto the image where faces have been recognised.
			for (x, y, w, h) in faces:
				print (x, y, w, h)
				cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
				#cv2.imshow("Faces found", image)
				#crop_rectangle = cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
				cv2.imwrite(os.path.join(dirname, ("still_"+timestamp+".jpg")),image)
				print "saving image"
				cv2.imshow("Faces found", image)



				#at this point we will now need to create a crop of the image, and start to think about how it gets put in the DB
				#the below was an initial test to see whether I could simply take the coordinates from above and crop.
				#doesn't work yet.

						#final_img = image[cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)]
						#cv2.imshow("Cropped_image", final_image)
						#cv2.imwrite("crop_"+timestamp+".jpg",final_img)
				crop = image[y:y+h, x:x+w]
				print (x, w, y, h)
				path = os.path.join("")
				cv2.imwrite("crop"+timestamp+".jpg",crop)
				#cv.Copy(image, crop, mask=None)
				cv2.imshow("cropped", crop)
				cv2.waitKey(25)				


			time.sleep(1)
			print "waiting for 1 second"
			#print "saving images"

	#here's just a bit of control:
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	#this final section just stops the process when finished:
	cap.release()
	cv2.destroyAllWindows()


if __name__ == '__main__':
	while True:
		face_rec()
