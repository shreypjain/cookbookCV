import cv2
import numpy as np 
import argparse
import time

class YOLO():
    def main(self, image_path):
        '''
        Input: String of image path
        Output: list of objects detected
        '''
        # image = input("Enter the directory of the image: ")
        self.image = image_path
        if self.image:
            imgs = (self.image_detect(self.image))
            # cv2.destroyAllWindows()
            return imgs
        return ["ERROR"]

    def load_yolo(self):
        '''
        Uses YOLO from the cv2 library; note that you will need the files downloaded locally
        '''
        net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        self.classes = []
        with open("coco.names", "r") as f:
            self.classes = [line.strip() for line in f.readlines()]

        layers_names = net.getLayerNames()
        output_layers = [layers_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(self.classes), 3))
        return net, self.classes, colors, output_layers


    def load_image(self, img_path):
        '''
        cv2 load image
        '''
        img = cv2.imread(img_path)
        img = cv2.resize(img, None, fx=0.4, fy=0.4)
        height, width, channels = img.shape
        return img, height, width, channels

    # def display_blob(self, blob):
    #     '''
    #     Shows the boxes around the images
    #     '''
    #     for b in blob:
    #         for n, imgb in enumerate(b):
    #             cv2.imshow(str(n), imgb)


    def detect_objects(self, img, net, outputLayers):
        '''
        Uses network to output matrix
        '''
        blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
        net.setInput(blob)
        outputs = net.forward(outputLayers)
        return blob, outputs


    def get_box_dimensions(self, outputs, height, width):
        '''
        Returns the classes and location
        '''
        boxes = []
        confs = []
        class_ids = []
        for output in outputs:
            for detect in output:
                scores = detect[5:]
                class_id = np.argmax(scores)
                conf = scores[class_id]
                if conf > 0.3:
                    center_x = int(detect[0] * width)
                    center_y = int(detect[1] * height)
                    w = int(detect[2] * width)
                    h = int(detect[3] * height)
                    x = int(center_x - w/2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confs.append(float(conf))
                    class_ids.append(class_id)
        return boxes, confs, class_ids


    # def draw_labels(self, boxes, confs, colors, class_ids, classes, img):
    #     indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
    #     font = cv2.FONT_HERSHEY_PLAIN
    #     for i in range(len(boxes)):
    #         if i in indexes:
    #             x, y, w, h = boxes[i]
    #             label = str(classes[class_ids[i]])
    #             color = colors[i]
    #             cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
    #             cv2.putText(img, label, (x, y - 5), font, 1, color, 1)
    #     cv2.imshow("Image", img)


    def image_detect(self, img_path):
        '''
        Runs all the other commands
        '''
        model, classes, colors, output_layers = self.load_yolo()
        image, height, width, channels = self.load_image(img_path)
        blob, outputs = self.detect_objects(image, model, output_layers)
        boxes, confs, class_ids = self.get_box_dimensions(outputs, height, width)
        return [classes[i] for i in class_ids]


print(YOLO().main("/Users/paromitadatta/Desktop/darknet/data/foods.jpg")) # INSERT IMAGE PATH
