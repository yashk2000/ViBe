# ViBe
This repository contains my implementation of the [ViBe algorithm](http://orbi.ulg.ac.be/bitstream/2268/145853/1/Barnich2011ViBe.pdf).

The algorithm here has been implemented using OpenCV and Python.

To run the script, copy the `test.avi` video from Test Data into the same folder as the `vibe.py` script. If you run the script on your own video, you might have to change the values or `N, R, hashMin, or phi`. 
Best results are obtained on the following values:

- N = 20
- R = 20
- hashMin = 2
- phi = 16

Tweaking these values might be needed to obtain best results.
