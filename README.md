# Real-Time-Face-Detection
This post will demonstrate Real time face detection with the YOLO system using a re-trained model. This project was trained on my personal face dataset , which contain more than 2500 pictures of my face in diffrent position . This project also contain a graphic user interface that give you 2 options : detect Mahdi " me " , Or detect all objects in video.
## Overview
[![Real Time Face Recognition](http://img.youtube.com/vi/UFYbAV8svr8/0.jpg)](http://www.youtube.com/watch?v=UFYbAV8svr8 "Real Time Face Recognition")
## Dependencies

* PyQt5
* Subprocess
* Shlex
* Opencv
* Darknet

## Usage

In order to test the " Detect Mahdi " Function you need to download the retrained weights and cfg files:
* obj.data 
* obj.cfg and put it in "cfg file"
* obj_3000.weight 

In order to test the " Detect all " Function you need to download:
* coco.data and put it in "cfg file"
* yolov3-tiny.cfg and put it in "cfg file"
* yolov3-tiny.weights 

