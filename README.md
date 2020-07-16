# cookbookCV
Instantly, find recipes using certain foods you want to get rid of, right from the comfort of your phone camera.

## Run Server
Run the file **server.py**

## YOLO
Type: Class

### How to Use 
- Download yolov3.weights 
  - Housing Link: https://pjreddie.com/darknet/yolo/
  - Direct Download: https://pjreddie.com/media/files/yolov3.weights

### How to Add to Your Code
```
from yolo import YOLO

PATHNAME = "" # Add image path
objects = YOLO().main(PATHNAME)
print(objects)
```

### Details
Currently using COCO dataset; next step is to use a custom dataset