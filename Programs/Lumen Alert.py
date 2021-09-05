import requests
import cv2
import numpy as np
import imutils
from imutils.video import VideoStream
import argparse
import datetime
import time
import serial

url="http://192.168.43.1:8080/shot.jpg" #IP Webcam address, copied from application
arduino=serial.Serial('COM3',9600) #COM port for Arduino Serial communication, copied from Arduino IDE
pos=-1
ledtype={7:1,13:2,16:1,20:2,22:2}
# Format - Time(Hours(24h format): LED type
def main():
    firstFrame=None
    while True:
        flag=0
        lighttype=0
        date=time.localtime()#Result is the current time
        if date.tm_hour in ledtype :      #At alarm time
            lighttype=ledtype[date.tm_hour]*10+ledtype[date.tm_hour]
            img_resp = requests.get(url)
            img_arr = np.array(bytearray(img_resp.content),dtype=np.uint8)
            frame = cv2.imdecode(img_arr,-1)
            frame = imutils.resize(frame, width=1080,height=1920)
            if frame is None:
                break
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            gray=cv2.GaussianBlur(gray,(21,21),0)
            if firstFrame is None:
                firstFrame=gray
                continue
            frameDelta=cv2.absdiff(firstFrame,gray)
            thresh=cv2.threshold(frameDelta,35,255,cv2.THRESH_BINARY)[1]
            thresh=cv2.dilate(thresh,None,iterations=2)
            cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            cnts=imutils.grab_contours(cnts)
            for c in cnts:
                if cv2.contourArea(c)< 20000:
                    continue
                (x,y,w,h)=cv2.boundingRect(c)
                print("x:",x)
                if w>200 and h>200:     #Threshold for person's frame
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                    flag=1      #Person is present
                    pos= x+(w/2)
            cv2.imshow("Feed",frame)
            if cv2.waitKey(1) ==27:
                break
            
            if(flag):
                if(ledtype[date.tm_hour]==1):#Going on screen stops the wakelight
                    break
                angle=(int)((pos/1080)*130)
                data=(angle*100)+lighttype #Dataset format = 123 - Angle (000 to 180) 4 - LED Type (0-None, 1-White, 2-Red) 5 - Light type (0-Off, 1-Steady light, 2-Blinking)
                if data<10000:  #Angle less than 100 requires a 0 before the value so as to preserve dataset format
                    dataset='0'+str(data)+'\n'
                else:
                    dataset=str(data)+'\n'
                arduino.write(str.encode(dataset))
                time.sleep(0.5)
                print("dataset: ",dataset)
            else:
                if(ledtype[date.tm_hour]==1):
                    dataset='03011\n'
                else:
                    dataset='03000\n'
                arduino.write(str.encode(dataset))
                time.sleep(0.5)
    cv2.destroyAllWindows()
    dataset='03000\n'
    arduino.write(str.encode(dataset))
    time.sleep(0.5)

main()
