import cv2
import numpy as np
import os
from dotenv import load_dotenv




# face_classifier = cv2.CascadeClassifier(face_model)
face_classifier = cv2.CascadeClassifier(r"Models/face.xml")
# face_database_path=os.environ['face_database_path']


def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return None
    for(x, y, w, h) in faces:
        cropped_faces = img[y:y+h, x:x+w]
    return cropped_faces


cap = cv2.VideoCapture(0)
count = 0

names = input("Enter Name of the person \n")
while True:
    ret, frame = cap.read()
    '''Extract face , convert to grayscale and save it in out folders'''
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (200, 200))
#         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        face = cv2.cvtColor(face, cv2.COLOR_RGB2BGR)
#         file_name_path=r'./Dataset_Openvino/train/Atharva/'+str(count)+'.jpg'

        file_name_path = os.path.join('Face Database', f"{names}-{count}.jpg")
        
        file_name_path = os.path.abspath(os.path.join("Face Database", f"{names}-{count}.jpg" ))

        cv2.imwrite(file_name_path, face)
        cv2.putText(face, str(count), (50, 50),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Face Cropper', face)
    else:
        print("Face not found")
        pass
    if cv2.waitKey(1) == 13 or count == 50:
        break
cap.release()
cv2.destroyAllWindows()
print("Collecting Samples Complete!!")