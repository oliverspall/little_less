#.......................INTRODUCTION.........................................................................
#Many thanks to Tom Keene for introducing me to SQLite. 
#It makes building databases much easier.
#
#.......................What is this script?.................................................................
#This script defines the schema and functions of the database for the project "A little less condensation" //
#Along with a few other bits and pieces to keep the less_condensation_n_n.py script running.//
#
#.......................Dependencies.........................................................................
#Dependencies are:
#DatabaseBuilder.py
#less_condensation_n_n.py
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
  

from databasebuilder import DatabaseBuilder
import sqlite3
#
#Here are status settings for the images that we capture so we know which ones are new, which ones have been analysed and //
#which ones match / don't match.

NEW = 0
EXISTING = 1

databasename = "Faces"
DB = sqlite3.connect(databasename)






