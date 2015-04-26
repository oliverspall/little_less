##..................................A LITTLE LESS CONDENSATION...............................................................
##Following some experiments capturing images and video (in video_frames_n_n), this aims to bring together the database //
##and the face detection code into something that hopefully populates a database, and calls images for manipulation.
##
##..................................DEPENDENCIES.............................................................................
##Requires a good install of OpenCV2 which is a massive pain to install so book yourself a day to get this done.
##Also required:
##Settings_DB - this contains database instructions and the schema.
##
##..................................MORE INFORMATION:........................................................................
##This draws heavily on documentation in the OpenCV support site - here: http://docs.opencv.org
##Also code relies heavily on guidance from: <names needed>
##FUNCTIONALITY:
##This script enables a camera to scan a scene and identify faces in that scene. From there, the script will identify where the//
##faces are, draw a green square around the faces, and then crop the faces into a smaller image for further analysis.
##This is done via a database that stores the images, and then analyses them against a 'trained' facial recognition algorithm.
##Refer to the following code: facerec_eigenfaces.cpp for more details and further documentation.
##What we will then get is a statistical output of the 'matchiness' between the faces that have been seen, and how much they //
##coincide with an eigenvector (again, see facerec_eigenfaces.cpp for more documentation)
##Version video_frames_0_1: simple initiation of video, face detection in images.
##Version video_frames_0_2: added bounding box where face is detected. Save image w/ box identifying face
##Version video_frames_0_3: crop to box to show only face detected.
##Version video_frames_0_4: output to specified directory and include Haarcascade file in setup rather than on command line.
##(though deprecating this as it is a bit of a pain)
##Version less_condensation_0_1: starting to build the full script. First step includes threading to start to build the //
##image parsing to and calling from database, and perhaps the image manipulation, but I'm not sure about that yet.
##

##Dependencies:
import cv2
import cv
import numpy
import datetime
import time
import sys
import os
import threading
import settings_DB

##this sets up how the video is captured. it should allow me to change frame rate etc. - but it doesn't.
#if os.path.exists("/home/imiant/opencv/OpenCV/opencv-2.4.9/data/haarcascades/haarcascade_frontalface_default.xml"):
#	cascPath = os.path.join("home/imiant/opencv/OpenCV/opencv-2.4.9/data/haarcascades", "haarcascade_frontalface_default.xml")
cascPath = sys.argv[1]
print cascPath
cap = cv2.VideoCapture(1)
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

def startthreads():
	threading.Thread(target=face_rec).start()
	threading.Thread(target=check_new_faces).start()

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
				unique_id = timestamp
				cv2.imwrite(os.path.join("crop"+unique_id+".jpg",crop))
				image_loc = (os.path.join("crop"+unique_id+".jpg")
				#cv.Copy(image, crop, mask=None)
				cv2.imshow("cropped", crop)
				cv2.waitKey(25)
				filename = ("crop"+unique_id)
				print filename
				status = settings_DB.NEW
				print status
				#face_id, image_loc, timestamp, filename, status) VALUES(?,?,?,?)', values
				settings_DB.settings.insert_value(timestamp, image_loc, timestamp, filename, status)

			time.sleep(1)
			print "waiting for 1 second"
			#print "saving images"

	#here's just a bit of control:
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	#this final section just stops the process when finished:
	cap.release()
	cv2.destroyAllWindows()

def check_new_faces(faces):
	#identify whether there are new images


def compare_new_faces():
	#compares the faces with the database of elvises
	#adds data to the elvis database where needed

def analyse_manipulate_image():
	#this should ideally do the analysis & parse image information based on % probability


if __name__ == '__main__':
	while True:
		startthreads()
		#face_rec()
