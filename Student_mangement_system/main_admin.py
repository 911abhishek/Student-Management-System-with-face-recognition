# import cv2
# from tkinter import ttk
# from PIL import Image,ImageTk
import os
from tkinter import*
#desinger figma
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

#own lib
from train import Train
from face_recognition import face_recog
from att_export import Exporter
from std_manage import Student


ASSETS_PATH = Path(r"systemFiles\main_files\frame0")
class mainPage:
    
    def __init__(self, root):
        self.root = root
        
        self.set_gui()
    def set_gui(self):

    
        


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)


        

        # self.root.geometry("1512x982")
        self.root.geometry("1280x720")
        self.root.configure(bg = "#F0F0F0")
        self.root.title("Admin Panel")


        self.canvas = Canvas(
            self.root,
            bg = "#F0F0F0",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1280.0,
            155.0,
            fill="#E97979",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1_configure = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.std_configure,
            relief="flat"
        )
        button_1_configure.place(
            x=907.0,
            y=453.0,
            width=294.0,
            height=210.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2_att = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.attendance,
            relief="flat"
        )
        button_2_att.place(
            x=486.0,
            y=317.0,
            width=308.0,
            height=251.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3_export = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.exportData,
            relief="flat"
        )
        button_3_export.place(
            x=926.0,
            y=182.0,
            width=289.1644592285156,
            height=213.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4_configure = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.showData,
            relief="flat"
        )
        button_4_configure.place(
            x=62.0,
            y=457.0,
            width=294.0,
            height=206.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5_management = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.std_management,
            relief="flat"
        )
        button_5_management.place(
            x=62.0,
            y=192.0,
            width=294.0,
            height=203.0
        )

        self.canvas.create_text(
            254.0,
            17.0,
            anchor="nw",
            text="STUDENTS MANAGEMENT SYSTEM",
            fill="#FFFFFF",
            font=("HammersmithOne Regular", 48 * -1)
        )

        self.canvas.create_text(
            420.0,
            77.0,
            anchor="nw",
            text="Administration Panel",
            fill="#FFFFFF",
            font=("HammersmithOne Regular", 48 * -1)
        )
        self.root.resizable(False, True)

    def std_management(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)
    def std_configure(self):
        configurator = Train(self.root)
        configurator.training_classifier()

    def showData(self):
        # self.new_window = Toplevel(self.root)
        self.app = os.startfile(r"facedata") 
    def attendance(self):
        # self.new_window  = Toplevel(self.root)
        # self.app = face_recog(self.new_window)

        attend = face_recog()
        attend.face_recognition()
    def exportData(self):
        self.new_window = Toplevel(self.root)
        self.app = Exporter(self.new_window)

if __name__ == "__main__":
    root = Tk()
    app = mainPage(root)
    root.mainloop()
