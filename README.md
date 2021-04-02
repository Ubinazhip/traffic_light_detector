# Traffic light detector
We used Bosch Small Traffic Lights Dataset to train YOLOv3-tiny and for transfer learning we took the darknet53 model pre-trained on VOCdata. YOLO is fast enogh, so it'a good option for real time image recognition. Another good thing is that it supports well known datasets, in particular, Pascal VOC. Bosch Small Traffic Lights Dataset is coming with a Python script which turns the dataset into Pascal-VOC like dataset.
In the configuration folder there are some scripts in which we changed the numbers of classes to 4, the labels to those provided in the task since the original files had 8 different classes and paths to the data. We have also changed the number of filters to 27 according to the formula: filters=(classes + coords + 1)* number of mask, where mask is indices of anchors. Then we implemented the trained net to provided dataset. We trained the net on 140,000 images but used weights for only 100,000. The result wasn’tgood enough due to overfitting to the train data, inability to classify some unseen traffic lights and misdetection of some objects as traffic lights.

[![Video1](https://img.youtube.com/vi/NlfFXHBdoLU/0.jpg)](https://www.youtube.com/watch?v=NlfFXHBdoLU)
[![Video2](https://img.youtube.com/vi/UPnKbZqYpZM/0.jpg)](https://www.youtube.com/watch?v=UPnKbZqYpZM)

The second approach was to use a popular framework (mmdetection). MMDetection is an open source object detection toolbox based on PyTorch. We have decided to use it because of its very good documentation and easiness in use. The main document we will be using is a config file, where you basically set parameters of your model as well as parameters of training and testing pipeline. We have trained there 2 models: one just for 1000 images (frames from videos,which were provided by the lecturer) and one for the bosch dataset + around 800 images of that 1000 images. However, we had problems with speed in inference - we were able to reach maximum of 25 FPS using Tesla v100 GPU which is not enough. The problem was that the docker didn’t utilize all GPU (only 8-9%) and we couldn’t fix it.

forked from: 
https://github.com/ultralytics/yolov3 
https://github.com/abewley/sort
