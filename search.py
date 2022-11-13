import tkinter as tk
from tkinter import messagebox, ttk
import csv
def search():
    print(id.get(), name.get())

    with open('./employee.csv') as file:
        reader = csv.reader(file)
       
        for i,row in enumerate(reader):
            #Skip it if it's the first row
            #because that contains the field names
            #not the actual data invovled
            if i == 0:
                continue
            db_id = row[0]
            db_name = row[1]
            db_name = db_name.strip()
            print(name.get() + id.get() + db_name + db_id)
            if name.get() == db_name and id.get() == db_id:
                print('Found it')
                #move on to the next window
                fullstring = ""
                for j in row:
                    fullstring += j + " "

                messagebox.showinfo("All of it", fullstring)
                return True
    messagebox.showerror("Invalid credentials", "The employee id or the name you have entered is not correct")
# Use Tkinter to create window
window = tk.Tk()
frame = ttk.Frame(window)

# In center of screen, create welcome message, username and password input boxes with username and password headings
welcome_message = tk.Label(frame, text="Search Employee", font=('Arial', 25), width=50)

# Take in both username and password as input from the user
username_message = tk.Label(frame, text="Employee ID")

id = tk.Entry(frame)

pass_message = tk.Label(frame, text="Employee First Name")

name = tk.Entry(frame)

submit = tk.Button(frame, text="Submit", command=search)


welcome_message.pack()
username_message.pack()
id.pack()
pass_message.pack()
name.pack()
submit.pack()

frame.pack()
window.mainloop()