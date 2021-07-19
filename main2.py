import cv2
import numpy, random

cars = 0

cap = cv2.VideoCapture("source\DRONE-SURVEILLANCE-CONTEST-VIDEO.mp4")

def updateIndices(cars, img):
    cv2.putText(img, "K M Risvanth", (400, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255))
    cv2.putText(img, cars, (750, 50), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0,0,255))

def detectColours(img, imgToDraw):
    global cars

    height, width = img.shape[0:2]

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 650:
            peri = cv2.arcLength(cnt, True)

            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)

            x,y,w,h = cv2.boundingRect(approx)
                
            carComplete=int(y+h/2)
            complete=height-250
            
            if(carComplete<complete+5 and carComplete>complete-5):
                
                cars=cars+1

                cv2.putText(imgToDraw, str(random.randint(0, 1000)), (x+w-10, y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

                cv2.rectangle(imgToDraw, (x,y), (x+w, y+h), (0,0,255),2)
        
while True:
    i, img = cap.read()
    img = cv2.resize(img, (860, 560))

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)

    detectColours(imgCanny, img)
    updateIndices(str(cars), img)

    cv2.imshow("", img)

    if cv2.waitKey(1) == 27:
        break

































