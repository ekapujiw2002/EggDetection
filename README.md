# Egg Detection and Count

This project is used to detect and count eggs with the opencv library.

![Language](https://img.shields.io/pypi/pyversions/Django.svg)
[![License](http://img.shields.io/badge/license-MIT-lightgrey.svg?style=flat
)](http://mit-license.org)

  <img src="https://github.com/harunozdemir/EggDetection/blob/master/master/Screen%20Shot%202018-10-26%20at%2017.26.21.png" >
  
You can also adjust the radius and area from the settings page.


  <img src="https://github.com/harunozdemir/EggDetection/blob/master/master/Screen%20Shot%202018-10-26%20at%2017.26.54.png" height="500" >
  
## Description
  There are two blue and one green lines in the image. When the egg enters between two blue lines, the detection algorithm starts running.When the green line crosses, the number of eggs is increased by 1.
  
  **P.S**:
  I added a video file for testing. You can test it either through the video file or via the ip camera or via your webcam.
  
## Requirements
- Python 2.7.15+
- OpenCV 3.4.2+ 
- PyQt5 Library(GUI - for Setting page)
  
## Installation
  - Python(or from here [reference](https://www.python.org/downloads/)):
  ```bash
  $ brew install python3
  ```
  - OpenCV(or from here [reference](https://pypi.org/project/opencv-python/)):
  ```bash
  $ brew install opencv
  or
  $ pip3 install opencv-python  
  ```   
  - PyQt5(or from here [reference](http://pyqt.sourceforge.net/Docs/PyQt5/installation.html)):
  ```bash
  $ pip3 install pyqt5
  ```
## Feedback
Help / bug fix etc. Feel free to contact out via [Mail](mailto:harunozdmirr@gmail.com)

## Author
Harun Özdemir, harunozdmirr@gmail.com
