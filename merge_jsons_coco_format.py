import json
import os
import sys
import pickle
# Define the directory containing JSON files
json_directory = "./sample_json/"


class ProgressFile:
    def __init__(self, file, callback=None):
        self.file = file
        self.callback = callback
        self.bytes_written = 0

    def write(self, data):
        self.bytes_written += len(data)
        if self.callback:
            self.callback(self.bytes_written)
        self.file.write(data)

    def __getattr__(self, attr):
        return getattr(self.file, attr)

# Example callback function
def progress_callback(bytes_written):
    print(f"Bytes written: {bytes_written}")

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
ann_counter = 1
for filename in os.listdir(json_directory):
    if filename.endswith(".json"):
        with open(os.path.join(json_directory, filename), "r") as json_file:
            data = json.load(json_file)
            data["image"]["id"] = data["image"]["image_id"]
            combined_data["images"].append(data["image"])
            for anno in data["annotations"]:
                anno["image_id"] = data["image"]["image_id"]
                anno["category_id"] = 1
                anno["iscrowd"] = 0
                anno["id"] = ann_counter
                ann_counter += 1
                combined_data["annotations"].append(anno)


    total_files = total_files - 1
    print("Remaining files:", total_files)
    combined_data["categories"].append(category)

# Define the output JSON file path
output_json_path = "val_sam_set.json"

dict_size_bytes = sys.getsizeof(pickle.dumps(combined_data, protocol=pickle.HIGHEST_PROTOCOL))

# Convert bytes to gigabytes
dict_size_gb = dict_size_bytes / (1024 ** 3)
print(f"Estimated dictionary size: {dict_size_gb:.6f} GB")

# Write the combined data to the output JSON file
with open(output_json_path, "w") as output_json_file:
    progress_file = ProgressFile(output_json_file, callback=progress_callback)
    json.dump(combined_data, output_json_file, indent=4)

