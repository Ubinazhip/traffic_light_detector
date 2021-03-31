# traffic_light_detector
We used Bosch Small Traffic Lights Dataset to train YOLOv3-tiny with 220FPS and for transfer learning we took the darknet53 model pre-trained on VOCdata. Then manually changed the numbers of classes to 4, labels to those pro-vided in the task and the number of filters to 27. Then we implemented the trained net to provided dataset. The result wasn’tgood enough due to overfitting to the train data, inability to classify some un-seen traffic lights and misdetection some objects as traffic lights.

[![Video](https://img.youtube.com/vi/NlfFXHBdoLU/0.jpg)](https://www.youtube.com/watch?v=NlfFXHBdoLU)

The second approach was to use a popular framework (mmdetection). MMDe-tection is an open source object detection toolbox based on PyTorch. We havedecided to use it because of its very good documentation and easiness in use.The main document we will be using is a config file, where you basically set1
parameters of your model as well as parameters of training and testing pipeline.We have trained there 2 models: one just for 1000 images (frames from videos,which were provided by the lecturer) and one for the bosch dataset + around800 images of that 1000 images. However, we had problems with speed in infer-ence - we were able to reach maximum of 25 FPS using Tesla v100 GPU whichis not enough. The problem was that the docker didn’t utilize all GPU (only8-9%) and we couldn’t fix it.
