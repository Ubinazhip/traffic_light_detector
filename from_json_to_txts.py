import yaml
import os
from tqdm import tqdm
#for yolo
with open("mmdetection/label_files/train.yaml") as stream:
    data = yaml.safe_load(stream)

print(data[0])
classes = {"Green": 1, "Red": 0, "Yellow":2, "off": 3}

for i in tqdm(range(len(data))):
    filename = os.path.join("gt_labels", data[i]["path"].split("/")[-1].split(".")[0] + ".txt")

    with open(filename, "w") as f:
        for box in data[i]["boxes"]:
            label = box["label"]
            if label not in classes:
                break
            f.write(str(classes[label]) + " ")
            x_center = (box["x_min"] + box["x_max"])/2 - 1
            y_center = (box["y_min"] + box["y_max"])/2 - 1
            f.write(str(x_center/1280) + " ")
            f.write(str(y_center/720) + " ")
            f.write(str((box["x_max"] - box["x_min"])/1280) + " ")
            f.write(str((box["y_max"] - box["y_min"])/720) + "\n")
