import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import csv
from hashlib import sha256
from view_employees import ViewEmployeeAdmin, ViewEmployeeEmp
from Employee import Employee
import os
import csvalchemy
class LoginScreen():
    def __init__(self, master: tk.Tk) -> None:
        super().__init__()
        # This will create style object
        style = Style()
        style.configure('W.TLabel', font =
               ('Arial', 50, 'bold', 'underline'),
                foreground = 'black', background = 'white')
        style.configure('W.TButton', font =
               ('Arial', 25, 'bold', 'underline'),
                foreground = 'black', background = 'black')
 
        self.master = master
        self.master.title("Login Screen")
        self.master.geometry('1000x720')
        self.master['bg'] ='white'
        self.frame = tk.Frame(self.master, width=1000, height=720, background="white")
        # In center of screen, create welcome message, username and password input boxes with username and password headings
        self.welcome_message = Label(self.frame, text="Welcome", style='W.TLabel')

        # Take in both username and password as input from the user
        self.id_message = tk.Label(self.frame, text="Employee ID", font=('Arial', 25), foreground="white", background='black')

        self.id = tk.Entry(self.frame, font=('Arial', 25), background='silver')

        self.id_line = tk.Label(self.frame, text="", font=('Arial', 25), background='white' )
        self.id_line2 = tk.Label(self.frame, text="", font=('Arial', 25), background='white' )
        self.id_line3 = tk.Label(self.frame, text="", font=('Arial', 25), background='white' )


        self.pass_message = tk.Label(self.frame, text="Password", font=('Arial', 25), background='black', foreground="white")

        self.password = tk.StringVar()#Password is stored here
        self.pass_entry = tk.Entry(self.frame, textvariable=self.password, show="*", font=('Arial', 25), background='silver')

        self.submit = tk.Button(self.frame, text="Submit", command=self.login, font=('Arial', 25, 'bold', 'underline'), background="black", foreground="white")
        #Pack the members
        self.welcome_message.pack()
        self.id_line.pack()
        self.id_message.pack()
        self.id.pack()
        self.id_line2.pack()
        self.pass_message.pack()
        self.pass_entry.pack()
        self.id_line3.pack()
        self.submit.pack()
        self.frame.pack()

    def login(self):

        # Check for username in database. If not found, display username or password error to user, prompt to try again. If found, check for password match. If there is no match, display username or password error to the user, prompt to try again (forgot password? Admin reset or email?)
        # If match is found, check permissions in database, switch to correct search screen based on permissions
        employee = csvalchemy.singleton.search_emp_id(self.id.get())
        hasher = sha256()
        hash_pass = self.password.get().encode('utf-8')
        hasher.update(hash_pass)
        hash_pass = hasher.hexdigest()
        #the variable is for null checking
        if employee and employee.password == hash_pass:
            
            #move on to the next window
            #1. Destory the current window
            self.frame.destroy()
 
            #Must be initialized to variable or it will get dumped by the garbage collector
            if employee.permission == 'admin':
                self.app = ViewEmployeeAdmin(self.master, employee)
            else:
                self.app = ViewEmployeeEmp(self.master, employee)
            #The code above loads the window
            #Now we return to avoid getting an error message
            return
                    


        messagebox.showerror("Invalid credentials", "The username or the password you have entered is not correct")
    
