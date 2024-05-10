from tkinter import*
from tkinter import ttk, Tk, Canvas
from tkinter import messagebox
import cv2.data
import mysql.connector
import os
import datetime
import cv2
from tkcalendar import DateEntry\




class Student:
    def __init__(self, root):
        self.root =  root
        
        self.root.geometry("1280x720")
        self.root.title("New Registration")
        #after line 71 i encountered a problem that the to take input from combo i have to store then in a variable - variable is nothing but a countaner to store values
        #so to create a variable inside my class i have to decalre it first
        #below are the varibales that i am using to store values and to further use them
        self.var_dep = StringVar()
        self.var_course =StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_stdId = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_roll = StringVar()
        self.var_mentor = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        
        
        self.setgui()
        
        
    def setgui(self):
        #canva is same as label frame to draw the area to work
        self.canvas = Canvas(
            self.root,
            bg = "#F0F0F0",
            height = 720,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1280.0,
            155.0,
            fill="#E97979",
            outline="")

        self.canvas.place(x = 0, y = 0)

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
            text="Registration Portal",
            fill="#FFFFFF",
            font=("HammersmithOne Regular", 48 * -1)
        )

        mainFrame = Frame(self.root, bd=0, relief=RIDGE) #to check the border i have changed the colour of background to red to get a correct idea
        mainFrame.place(x = 0, y = 160, width=1280, height = 560)
        #let us divide the whole frame into two half
        #left frame will show the entry feild
        #right will show the loaded aur registered student
        leftFrame = Frame(self.root, bd = 5, relief = RIDGE)
        leftFrame.place(x=0, y=165, width = 520, height = 550)

        rightFrame = Frame(self.root, bd=5, relief=RIDGE)
        rightFrame.place(x=520, y = 165, width = 760, height=550)


        #so now we have divided the whole frame into two different parts lets first work on the left side where we take input from the user
        #I used label frame to give correct haeding to the user
        courseFrame = LabelFrame(leftFrame, text="Course Details", bd = 5, relief="raised", font=("Roboto", 10,"bold"))
        courseFrame.place(x=5, y= 0, width=500, height=100)
        #lets countiue with our label frame and add some combobox in it combo box are typically drop down boxes
        #to make it accurate we will use grid - grid can be assumed as a matrix
        dep = Label(courseFrame, text="Department", font=("Roboto", 10, "bold"),bd = 2, relief="flat")
        dep.grid(row=0, column=0, padx = 5, pady= 5)
        dep_combo = ttk.Combobox(courseFrame, width= 18,textvariable=self.var_dep, font=("Arial", 10,), state="readonly")
        dep_combo["values"] = ("Select Department", "BTECH", "BCA", "BBA")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx = 2, pady = 5)
        #lets make same for our course field but to do so i encountred a issue that every dep has different set of course so i have to take the dep and according to it show courses
        #to do so i think an if else statments will be perfect
        course = Label(courseFrame, text="Course", font=("Roboto", (10),"bold"))
        course.grid(row=0, column=3, padx=5, pady=5)
        self.course_combo = ttk.Combobox(courseFrame,width = 18,textvariable=self.var_course, font=("Arial", 10), state="readonly")
        self.course_combo.grid(row = 0, column = 4, padx=5, pady = 5)
        # to do so lets store the value from dep combo box into am varibale
        #okay so for long disccussion with my mates i have decided to make a seperate function for it

        #to use the fucntion again and again whenever we select any departemnt we have to bind it the process is 
        dep_combo.bind("<<ComboboxSelected>>", self.on_department_select)
        self.root.resizable(False, False)
    #making year label
        year = Label(courseFrame, text="Year", font=("Roboto", 10, "bold"))
        year.grid(row=1, column = 0, padx=5, pady=5)
        year_combo = ttk.Combobox(courseFrame, textvariable=self.var_year, width=18,font=("Arial", 10), state="readonly")
        year_combo["values"] =("Select Year", "2020","2021","2022","2023","2024", "2025")
        year_combo.grid(row=1, column=1, padx=5, pady=5)
        year_combo.current(0)
    #making semester box
        sem = Label(courseFrame, text="Semester", font=("Roboto", 10, "bold"))
        sem.grid(row=1, column = 3, padx=5, pady= 5)
        sem_combo = ttk.Combobox(courseFrame, textvariable=self.var_sem, width = 18, font=("Arial", 10), state="readonly")
        sem_combo["values"] = ("Select Semester", "First", "Second", "Third", "Fourth", "Fifth", "Sixth")
        sem_combo.current(0)
        sem_combo.grid(row=1, column = 4, padx=5, pady=5)
        #lets add a new label frame for student details section
        stdDetail = LabelFrame(leftFrame, text="Student Details", font=("Roboto", 10, "bold"),bd = 5, relief="raised")
        stdDetail.place(x = 5, y = 100, width = 500, height=150)

        idLabel = Label(stdDetail, text="Student Id", font=("Roboto", 10, "bold"))
        idLabel.grid(row=0, column = 0 , padx=5, pady=5)

        idEntry = ttk.Entry(stdDetail, textvariable=self.var_stdId, font=("Roboto", 10), width=20)
        idEntry.grid(row = 0, column = 1, padx=5, pady = 5)

        nameLabel = Label(stdDetail, text="Name", font=("Roboto", 10, "bold"))
        nameLabel.grid(row=0 , column=2, padx=5, pady=5)

        nameEntry = ttk.Entry(stdDetail, textvariable=self.var_name, font=("Roboto", 10, "bold"), width=20,)
        nameEntry.grid(row=0, column=3, padx=5, pady=5)

        genderLabel = Label(stdDetail, text="Gender", font=("Roboto", 10, "bold"))
        genderLabel.grid(row=1, column=0, padx=5, pady = 5)

        gendercombo = ttk.Combobox(stdDetail, textvariable=self.var_gender, font=("Roboto", 10, "bold"), width = 17, state="readonly")
        gendercombo["values"] = ("Select Gender", "Male", "Female", "Transgender")
        gendercombo.current(0)
        gendercombo.grid(row = 1, column = 1, padx=5, pady=5)

        rollLabel = Label(stdDetail, text="Roll No", font =("Roboto", 10, "bold"))
        rollLabel.grid(row=1, column = 2, padx=5, pady=5)

        rollEntry = ttk.Entry(stdDetail, textvariable=self.var_roll, font=("Roboto", 10, "bold"), width=20,)
        rollEntry.grid(row = 1, column= 3, padx=5, pady=5)

        dobLabel = Label(stdDetail, text="DOB", font=("Roboto", 10, "bold"))
        dobLabel.grid(row=2, column = 0, padx= 5, pady = 5)

        #we decided to add a calender to choose between the respective dob 
        #so to achieve that we used tkcalender
        #pip install tkcalender
        #from tk.Calender import DateEntry

        dobEntry = DateEntry(stdDetail, textvariable=self.var_dob, font=("Roboto", 10), width = 17, date_pattern='yyyy-mm-dd')
        dobEntry.grid(row=2, column = 1, padx=5, pady =  5)

        mentorLabel = Label(stdDetail, text="Mentor", font=("Roboto", 10 , "bold"))
        mentorLabel.grid(row = 3, column = 0, padx=5, pady = 5)

        mentorEntry = ttk.Entry(stdDetail, textvariable=self.var_mentor, font=("Roboto", 10),width = 20 )
        mentorEntry.grid(row = 3, column = 1, padx=5, pady = 5)

        phoneLabel = ttk.Label(stdDetail, text="Phone No", font=("Roboto", 10, "bold"))
        phoneLabel.grid(row=3, column =2, padx=5, pady = 5)

        phoneEntry = ttk.Entry(stdDetail, textvariable=self.var_phone, font=("Roboto", 10,), width=20)
        phoneEntry.grid(row=3, column= 3, padx=5, pady=5)

        mailLabel = Label(stdDetail, text="Email Id", font=("Roboto", 10, "bold"))
        mailLabel.grid(row=2, column=2, padx=5, pady=5)

        mailEntry = ttk.Entry(stdDetail, textvariable=self.var_email, font=("Roboto", 10), width=20,)
        mailEntry.grid(row=2, column=3, padx=5, pady=5)

        figmaButtonFrame = Frame(leftFrame, bd = 5)
        figmaButtonFrame.place(x=5, y = 250, width=500, height=290)
        # stdDetail.place(x = 5, y = 100, width = 500, height=150)
        saveButton = ttk.Button(figmaButtonFrame, text="save", command=self.save_my_data)
        saveButton.grid(row = 0, column=1, padx=5, pady = 5)

        updateButton = ttk.Button(figmaButtonFrame,command=self.update_my_data, text = "Update")
        updateButton.grid(row = 0, column =2 , padx = 5, pady = 5)

        resetButton = ttk.Button(figmaButtonFrame, text="Reset",command=self.reset_my_data)
        resetButton.grid(row = 0 , column = 3, padx=5 , pady = 5)

        deleteButton = ttk.Button(figmaButtonFrame,text = "Delete", command=self.delete_my_data)
        deleteButton.grid(row = 0, column = 4, padx=5, pady=5)
        self.capture_button = ttk.Button(figmaButtonFrame, text="Capture Face", command=self.capture_face)
        self.capture_button.grid(row=0, column=5, padx=5, pady=5)

        #okay table will be the frame where i am going to show my table
        table_area = Frame(rightFrame,bd= 5, relief="raised", )
        table_area.place(x=5, y = 5, width = 740, height = 530)
        # rightFrame.place(x=520, y = 165, width = 760, height=550)taking refrence
        #right frame side work
            #after saving the data i want to show the data in the right frame 
    #through lots of research we found out that a seperate tree view function is in tkinter to arrange and show the data
        scroll_hor = ttk.Scrollbar(table_area, orient=HORIZONTAL)
        self.student_table = ttk.Treeview(table_area, columns=("students_id", "name", "roll", "department",'course', "year", "semester", "gender", "mentor", "phone", "email", "dob"),xscrollcommand=scroll_hor.set)


        scroll_hor.pack(side=BOTTOM,fill=X)
        
        scroll_hor.config(command=self.student_table.xview)#this will configure the scroll bar

