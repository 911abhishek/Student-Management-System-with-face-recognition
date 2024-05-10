from tkinter import*
from tkinter import ttk,Tk
import csv
import os

data_path = "attendance_data"
class Exporter:
    def __init__(self,root):

        self.root = root
        self.root.geometry("500x500")
        self.root.title('Export Attendance')
        
        self.export_attend()
        
        
        
        



    def open_csv_in_excel(self):
        selected_file = self.csv_listbox.get(ACTIVE)#its a tikinter box width that will list the csv files in the data path tk.active is used to select the csv file
        #after the selection the selected file will be stored in varibale "selected_file"
        if selected_file:
            file_path = os.path.join(data_path, selected_file)#this will store the full path of usable data
            os.system(f'start excel "{file_path}"')# executes a shell command to open the specified file (file_path) in Microsoft Excel.

    def export_attend(self):
        # Get all CSV files in the directory
        csv_files = [file for file in os.listdir(data_path) if file.endswith('.csv')]#from our path selecting only the files that ends with csv

        # root = tk.Tk()
        

        self.csv_listbox = Listbox(self.root, selectmode=SINGLE, height=20, width=60)#here we create a simple list box using tkinter
        for file in csv_files:#here we are taking csv files on by one and adding or appending it to the list box we have made
            self.csv_listbox.insert(END, file)
        self.csv_listbox.pack()#packing of the file

        open_button = ttk.Button(self.root, text='Export', command=self.open_csv_in_excel)# a simple  button to export the data
        open_button.pack()

if __name__ == "__main__":
    root = Tk()
    obj = Exporter(root)
    root.mainloop()
