import json
import os
import sys
import pickle
from pycocotools import mask as mask_utils
import matplotlib.pyplot as plt
import cv2
import numpy as np
from itertools import groupby
# Define the directory containing JSON files
json_directory = "./sample_json/"


def binary_mask_to_rle(binary_mask):
    rle = {'counts': [], 'size': list(binary_mask.shape)}
    counts = rle.get('counts')
    for i, (value, elements) in enumerate(groupby(binary_mask.ravel(order='F'))):
        if i == 0 and value == 1:
            counts.append(0)
        counts.append(len(list(elements)))
    return rle


def is_bbox_valid(bbox, image_width, image_height):
    x, y, w, h = bbox

    # Check if all values are positive
    if x < 0 or y < 0 or w <= 0 or h <= 0:
        return False

    # Check if the bounding box is within the image dimensions
    if x + w > image_width or y + h > image_height:
        return False

    return True
# Example callback function
def progress_callback(bytes_written):
    print(f"Bytes written: {bytes_written}")

# Initialize the COCO annotation dictionary
coco_annotation = {
    "info": {
        "description": "Object detection annotations in COCO format",
        "version": "1.0",
        "year": 2023,
        "date_created": "2023-06-26"
    },
    "licenses": [],
    "images": [],
    "annotations": [],
    "categories": []
}

# Define the category
category = {
    "id": 1,
    "name": "tower",
    "supercategory": "tower"
}
coco_annotation["categories"].append(category)
total_files = len(os.listdir(json_directory))
ann_counter = 0
for filename in os.listdir(json_directory):
    if filename.endswith(".json"):
        with open(os.path.join(json_directory, filename), "r") as json_file:
            data = json.load(json_file)


        image_entry = {
        "id": data["image"]["image_id"],
        "file_name": data["image"]["file_name"],
        "height": data["image"]["height"],
        "width": data["image"]["width"]
        }
        coco_annotation["images"].append(image_entry)
        im_name = json_directory + data["image"]["file_name"]
        im = cv2.imread(im_name)
        print("total anos", len(data["annotations"]))
        for counter,anno in enumerate(data["annotations"]):

            #mask = mask_utils.decode(anno["segmentation"])
            x, y, w, h = np.array(anno["bbox"]).astype(np.int32)

            #rle_mask = binary_mask_to_rle(mask)
            annotation_entry = {
            "id": ann_counter,
            "image_id": data["image"]["image_id"],
            "category_id": category["id"],
            "bbox": anno["bbox"],
            "area": anno["area"],
            "segmentation": anno["segmentation"],
            "iscrowd": 0
            }
            coco_annotation["annotations"].append(annotation_entry)
            ann_counter += 1
                    
                #cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0))


            #combined_data["annotations"].extend(data["annotations"])

    total_files = total_files - 1
    print("Remaining files:", total_files)


# Define the output JSON file path
output_json_path = "val_json2.json"


# Write the combined data to the output JSON file
with open(output_json_path, "w") as output_json_file:
    json.dump(coco_annotation, output_json_file)

