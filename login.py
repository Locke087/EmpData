import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from hashlib import sha256
from view_employee import ViewEmployee
class LoginScreen():
    def __init__(self, master: tk.Tk) -> None:
        super().__init__()
        self.master = master
        self.master.title("Login Screen")
        self.master.geometry('1000x720')
        self.frame = tk.Frame(self.master, width=1000, height=720)
        # In center of screen, create welcome message, username and password input boxes with username and password headings
        self.welcome_message = tk.Label(self.frame, text="Welcome", font=('Arial', 50))

        # Take in both username and password as input from the user
        self.username_message = tk.Label(self.frame, text="Employee ID", font=('Arial', 25))

        self.username = tk.Entry(self.frame, font=('Arial', 25))


        self.pass_message = tk.Label(self.frame, text="Password", font=('Arial', 25))

        self.password = tk.StringVar()#Password is stored here
        self.pass_entry = tk.Entry(self.frame, textvariable=self.password, show="*", font=('Arial', 25))

        self.submit = tk.Button(self.frame, text="Submit", command=self.login, font=('Arial', 25))
        #Pack the members
        self.welcome_message.pack()
        self.username_message.pack()
        self.username.pack()
        self.pass_message.pack()
        self.pass_entry.pack()
        self.submit.pack()
        self.frame.pack()

    def login(self):
        print(self.username.get(), self.password.get())
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
                db_username = row[0]

                hash_pass = self.password.get().encode('utf-8')
                hasher.update(hash_pass)
                hash_pass = hasher.hexdigest()
                db_password = row[21]
                
                if hash_pass == db_password and self.username.get() == db_username:
                    
                    #move on to the next window
                    #1. Destory the current window
                    self.frame.destroy()
                    #Must be initialized to variable or it will get dumped by the garbage collector
                    self.app = ViewEmployee(self.master, row)
                    #The code above loads the window
                    #Now we return to avoid getting an error message
                    return
                    


        messagebox.showerror("Invalid credentials", "The username or the password you have entered is not correct")
    
