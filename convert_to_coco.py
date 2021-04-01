import json
import glob
from tqdm import tqdm
from matplotlib import pyplot as plt
import os
#for mmdetection
class_id_dict = {2818929:0, 2818931:1, 2818935:2, 2821659:3} #2818929 green, 2818931 red, 2818935 yellow, 2821659 unknown

#json_files = glob.glob('/Users/alisakugusheva/Desktop/HSE/Tips/mmdetection/val_data/*/*/*.json')
json_files = glob.glob("/home/aslan/Documents/mmdetection/val_data/*/*/*.json")

obj_count = 0

annotations = []
images = []
categories = [dict(id=0, name="green"), dict(id=1, name="red"), dict(id=2, name="yellow"), dict(id=3, name="unknown")]

for idx, json_file in tqdm(enumerate(json_files)):
    with open(json_file) as f:
        data = json.load(f)

    filename=json_file.split("/")[-1].split(".json")[0]

    images.append(dict(id=idx,
                       file_name=filename,
                       height=data["size"]["height"],
                       width=data["size"]["width"]))

    for i in range(len(data["objects"])):
        bbox_coords = data["objects"][i]["points"]["exterior"]

        annotations.append(dict(image_id=idx,
                                iscrowd=0,
                                id=obj_count,
                                category_id=class_id_dict[data["objects"][i]["classId"]],
                                bbox=[bbox_coords[0][0], bbox_coords[0][1], bbox_coords[1][0] - bbox_coords[0][0], bbox_coords[1][1] - bbox_coords[0][1]],
                                area=(bbox_coords[1][0] - bbox_coords[0][0])*(bbox_coords[1][1] - bbox_coords[0][1])))

        obj_count += 1

with open("val.json", "w") as write_file:
    json.dump(dict(images=images, annotations=annotations, categories=categories), write_file)
