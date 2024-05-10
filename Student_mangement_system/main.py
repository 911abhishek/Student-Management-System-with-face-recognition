# from tkinter import*
# from tkinter import ttk
# from PIL import Image,ImageTk
# import mysql
#deign figmaa
from pathlib import Path
from tkinter import messagebox
import mysql.connector
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
#own lib
from main_admin import mainPage
from main_attendMr import mainAtt




ASSETS_PATH = Path(r"systemFiles\login_files\frame0")
class login_page:
    def __init__(self,root):
        self.root = root
        self.loginGui()
    def loginGui(self):

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)



        self.root.geometry("1280x720")
        # self.root.geometry("1512x982")
        self.root.configure(bg = "#2148C0")

                
        def login():
            uid=entry_1.get()
            pwd=entry_2.get()
            if uid=="" or pwd== "":
                messagebox.showerror("Error","All fields are required", parent = self.root)
            else:
                    
                    #admin data fetching
                    conn = mysql.connector.connect(host = "localhost", username = "root", password = "Abhi@9534", database = "att_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("SELECT * FROM admin WHERE user_id=%s AND pwd=%s", (uid, pwd))
                    data_admin = my_cursor.fetchall()
                    #attendance manager data fetching
                    
                    my_cursor2 = conn.cursor()
                    my_cursor2.execute("Select * FROM att_manager WHERE user_id=%s AND pwd=%s",(uid, pwd))
                    att_manager = my_cursor2.fetchall()


                    
                    if data_admin:
                        messagebox.showinfo("Info","Logged in succesfully", parent=self.root),
                        
                        self.admin_page()
                    elif att_manager:
                        messagebox.showinfo("Info", "logging to Attendance Manager Panel", parent=self.root)
                        self.att_page()

                    
                        
                        
                        
                    else:
                        messagebox.showerror("Error","Check Username or Password", parent = self.root)    
                    conn.commit()
                    conn.close()
                
            
                    
                
            
        canvas = Canvas(
            self.root,
            bg = "#2148C0",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            1182.0,
            542.0,
            image=self.image_image_1
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = canvas.create_image(
            640.0,
            352.5,
            image=self.entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=490.0,
            y=330.0,
            width=300.0,
            height=43.0
        )

        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = canvas.create_image(
            640.0,
            433.5,
            image=self.entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show="*"
        )
        entry_2.place(
            x=490.0,
            y=411.0,
            width=300.0,
            height=43.0
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=login,
            relief="flat"
        )
        button_1.place(
            x=490.0,
            y=483.0,
            width=300.0,
            height=45.0
        )

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            639.0,
            209.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.image_3 = canvas.create_image(
            532.0,
            309.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.image_4 = canvas.create_image(
            532.0,
            393.0,
            image=self.image_image_4
        )

        self.root.resizable(False,False)
    def admin_page(self):
        self.root.destroy()  # Close the login window s
        root_admin = Tk()  # Create a new Tkinter window *it is same like creating a new window like we have done in other main calling function
        app = mainPage(root_admin)  # Initialize the main page
        root_admin.mainloop()
    def att_page(self):
        self.root.destroy()
        root_att = Tk()
        app = mainAtt(root_att)
        root_att.mainloop()

        
        

        
        
if __name__ == "__main__":
    
    root = Tk()
    app = login_page(root)
    root.mainloop()
