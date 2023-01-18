import cv2

frameWidth = 640
frameHeight= 480

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,130)

def takePicture():
    print("Hold for Picture")
    for i in range(0,120):
        cool,img = cap.read()
        imgResult = img.copy()
        cv2.imwrite("PeoplePhotos\Person.png",imgResult) # change in the future to allow for more than one photo (overwrites pervious files atm)
    print('Whoa! Check the File.')