#to show heading we have to write columns into text
        self.student_table.heading("students_id" , text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("department", text = "Department")
        self.student_table.heading("course", text = "Course")
        self.student_table.heading("year", text="Year")
        
        
        self.student_table.heading("semester", text="Semester")
        
        self.student_table.heading("gender", text="Gender")
        
        self.student_table.heading("mentor", text="Mentor")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("email", text = "Email")
        self.student_table.heading("dob", text = "DOB")
        self.student_table["show"] = "headings"#"show" option determines what parts of the widget are visible when we choose "headings"it means only heading will be shown
        self.student_table.pack(fill=BOTH, expand = 1)#pack is simply arranging items in a box
        self.student_table.bind("<ButtonRelease>", self.update_using_cursor)#this will bind the function update_using_cursor
        self.fetch_my_data()#function written in line 303

#half code
#function which i develop to integrate between department choice with respect to shown courses
    def on_department_select(self,event):
        selected_department = self.var_dep.get()
        # print(selected_department)
        if selected_department == "BTECH":
            self.course_combo["values"] = ("Select Course", "CSE", "Civil", "Mechanical")
        elif selected_department == "BCA":
            self.course_combo["values"] = ("Select Course", "Accounts", "Commerce")
        elif selected_department == "BBA":
            self.course_combo["values"] = ("Select Course", "Finance", "Marketing", "Human Resources")
        else:
            self.course_combo["values"] = ("Select Course",)
        self.course_combo.current(0)
    def conn_database(self):
        # after writng line 308 i found out that i have the same code again and again to conn from my database so created this fucntion which returns the conn
                conn = mysql.connector.connect(
                    host = "localhost",
                    username = 'root',
                    password = "Abhi@9534",
                    database = "att_system"
                )
                return conn
    def save_my_data(self):
        # i have develop these function to save my data that are given by user 
        #the first step i take is to retrive the data by get function 

 
        studentId = self.var_stdId.get()
        department = self.var_dep.get()
        course = self.var_course.get()
        year = self.var_year.get()
        semester  = self.var_sem.get()
        name = self.var_name.get()
        gender = self.var_gender.get()
        roll = self.var_roll.get()
        mentor = self.var_mentor.get()
        phone = self.var_phone.get()
        email = self.var_email.get()
        dob = self.var_dob.get()
        #so for now we have retrived all the data that the user has provided the second step will be to check data 
        #if the data we get is it the intial stage we will show a error
        #we are using a if statement to achieve this
        #lower statement i used for debugging
        #print(f"id={studentId}, depar ={department}, course = {course}, year = {year}, semester = {semester}, \n name = {name}, gender = {gender}, roll = {roll}, mentor = {mentor}, phone = {phone}, mail = {email}, dob = {dob}")
        conn = self.conn_database()
        save_cursor = conn.cursor()
        if (studentId == "" or department == "Select Department" or course == "Select Course" or course == "" or year == "Select Year" or 
            semester == "Select Semester" or name == ""or  gender=="Select Gender" or roll == "" or mentor == "" or
            
            phone == ""  or email == ""):

            messagebox.showerror("Missing Information", "Please fill in all required fields.", parent = self.root)
        else:

            try:

                save_cursor = conn.cursor()
                sql = "INSERT INTO students(students_id, department, course, year, semester, name, gender, roll, mentor, phone, email, dob) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)"
                values = (studentId, department, course, year, semester, name, gender, roll, mentor, phone, email, dob)
                save_cursor.execute(sql,values)
                conn.commit()
                self.fetch_my_data()
                messagebox.showinfo("Success", "Data saved Successfully!")
                conn.close()

                
            except Exception as error:
                messagebox.showerror("Error", f"error saving data :{str(error)}")
            self.tree.insert("", "end", values=(studentId, name, department, course, year, semester, gender, roll, mentor, phone, email, dob))

    def fetch_my_data(self):
         #this function will fetch all the data from the sql database
        #  lets connect first func with db   
        conn = self.conn_database()#function made by to remove the issue to write the same code again and again
        fetch_cursor = conn.cursor()
        fetch_cursor.execute("SELECT * FROM students")

        for old_data in self.student_table.get_children():
             #this function will delete the old data in the table
             self.student_table.delete(old_data)
        datas = fetch_cursor.fetchall()
        for data in datas:
             #this function will take data one by one and insert it into the table
             self.student_table.insert("", END, values=data)
        conn.commit()
        conn.close()
        #now this function will be called on save_my_data function to see the db in the table and inside the student table also

    
    def update_using_cursor(self, event=""):
         #this function will help us to update the data 
         #when a cursor click on the table data then the data should insert inside the respective blocks for edit and upload
         on_click = self.student_table.focus() #focus is commanly used to retrive the data that is clicked
         print(on_click)
         content = self.student_table.item(on_click)#this line of code will extract the whole content inside the content
         print(content)
         data = content["values"]#this will filter the value of the content and store it in data

         #now its time to extract the perticular data from each data variable
         self.var_stdId.set(data[0])#lets break this down this function will set the data of std id (data[0]) will extract the of index 0 and as we shown in table the first column has std id then name, roll and so on
         self.var_name.set(data[1])
         self.var_roll.set(data[2])
         self.var_dep.set(data[3])
         self.var_course.set(data[4])
         self.var_year.set(data[5])
         self.var_sem.set(data[6])
         self.var_gender.set(data[7])
         self.var_mentor.set(data[8])
         self.var_phone.set(data[9])
         self.var_email.set(data[10])
         self.var_dob.set(data[11])
    
    def update_my_data(self):
         #this function will update my data when the button is clicked
        studentId = self.var_stdId.get()
        department = self.var_dep.get()
        course = self.var_course.get()
        year = self.var_year.get()
        semester  = self.var_sem.get()#i have copied this code from save_my_data function just to ensure at the time of updating someone dosent fill empty data

        name = self.var_name.get()
        gender = self.var_gender.get()
        roll = self.var_roll.get()
        mentor = self.var_mentor.get()
        phone = self.var_phone.get()
        email = self.var_email.get()
        dob = self.var_dob.get()
        if (studentId == "" or department == "Select Department" or course == "Select Course" or course == "" or year == "Select Year" or 
            semester == "Select Semester" or name == ""or  gender=="Select Gender" or roll == "" or mentor == "" or
            
            phone == ""  or email == ""):

            messagebox.showerror("Missing Information", "Please fill in all required fields.", parent = self.root)
        else:
            #  pass

            try:
                 update = messagebox.askyesno("Update", "Are you sure you want to update the details", parent = self.root) 
                 conn = self.conn_database()
                 cursor = conn.cursor()
                 sqlcode =("UPDATE students SET name = %s , roll= %s, department= %s, course= %s, year= %s, semester= %s, gender= %s, mentor= %s, phone= %s, email= %s, dob= %s  WHERE students_id= %s")
                 values = (name, roll, department, course, year, semester, gender, mentor, phone, email, dob, studentId)
                 cursor.execute(sqlcode, values)
                 messagebox.showinfo("", "Details Updated Successfully")

                 conn.commit()
                 self.fetch_my_data()
                 conn.close()                
            except Exception as e:
                 messagebox.showerror("Error", f"Due to {str(e)}")

    def delete_my_data(self):
            try:
                conn = self.conn_database()
                cursor = conn.cursor()
                sqlcode = ("DELETE FROM students WHERE students_id = %s")
                student_id = self.var_stdId.get()
                print(student_id)
                val = (student_id,)
                cursor.execute(sqlcode, val)
                messagebox.showinfo("", "Deleted Successfully")
                conn.commit()
                self.fetch_my_data()
                conn.close()

            except Exception as e:
                 messagebox.showerror("", f"Due to {str(e)}")
    def reset_my_data(self):
        self.var_dep.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_stdId.set(""),
        self.var_name.set(""),
        self.var_course.set("Select Course"),
        self.var_gender.set("Select Gender"),
        self.var_roll.set(""),
        self.var_dob.set(""),
        self.var_mentor.set(""),
        self.var_phone.set(""),
        self.var_email.set("")

########################################################################################face detection
    def capture_face(self):
        cam = cv2.VideoCapture(0)
        face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        face_id = self.var_stdId.get()
        face_name = self.var_name.get()
        count = 0
        while True:
                ret , img =  cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_detector.detectMultiScale(gray, 1.3,5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img, (x,y),(x+w, y+h), (255, 0, 0), 2)
                    count += 1
                    if not os.path.exists("facedata"):
                        os.makedirs("facedata")
                        cv2.imwrite("facedata/student."+str(face_id) + '.'+str(count)+".jpg",gray[y:y+h,x:x+w])
                        cv2.imshow('image', img)
                    else:
                        cv2.imwrite("facedata/student."+str(face_id) + '.'+str(count)+".jpg",gray[y:y+h,x:x+w])
                        cv2.putText(img, f"ID :{str(face_id)},name : {str(face_name)}, count:{str(count)}", (x-50, y+h+25), cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,255),1)
                        cv2.imshow('image', img)

                    if cv2.waitKey(1)==13 or int(count == 50):
                         break
                if cv2.waitKey(1)==13 or int(count == 50):
                    break
                         
                         
        cam.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Face Scan", "Successful")
                    
                       
                    
                
        
        
                        
                   
            
                    
                    

                         
                   
                    



    

         

    


        
         
        




        


        

        
       


        
if __name__ == "__main__":

    root = Tk()
    mainWin = Student(root)
    root.mainloop()