import json
import glob
from tqdm import tqdm
from matplotlib import pyplot as plt
import os

#red -> green -> yellow -> off
#convert our annotated images to suitable format
state = {2818929:1, 2818931:0, 2818935:2, 2821659:3} #2818929 green, 2818931 red, 2818935 yellow, 2821659 unknown

#json_files = glob.glob('/Users/alisakugusheva/Desktop/HSE/Tips/mmdetection/val_data/*/*/*.json')
json_files = glob.glob("/home/aslan/Documents/val_data/*/*/*.json")

data = {}
traffic_id = 0

for frame_id, json_file in tqdm(enumerate(json_files)):
    with open(json_file) as f:
        frame_data = json.load(f)
    filename = os.path.join("gt_labels", json_file.split("/")[-1].split(".")[0] + ".txt")

    with open(filename, "w") as f:
        for i in range(len(frame_data["objects"])):
            label = state[frame_data["objects"][i]["classId"]]
            f.write(str(label) + " ")
            bbox = frame_data["objects"][i]["points"]["exterior"]
            x_center = (bbox[0][0] + bbox[1][0])/2 - 1
            y_center = (bbox[0][1] + bbox[1][1])/2 - 1
            f.write(str(x_center/frame_data["size"]["width"]) + " ")
            f.write(str(y_center/frame_data["size"]["height"]) + " ")
            f.write(str((bbox[1][0] - bbox[0][0])/frame_data["size"]["width"]) + " ")
            f.write(str((bbox[1][1] - bbox[0][1])/frame_data["size"]["height"]) + "\n")
