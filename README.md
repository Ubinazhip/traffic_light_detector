# commands 
The main files are inside yolov3 folders and see the text file commands to run the program. Also see the pdf file: traffic_light_detection.pdf
# Traffic light detector
Task: Real time traffic light detection. Save the results in json file. Format: <br />

frame_id”: [ <br />
      “traffic_light_id”: { <br /> 
                  “coords”: [x1, y1, x2, y2], <br />
                          “state”: “red|yellow|green”, <br />                        
                           affect”: true|false }

# Dataset 
We used [bosch small traffic lights dataset](https://hci.iwr.uni-heidelberg.de/content/bosch-small-traffic-lights-dataset) train dataset + yellow traffic lights from test set(there was class disblance). Moreover, we have decided to annote the frames(every 20's frame) of the videos, that the lecturer provived us.  <br />
see the [annotations](https://drive.google.com/drive/folders/1g5q8Ucv6siXylpvj9UIL0m-M4QLSI0JF?usp=sharing). We have used frames of 2 videos for validation 
<br />

forked from: <br />
https://github.com/ultralytics/yolov3 <br> 
https://github.com/abewley/sort
