import cv2
import time
import numpy as np
cap = cv2.VideoCapture("carDetection/video.mp4")
cascade = cv2.CascadeClassifier("carDetection/car.xml")



while True:
    ret , frame =cap.read()
    car_rect = cascade.detectMultiScale(frame , 1.095 , 2)
    if ret:
        gray = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)
        for x,y,w,h in car_rect:
            cv2.rectangle(gray, (x,y), (x+w , y+h), (255,255,255), 2)
            cv2.imshow("deneme", gray)
        time.sleep(0.019)

    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()
