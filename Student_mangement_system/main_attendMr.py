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
class mainAtt:
    def __init__(self, root):
        self.root = root
        self.set_gui()

    def set_gui(self):
        def relative_to_assets(path : str) -> Path:
            return ASSETS_PATH/Path(path)
        
        self.root.geometry("1280x720")
        self.root.configure(bg = "#F0F0F0")
        self.root.title("Attendance Manager")


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

        self.button_image_config = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_config = Button(
            image=self.button_image_config,
            borderwidth=0,
            highlightthickness=0,
            command=self.std_configure,
            relief="flat"
        )
        button_config.place(
            x=853.0,
            y=188.0,
            width=294.0,
            height=210.0
        )

        self.button_image_att = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_att = Button(
            image=self.button_image_att,
            borderwidth=0,
            highlightthickness=0,
            command=self.take_att,
            relief="flat"
        )
        button_att.place(
            x=465.0,
            y=356.0,
            width=308.0,
            height=251.0
        )

        self.button_image_export = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_export = Button(
            image=self.button_image_export,
            borderwidth=0,
            highlightthickness=0,
            command=self.export,
            relief="flat"
        )
        button_export.place(
            x=95.0,
            y=185.0,
            width=289.1644592285156,
            height=213.0
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
            384.0,
            77.0,
            anchor="nw",
            text="Attendance Manager",
            fill="#FFFFFF",
            font=("HammersmithOne Regular", 48 * -1)
        )
        self.root.resizable(False, False)
    def std_configure(self):
        configurator = Train(self.root)
        configurator.training_classifier()

    def take_att(self):
        attend = face_recog()
        attend.face_recognition()

    def export(self):
        self.new_window = Toplevel(self.root)
        self.app = Exporter(self.new_window)
    def std_management(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)
if __name__ == "__main__":
    root = Tk()
    app = mainAtt(root)
    root.mainloop()

