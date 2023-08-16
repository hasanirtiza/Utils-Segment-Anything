import json
import os
import sys
import pickle
# Define the directory containing JSON files
json_directory = "./sample_json/"

# Define the output JSON file path
output_json_path = "combined_sample_data.json"

combined_data = {
    "images": [],
    "annotations": [],
     "categories": []
}
category = {
    "id": 1,
    "name": "object",
    "supercategory": "object"
}

total_files = len(os.listdir(json_directory))
for filename in os.listdir(json_directory):
    if filename.endswith(".json"):
        with open(os.path.join(json_directory, filename), "r") as json_file:
            data = json.load(json_file)
            data["image"]["id"] = data["image"]["image_id"]
            combined_data["images"].append(data["image"])
            for anno in data["annotations"]:
                anno["image_id"] = data["image"]["image_id"]
                anno["iscrowd"] = 0
                combined_data["annotations"].extend(data["annotations"])

    total_files = total_files - 1
    print("Remaining files:", total_files)
    combined_data["categories"].append(category)



dict_size_bytes = sys.getsizeof(pickle.dumps(combined_data, protocol=pickle.HIGHEST_PROTOCOL))

# Convert bytes to gigabytes
dict_size_gb = dict_size_bytes / (1024 ** 3)
print(f"Estimated dictionary size: {dict_size_gb:.6f} GB")

# Write the combined data to the output JSON file
with open(output_json_path, "w") as output_json_file:
    json.dump(combined_data, output_json_file)

