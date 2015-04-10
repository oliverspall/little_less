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
##Version less_condensation_0_2: started to write the functions for querying and updating the database. Slowly.

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
from DatabaseBuilder import DatabaseBuilder
import sqlite3
import DB_Manager

NEW = 0
EXISTING = 1
#Here are status settings for the images that we capture so we know which ones are new, which ones have been analysed and //
#which ones match / don't match.

##this sets up how the video is captured. it should allow me to change frame rate etc. - but it doesn't.
#if os.path.exists("/home/imiant/opencv/OpenCV/opencv-2.4.9/data/haarcascades/haarcascade_frontalface_default.xml"):
#	cascPath = os.path.join("home/imiant/opencv/OpenCV/opencv-2.4.9/data/haarcascades", "haarcascade_frontalface_default.xml")
cascPath = sys.argv[1]
print cascPath
#cap = cv2.VideoCapture(0)
#ramp_frames = 30
faceCascade = cv2.CascadeClassifier(cascPath)
if os.path.exists("/Users/oliverspall/little_less/crops") == False:
	print os.path.exists("/Users/oliverspall/little_less/crops/")
	dirname = 'crops'
	os.mkdir(dirname)
else:
	dirname = 'crops'

##here's some database setup stuff:
DBD = DB_Manager.DatabaseFunctions(settings_DB.databasename)
databasefile = settings_DB.databasename
db = sqlite3.connect(databasefile)
cursor = db.cursor()
  
def databasestart():

    dbstruct = {
        'Found_faces':{
            'face_id':'INTEGER',
            'file_location':'TEXT unique',                
            'timestamp':'INTEGER',
            'autotimestamp':'DATETIME DEFAULT CURRENT_TIMESTAMP',
            'filename':'TEXT',
            'status':'SMALLINT unsigned not null',
        }
    }

    # Initialise the database and build it if it doesn't exist
    builder = DatabaseBuilder(databasefile, dbstruct)
    print(builder.msg)  

    # Connect to the database


	    #need to do something here that will import (once) the elvis data and images.

	

#what this does is it sets where the script will look for a camera source. As most machines
##only have 1 camera, you usually need to pass either 0 or 1. If you want to use a file
##you can specify the source here. it also discards 30 frames to allow for the webcam to adjust
##

##Using threading to make sure that we can run multiple processes simultaneously. Think this will be /
##Necessary with the webserver.
# def startthreads():
# 	threading.Thread(target=face_rec).start()
# 	#threading.Thread(target=check_new_faces).start()

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
		##rolling = True
		##while rolling:
		timestamp = str(datetime.datetime.now())
		#rolling, image = cap.read()
		image = cv2.imread("/Users/oliverspall/little_less/crops/testing_image.jpg",0)
		cv2.imshow("/Users/oliverspall/little_less/crops/testing_image.jpg",0)
		# gray = image
		# #cv2.imshow(image, gray)
		# # Detect faces in the image using the OpenCV XML facial recognition cascade.
		# faces = faceCascade.detectMultiScale(
		#     gray,
		#     scaleFactor=1.1,
		#     minNeighbors=5,
		#     minSize=(30, 30),
		#     flags = cv2.cv.CV_HAAR_SCALE_IMAGE
		# )
		# print "Found {0} faces".format(len(faces))
#this part below prints a square onto the image where faces have been recognised.
		# for (x, y, w, h) in faces:
		# 	print (x, y, w, h)
		# 	cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
		# 	#cv2.imshow("Faces found", image)
		# 	#crop_rectangle = cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
		cv2.imwrite(os.path.join(dirname, ("thisisatest_"+timestamp+".jpg")),image)
		unique_id = timestamp
		print "saving image"
		cv2.imshow("Faces found", image)
		#below for database stuff:
		file_path = (os.path.join(dirname, ("Elvis_"+timestamp+".jpg")))
		filename = str("Elvis_"+timestamp)
		print file_path
		print filename
		status = settings_DB.NEW
		print status
		#face_id, image_loc, timestamp, filename, status) VALUES(?,?,?,?)', values
		DBD.insert_value(timestamp, file_path, timestamp, filename, status)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	time.sleep(1)
	print "waiting for 1 second"
	#print "saving images"

#here's just a bit of control:

#def get_new_images():


	#this final section just stops the process when finished:
	cap.release()
	cv2.destroyAllWindows()

# def check_new_faces(faces):
# 	#identify whether there are new images


# def compare_new_faces():
# 	#make a list of new faces recognized
# 	new_images = [settings_DB.settings.get_new_images(self,image_id,status)]
# 	for image in new_images:
# 		#run the elvis action on the images
# 		#update the elvis table with matching images
# 		#update with match %
# 		#update with the elvis ID
# 		#update shown_status
# 		#update the image table status



# def analyse_manipulate_image():
# 	#this should ideally do the analysis & parse image information based on % probability

# def web stuff()
if __name__ == '__main__':
	databasestart()
	face_rec()
	# while True:
	# 	startthreads()

