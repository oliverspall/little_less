 little_less

This is a repository for an MA Interactive Media, Critical Theory and Practice minor project at Goldsmiths, University of London.

The project is called: Little Less Condensation.

Little Less Condensation is a poorly-planned hack of computer vision software in order to train a machine to search for Elvis.

I have been searching for Elvis by looking upward, trying to find The King amongst cumulonimbus, stratus and cirrus clouds, mainly around the Lewisham area of London.

So far, I have not found The King.

________________________________________________________________________________________________________

The project runs primarily on software written with the OpenCV framework, working mainly in Python.

OpenCV can be accessed here: http://www.opencv.org

I would strongly advise you plan for a day to install, unless you want to do a basic install with a software installation package like Homebrew, where you can install very quickly, but with some compromise in configuration. 

Here's a link to a Homebrew tutorial: http://www.jeffreythompson.org/blog/2013/08/22/update-installing-opencv-on-mac-mountain-lion/ 

Other dependencies:

Numpy

If you want to run this and publish any results to the web:

Threading
Cherrypy
sqlite3

The facial recognition and detection sections of this project are still very much work in progress, but revolve around the following pieces of technology, defined as follows:

Eigenfaces: statistically-driven machine learning algorithms that 'learn' the characteristics of a face from a large number of example images of that person. This focuses on picking up the characteristics in multiple lighting, and perspectival ways to create a vector-driven 'model' of that person's face. To learn more about Eigenfaces, read here: http://docs.opencv.org/modules/contrib/doc/facerec/tutorial/facerec_video_recognition.html 

Haar Cascades: these are tree-like neural networks that allow for very fast processing of very disparate data. This breaks a large set of different faces down into component parts and then trains an algorithm to search for these parts in a given field. What's clever is that the technology uses a cascade process that ensures very efficient processing and high speed of recognition. More details here: http://docs.opencv.org/master/d7/d8b/tutorial_py_face_detection.html 



________________________________________________________________________________________________________

*******The project uses OpenCV features to do the following:******

- Read a camera attached to a computer via USB.

- Break that feed down into frames, then into grayscale and then into mats in order to calculate pixel values.

- Use OpenCV's built-in Haar Cascade facial detection software to look for faces

- Highlight when a face has been detected and outline it with a green square

- Save those frames with faces in them as unique files to a folder on your computer.

Future plans for this project are as follows:

- Build a database architecture for the project, allowing categorization, and storage of images with faces in them
- Host a website that will show these images.

________________________________________________________________________________________________________

******Detailed tutorial:*******

STEP 1:

Starting out, install OpenCV. Use the latest version of OpenCV2 which you can find here: http://opencv.org/downloads.html

If you are running on a mac, use the above tutorial.

If you are running a ubuntu / linux machine, then use this tutorial: http://docs.opencv.org/doc/tutorials/introduction/linux_install/linux_install.html 
and refer to this one: http://milq.github.io/install-opencv-ubuntu-debian/ 

Make sure you also have the latest version of python 2.x and numpy, which will help OpenCV do the math.


STEP 2:

Really, it's a matter of just getting started. There is excellent first steps documentation on the documentation section of OpenCV's website.
 
To continue the project that I have created, you can use the script video_frames_0_4.py to start with. 

This is the command line script you need to write: $ python video_frames_0_4.py <the address to your Haar Cascade> 

This borrows from the following Real Python tutorial which was very helpful in putting my thinking straight:

https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/
https://realpython.com/blog/python/face-recognition-with-python/ 

What you'll need from your install of OpenCV is the Haar Cascade that allows you to detect faces. This will be in the data section of your install.

STEP 3:

you now want to start to train your own Haar Cascade. I have included a repository in this project that has all the information you need to complete a Haar training, aside from the positive images.

Haar cascades work in the following way:

1) You start with a large amount of images of the thing you want to detect (banana, elvis, car, whatever)
2) You also create a large number of negative images that do not contain the thing you want to detect.
3) You create data files of both of these sets of images, with the positive image containing the 4 point coordinates of the thing you are searching for
4) You then use the OpenCV framework to create a vector file of these positive images, and train the cascade with the vector, and the datafile of the negative images.
5) You will at the end, eventually, have a Cascade that is trained to detect what you are looking for.

Note: This is not a quick process. It requires a LOT of trial and error, and also a huge number of images in order for it to work well. To get a cascade that had a relevant number of stages in it, it took me > 4 solid days on a macbook pro with 8GB of RAM and a 2.8GHz processor. Allow for significant amounts of time for this to work.


ESSENTIAL READING:

You will not get this right first time. I am a novice at programming and I did not get this right 10th time, or 50th time. Look at the command line transcript if you want to have a look at how much time this took.

Here are some essential things for you to read before you start:

Official documentation: http://docs.opencv.org/doc/user_guide/ug_traincascade.html

Naotoshi Seo's very famous (but flawed) tutorial. Read this for context, try out the tutorial, but it didn't work for me as the perl script is outdated. http://note.sonots.com/SciSoftware/haartraining.html 

A useful film for Windows: https://www.youtube.com/watch?v=WEzm7L5zoZE

Another useful film for Ubuntu: https://www.youtube.com/watch?v=WEzm7L5zoZE

when you have finished / given up, all you need to do is replace the OpenCV supplied cascade with cascade you have trained as the argument in your command line prompt.


And that's about it.

Good luck.'

Please help me evolve this project too. Any help is much appreciated.
