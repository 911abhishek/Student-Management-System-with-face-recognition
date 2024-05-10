import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import cv2
from tkinter import messagebox

class Train:
    def __init__(self, root):
        self.root = root
        # self.training_classifier()
        
      
    
        


    def training_classifier(self):
        data_dir = "facedata"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image_path in path:
            img = Image.open(image_path).convert('L')  # Convert image to grayscale
            img_np = np.array(img, 'uint8')
            # id = int(os.path.split(image_path).split('.')[0].split('_')[1])#user.1_2.jpg so extracting like this
            id = int(os.path.split(image_path)[-1].split('.')[1])

            faces.append(img_np)
            ids.append(id)

            # Display the training 
            cv2.imshow("Training", img_np)
            cv2.waitKey(1) == 40  # Display image 


        # Initialize LBPH Face Recognizer
        model = cv2.face.LBPHFaceRecognizer.create()

        # Train the model with faces and ids
        model.train(faces, np.array(ids))
        

        # Save the trained model to a file
        model.write("model.xml")

        # Close the training image window
        cv2.destroyAllWindows()

        # Show training completion message
        messagebox.showinfo("Result", "Training Data Set Completed")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
