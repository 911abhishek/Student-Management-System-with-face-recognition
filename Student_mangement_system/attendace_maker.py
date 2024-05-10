import os
import datetime
import mysql.connector

def attendance_marker(ids):
            conn = mysql.connector.Connect(host="localhost", username = "root", password = "Abhi@9534", database="att_system")
            cursor = conn.cursor()
            sql_code = ("SELECT roll, name,department FROM students where students_id=%s")
            
            cursor.execute(sql_code,(ids,))#extracting the values from data base
            r = cursor.fetchone()#storing the extracted values to a variable
            if r:
                roll, name, department = r#stored variable has four values so extracting them
                print(roll, name, department)
                saveAttendance(ids,roll,name,department)
                # saveatt(ids,roll,name,department)
def saveAttendance(id, roll_no, name, dep):
    current_datetime = datetime.datetime.now()
    date = current_datetime.date()
    time = current_datetime.time()
    dir = "attendance_data"
    os.makedirs(dir, exist_ok=True)
    file_path = os.path.join(dir, f"attendance_{date}.csv")
    
    header = "Student_id, Roll NO, Name, Department, Date, Time, Status\n"
    
    if not os.path.isfile(file_path):
        with open(file_path, "w", newline="\n") as file:
            file.write(header)
    else:
        with open(file_path, "r", newline="\n") as fle:
            dataList = fle.readlines()
            for line in dataList:
                entry = line.strip().split(", ")
                if entry[0] == str(id) and entry[1] == str(roll_no) and entry[2] == name and entry[3] == dep:
                    return  # Duplicate entry found, do not write again
    
    with open(file_path, "a", newline="\n") as fle:
        fle.write(f"{id}, {roll_no}, {name}, {dep}, {date}, {time}, Present\n")


def main():
    attendance_marker(1)
    attendance_marker(1)
    attendance_marker(1)
  
if __name__ == "__main__":
     main()
    #  pass