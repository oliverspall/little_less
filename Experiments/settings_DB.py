#.......................INTRODUCTION.........................................................................
#Many thanks to Tom Keene for introducing me to SQLite. 
#It makes building databases much easier.
#
#.......................What is this script?.................................................................
#This script defines the schema and functions of the database for the project "A little less condensation" //
#Along with a few other bits and pieces to keep the video_frames_n_n.py script running.//
#
#.......................Dependencies.........................................................................
#Dependencies are:
#DatabaseBuilder.py
#video_frames_n_n.py
#sqlite3 (this is included in Python 2.x)
#More broadly, you will need to build OpenCV2.4.x or 3. This takes time so book a day off.
#
#........................More information....................................................................
# (tom's notes) Place this script in the same directory as your script and use the following code:
#
#The aim of this database is to collect cropped images from the facial recognition work in the main script, //
#categorise them and parse them to a level where they can then be analysed for signs of Elvis. //
#The two tables contain information about the original images (Found_faces) and the analysed images (Elvis_impersonators) //
#We will be able to make decisions on things like:
#If there's an Elvis match with the photograph of the clouds
#How accurate the match is (in % probability)
#If the image has been identified before, and whether it will be shown on a website.
#
#Based on the results of analysis, we will then be able to develop an image manipulation that redefines Elvis, perhaps.

# .....................Tom's Notes ......................................
# Is this script being run directly i.e pyhton ./databasebuilder.py
 
# Example showing how to to use this class. Run: python2 ./database.py
#........................................................................
  

from DatabaseBuilder import DatabaseBuilder
import sqlite3
#
#Here are status settings for the images that we capture so we know which ones are new, which ones have been analysed and //
#which ones match / don't match.

NEW = 0
EXISTING = 1
ANALYSED = 2
MATCH = 3
NONMATCH = 4

class settings: 

    def db_connect():

        dbstruct = {
            'Found_faces':{
                'face_id':'SMALLINT not null AUTO_INCREMENT',
                'file_location':'TEXT unique',                
                'timestamp':'INTEGER',
                'autotimestamp':'DATETIME DEFAULT CURRENT_TIMESTAMP',
                'filename':'TEXT',
                'status':'SMALLINT unsigned not null',
            },
            'Elvis_impersonators':{
                'Elvis_id':'SMALLINT not null AUTO_INCREMENT',
                'Elvis_filename':'TEXT unique',
                'Image_details':'TEXT unique',
                'match_face_id':'SMALLINT not null AUTO_INCREMENT',
                'image_location':'TEXT unique',    
                'elvis_location':'TEXT unique',                
                'likeness':'INTEGER',
                'autotimestamp':'DATETIME DEFAULT CURRENT_TIMESTAMP',
                'shown_status': 'SMALLINT unsigned not null',
            }
        }
        
        # Initialise the database and build it if it doesn't exist
        databasefile = "Faces"
        builder = DatabaseBuilder(databasefile, dbstruct)
        print(builder.msg)  

        # Connect to the database
        db = sqlite3.connect(databasefile)
        cursor = db.cursor()

        #need to do something here that will import (once) the elvis data and images.

    def insert_value(
                self,
                face_id,
                image_loc,
                timestamp,
                filename,
                status,
                ):
        #values = (1234, 1, "/home/imiant/Desktop/still_1", "still_1")
        cursor.execute('INSERT INTO Found_faces(face_id, image_loc, timestamp, filename, status) VALUES(?,?,?,?)', values)
        db.commit()

    def select_entry():
        cursor.execute("SELECT timestamp, title, lat, lon FROM Found_faces")
        rows = cursor.fetchall()
        for row in rows:
            print('timestamp:{} title:{} lat:{} lon:{}'.format(row[0], row[1], row[2], row[3]))
        
    def update_entry():
        cursor.execute("UPDATE Found_faces SET timestamp=1 WHERE timestamp=1234")
        db.commit()

    def analyse_image():
        print('-----')
        cursor.execute("SELECT timestamp, title, lat, lon FROM table1")
        rows = cursor.fetchall()
        for row in rows:
            print('timestamp:{} title:{} lat:{} lon:{}'.format(row[0], row[1], row[2], row[3]))