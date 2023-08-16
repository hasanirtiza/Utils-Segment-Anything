# Utils-Segment-Anything
Some utility functions to download [SAM-1b dataset](https://ai.meta.com/datasets/segment-anything/) from Meta.

Please visit the site, signup, read terms and conditions and do appropriate actions. 
Download the whole dataset or part of it by running dataset_downlaod.sh (shell script). It goes through the .txt file and download each set. 

Visit the [following site](https://scontent-hel3-1.xx.fbcdn.net/m1/v/t6/An8MNcSV8eixKBYJ2kyw6sfPh-J9U4tH2BV7uPzibNa0pu4uHi6fyXdlbADVO4nfvsWpTwR8B0usCARHTz33cBQNrC0kWZsD1MbBWjw.txt?ccb=10-5&oh=00_AfDGdz5szNbn8HihwL-bhVXl4hFgd4SzCswurBA55akwbw&oe=65015CD8&_nc_sid=0fdd51) and download this [txt file](https://scontent-hel3-1.xx.fbcdn.net/m1/v/t6/An8MNcSV8eixKBYJ2kyw6sfPh-J9U4tH2BV7uPzibNa0pu4uHi6fyXdlbADVO4nfvsWpTwR8B0usCARHTz33cBQNrC0kWZsD1MbBWjw.txt?ccb=10-5&oh=00_AfDGdz5szNbn8HihwL-bhVXl4hFgd4SzCswurBA55akwbw&oe=65015CD8&_nc_sid=0fdd51). Then place annotations (.json format) into a single folder called annotations and run merge_jsons_coco_format.py. This willl combine all jsons in COCO format.


If you use SAM 1b please cite respective sources.
