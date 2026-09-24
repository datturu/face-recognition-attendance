import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
import os 
import smtplib

# Credentials come from environment variables, never hardcode them:
#   ATTENDANCE_EMAIL, ATTENDANCE_EMAIL_PASSWORD (Gmail app password), ATTENDANCE_REPORT_TO

email=smtplib.SMTP('smtp.gmail.com',587)
email.starttls()
email.login(os.environ['ATTENDANCE_EMAIL'], os.environ['ATTENDANCE_EMAIL_PASSWORD'])
subject="Presenties and Absenties of final year"

stop="Mon June 02 08:20:50 2021"

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = "data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'user1', 'user2', 'user3', 'user4', 'user5'] 
pre=['0','0','0','0','0']
abse=['user1','user2','user3','user4','user5']
g=0
l=0
# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

i=0
count=1
while True:
    ret, img =cam.read()
    #img = cv2.flip(img, -1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])


        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 70):
            id = names[id]
            
            confidence = "  {0}%".format(round(100 - confidence))
            if(count == 1):
                        print('face id:',str(id),' present')
                        for i in range(5):
                            if pre[i]!=str(id):
                              l=1
                        if l==1:
                            pre[g]=str(id)
                            abse.remove(str(id))
                            g=g+1
                            l=0
                        count =2
                        i=0
                                    
        else:
            id = "unknown"
            print('no face detected')
            confidence = "  {0}%".format(round(100 - confidence))
            time.sleep(0.1)

            
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img)
    i= i+1
    #print('i: ',int(i))
    if(i == 100):
        #print('i: ',int(i))
        count=1
        i=0

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if time.asctime()>=stop or k == 27:
        print("Presents:",pre)
        print("Absenties:",abse)
        text="Presenties:{}\nAbsenties:{}".format(pre,abse)
        message="subject:{}\n\n{}".format(subject,text)
        email.sendmail(os.environ['ATTENDANCE_EMAIL'], os.environ['ATTENDANCE_REPORT_TO'], message)
        email.quit()
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
