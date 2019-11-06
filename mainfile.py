import cv2
import os
import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
count = 0
for path, subdirnames, filenames in os.walk("trainingImages"):
    for filename in filenames:
        if filename.startswith("."):
            print("Skipping File:", filename)  # Skipping files that startwith .
            continue
        img_path = os.path.join(path, filename)  # fetching image path
        print("img_path", img_path)
        img = cv2.imread(img_path)
        array=np.array([])
        array_set=np.array([],dtype=int)
        datalist=list()
        dob_list=list()
        name_list=list()
        name_list=filename.split(".")
        datalist=name_list[0].split("_")
        print(datalist)
        dob_list=datalist[1].split("M" or "m")
        print(dob_list)
        if img is None:
            print("Image not loaded properly")
            continue
        image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(image, (64, 64))
        print(resized_image.shape)
        result = np.array(image).flatten()
        result_array=np.append(array,[result.astype(np.float),datalist[0],dob_list[0],dob_list[1]])
        print(result_array)
        array_set=np.append(array,[result.astype(np.float),(float)(count)])
        with open("data.csv", "a") as datafile:
            writer = csv.writer(datafile)
            writer.writerow(result_array)
        with open("data_one.csv","a") as datafile1:
            writer=csv.writer(datafile1)
            writer.writerow(array_set)
        new_path = "resized"
        print("Desired path is",os.path.join(new_path, "frame%d.jpg" % count))
        cv2.imwrite(os.path.join(new_path, "frame%d.jpg" % count), resized_image)
        count += 1


