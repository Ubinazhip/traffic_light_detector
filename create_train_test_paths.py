import glob
import os

#imgs = glob.glob('/Users/alisakugusheva/docker/dataset/images/*')
imgs = glob.glob('/home/aslan/docker/dataset/images/*')

with open("train.txt", "w") as f1:
    with open("test.txt", "w") as f2:
        for img in imgs:
            if ("video4" not in img) and ("video5" not in img):
		#f1.write(os.path.join('/Users/alisakugusheva/docker/dataset/images', img.split('/')[-1]) + '\n')
                f1.write(os.path.join("/home/aslan/docker/dataset/images", img.split("/")[-1]) + "\n")
            else:
		#f2.write(os.path.join('/Users/alisakugusheva/docker/dataset/images', img.split('/')[-1]) + '\n')
                f2.write(os.path.join("/home/aslan/docker/dataset/images", img.split("/")[-1]) + "\n")
