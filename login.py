import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from hashlib import sha256
from manager import WindowManager
class LoginScreen(tk.Tk):
    def __init__(self,manager: WindowManager, screenName: str | None = ..., baseName: str | None = ..., className: str = ..., useTk: bool = ..., sync: bool = ..., use: str | None = ...) -> None:
        super().__init__()
        self.title("Login Screen")
        self.geometry('1000x720')
        # In center of screen, create welcome message, username and password input boxes with username and password headings
        self.welcome_message = tk.Label(self, text="Welcome", font=('Arial', 50))

        # Take in both username and password as input from the user
        self.username_message = tk.Label(self, text="Employee ID", font=('Arial', 25))

        self.username = tk.Entry(self, font=('Arial', 25))


        self.pass_message = tk.Label(self, text="Password", font=('Arial', 25))

        self.password = tk.StringVar()#Password is stored here
        self.pass_entry = tk.Entry(master=self, textvariable=self.password, show="*", font=('Arial', 25))

        self.submit = tk.Button(self, text="Submit", command=self.login, font=('Arial', 25))
        self.pack_members()
    def pack_members(self):
        self.welcome_message.pack()
        self.username_message.pack()
        self.username.pack()
        self.pass_message.pack()
        self.pass_entry.pack()
        self.submit.pack()

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
                db_password = row[18]
                if hash_pass == db_password and self.username.get() == db_username:
                    print('Found it')
                    #move on to the next window
                    return True
        messagebox.showerror("Invalid credentials", "The username or the password you have entered is not correct")
    