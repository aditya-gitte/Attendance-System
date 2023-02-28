import cv2
import os
import subprocess



class ROISaver:

    def __init__(self, ImageDirectory, imgpath, coordinatespath, base_counter):
        self.dic=ImageDirectory
        self.imgpath=imgpath
        self.coordinatespath=coordinatespath
        self.base_counter=base_counter

    def run(self):
        # Load the image
        image = cv2.imread(self.imgpath)

        # Open the text file in read mode
        boxes=[]
        with open(self.coordinatespath, 'r') as file:
            # Read all the lines of the file
            lines = file.readlines()
            for line in lines:
                words=line.split()
                wordsint=[]
                for word in words:
                    wordint=int(word)
                    wordsint.append(wordint)
                boxes.append(wordsint)

        # Iterate over the bounding boxes
        counter=0
        for box in boxes:
            counter=counter+1
            # Extract the bounding box from the image
            x1 = box[0] 
            y1 = box[1] 
            x2 = box[2] 
            y2 = box[3] 
            roi = image[y1:y2, x1:x2]
            np=os.path.join(self.dic,f'{self.base_counter}_box_{counter}.jpg')
            cv2.imwrite(np, roi)
            #Converting RGB to BGR
            img = cv2.imread(np)
            bgr_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            cv2.imwrite(np, bgr_img)
            
        
        print(f"[ INFO !! ] Added {counter} images to the input folders directory for the base {self.base_counter}")

    
    def databaseCrop(self):
        # Load the image
        image = cv2.imread(self.imgpath)

        # Open the text file in read mode
        boxes=[]
        with open(self.coordinatespath, 'r') as file:
            # Read all the lines of the file
            lines = file.readlines()
            for line in lines:
                words=line.split()
                wordsint=[]
                for word in words:
                    wordint=int(word)
                    wordsint.append(wordint)
                boxes.append(wordsint)

        # Iterate over the bounding boxes
        counter=0
        for box in boxes:
            counter=counter+1
            # Extract the bounding box from the image
            x1 = box[0] 
            y1 = box[1] 
            x2 = box[2] 
            y2 = box[3] 
            roi = image[y1:y2, x1:x2]
            # np=os.path.join(self.dic,f'box_{counter}.jpg')
            cv2.imwrite(self.imgpath, roi)




#testing
# if __name__ == "__main__":
#     obj=ROISaver("Input_Images","/Users/aditya_gitte/Downloads/grp1.jpg","/Users/aditya_gitte/Projects/Attendance-System/coordinates.txt")
#     obj.run()
            










