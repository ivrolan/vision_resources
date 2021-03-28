import os
import sys
import json
import numpy as np
import cv2
import base64
import labelme

def getJsonTemplate():

    labelme_file_template = {

        "version" : "4.5.7",
        "flags" : {},
        "shapes": [{
            "label" : "test",
            "points" : [
                [
                1,
                2
                ],
                [3,4]
            ],
        "group_id" : None,
        "shape_type" : "polygon",
        "flags" : {}
        
        }],
        "imagePath" : "blabla.jpg",
        "imageData" : "encoded"

    }

    return labelme_file_template

def getCountourPoints(filename, mask_filename):
    #print("mask:", mask_filename)
    img = cv2.imread(mask_filename, cv2.IMREAD_GRAYSCALE)
    _, threshold_not = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
    threshold = cv2.bitwise_not(threshold_not)
    # Detecting contours in image.
    contours, _= cv2.findContours(threshold, cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_NONE)
    
    max_len = 0
    max_cnt = None
    # Going through every contours found in the image.
    for cnt in contours :
        #print("###############################")
        #print(cnt)
        #approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

        #print(len(cnt))
        if len(cnt) > max_len:
            max_cnt = cnt
            max_len = len(cnt)
    points_list = []
    for i in max_cnt:
        for coords in i:
            x = float(coords[0])
            y = float(coords[1])
            points_list.append([x, y])
    #print(points_list)
    return points_list

def main():
    
    if len(sys.argv) != 3:
        print("2 parameters needed. [path] [label_name]")
        return

    img_type = ".jpg"
    os.chdir(sys.argv[1])
    for f in os.listdir("."):
        
        if f.endswith(img_type):
            img = f[:f.find(img_type)]
            labelme_json = getJsonTemplate()
            labelme_json["label"] = str(sys.argv[2])
            labelme_json["imagePath"] = img + ".jpg"
            #labelme_json["imageData"] = str(base64.b64encode(open(img + ".jpg", "rb").read().decode('utf-8')))
            data = labelme.LabelFile.load_image_file(img + ".jpg")
            labelme_json["imageData"] = base64.b64encode(data).decode('utf-8')
            labelme_json["shapes"][0]["points"] = getCountourPoints(img + ".jpg", "masks/" + img + "_mask.pbm")

            #print(json.dumps(labelme_json, indent=4))
            
            
            f= open(img + ".json","w")

            f.write(str(json.dumps(labelme_json, indent=4)))

            print(img, "done")
    
if __name__ == "__main__":
    main()