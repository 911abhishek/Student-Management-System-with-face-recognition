import os
import mysql.connector
import cv2

from attendace_maker import attendance_marker

class face_recog:
    def __init__(self):
        #no need for creatinng a another window using im showcommand inside the function
        # self.root = Tk()
        # self.root.title("Face Recognition")
        # self.root.geometry("500x500")
        self.cam = cv2.VideoCapture(0)#open the primary camera

        self.face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.recognizer = cv2.face.LBPHFaceRecognizer.create()
        self.recognizer.read("model.xml")

        self.face_recognition()
        

    def face_recognition(self):
     
        while True:
            ret, img = self.cam.read()#ret in this is a boolean value that has true or false it indicates the frame was read successfully and image is the
            #img = actual image frame read fror the camera
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(100,100))
            #the perimeters used are for controlling the process of face detection
            
            
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0),2)
                
                id, confidence = self.recognizer.predict(gray[y:y+h, x:x+w])
                if confidence < 79:
                    cv2.putText(img, "Attendance Marked for ID : "+str(id),(x+25, y+h-5),cv2.FONT_HERSHEY_SIMPLEX , 0.5, (255,255,255),2)
                    attendance_marker(id)
                else:
                    cv2.putText(img, "Unknown", (x+25,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0),2)
            cv2.imshow("Face Recognition", img)
                
            if cv2.waitKey(1) == 13:                    
                break
        self.cam.release()
        cv2.destroyAllWindows()

    






if __name__ == "__main__":
    
    facewin = face_recog()
    
    
    
    

