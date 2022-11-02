import tkinter as tk
from tkinter import messagebox, ttk
import csv
from hashlib import sha256
def login():
    print(username.get(), password.get())
    # Check for username in database. If not found, display username or password error to user, prompt to try again. If found, check for password match. If there is no match, display username or password error to the user, prompt to try again (forgot password? Admin reset or email?)
    # If match is found, check permissions in database, switch to correct search screen based on permissions
    with open('./employee.csv') as file:
        reader = csv.reader(file)
       
        for i,row in enumerate(reader):
            #Skip it if it's the first row
            #because that contains the field names
            #not the actual data invovled
            if i == 0:
                continue
            hasher = sha256()
            db_username = row[18]

            hash_pass = password.get().encode('utf-8')
            hasher.update(hash_pass)
            hash_pass = hasher.hexdigest()
            db_password = row[19]
            if hash_pass == db_password and username.get() == db_username:
                print('Found it')
                #move on to the next window
                return True
    messagebox.showerror("Invalid credentials", "The username or the password you have entered is not correct")
# Use Tkinter to create window
window = tk.Tk()
frame = ttk.Frame(window)

# In center of screen, create welcome message, username and password input boxes with username and password headings
welcome_message = tk.Label(frame, text="Welcome", font=('Arial', 25), width=50)

# Take in both username and password as input from the user
username_message = tk.Label(frame, text="User Name")

username = tk.Entry(frame)


pass_message = tk.Label(frame, text="Password")

password = tk.StringVar()#Password is stored here
pass_entry = tk.Entry(master=frame, textvariable=password, show="*")

submit = tk.Button(frame, text="Submit", command=login)


welcome_message.pack()
username_message.pack()
username.pack()
pass_message.pack()
pass_entry.pack()
submit.pack()

frame.pack()
window.mainloop()