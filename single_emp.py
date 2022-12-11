from Employee import Employee
import tkinter as tk
from tkinter import messagebox
import csv

class SingleEmployeePrivate():
    def __init__(self,master, viewer, employee) -> None:
        self.master = master
        self.master.title("View Employee Screen")
        self.master.geometry('1000x720')
        self.master['bg'] = '#007385'

        #TODO Binding is a tiny bit buggy when clicking. Maybe removing the feature to begin with?
        #TODO actually document this document
        self.frame =tk.Frame(width=1000, height=720, background='#007385')
        self.frame.grid(row=0, column=0)
        # In center of screen, create welcome message, username and password input boxes with username and password headings
        self.user = employee
        self.viewer = viewer
        self.back_button = tk.Button(self.frame, text='Back', command=self.go_back, foreground="white", background="black")
        self.back_button.grid(row=0, column=0, padx=0)
        self.back_button1 = tk.Button(self.frame, text='Print Pay', command=self.printpayInfo, foreground="white", background="black")
        self.back_button1.grid(row=0, column=2, padx=0)
        self.title_view = tk.Label(self.frame, text=f"{self.user.fname} {self.user.lname}'s Profile", font=('Arial', 50), foreground="white", background="black")
        self.title_view.grid(row=0, column=1, padx=0, sticky=tk.W)
        self.views: dict[tk.Label] = {}
        self.views['id'] = tk.Label(self.frame, text="ID: " + self.user.emp_id, foreground="white", background="black")
        self.views['fname'] = tk.Label(self.frame, text="First Name: " + self.user.fname, foreground="white", background="black")
        self.views['lname'] = tk.Label(self.frame, text="Last Name: " + self.user.lname, foreground="white", background="black")
        self.views['address'] = tk.Label(self.frame, text="Address: " + str(self.user.address), foreground="white", background="black")
        self.views['office_phone'] = tk.Label(self.frame, text="Office Phone: " + self.user.office_phone, foreground="white", background="black")
        self.views['pay_type'] = tk.Label(self.frame, text="Paytype: " + self.user.pay_type, foreground="white", background="black")
        self.views['wage'] = tk.Label(self.frame, text="Wage: " + self.user.wage, foreground="white", background="black")
        self.views['birthday'] = tk.Label(self.frame, text="Birthday" + self.user.birthday, foreground="white", background="black")
        self.views['permission'] = tk.Label(self.frame, text="Permission Level: " + self.user.permission, foreground="white", background="black")
        self.views['title'] = tk.Label(self.frame, text="Title: " + self.user.title, foreground="white", background="black")
        self.views['department'] = tk.Label(self.frame, text="Department: " + self.user.department, foreground="white", background="black")
        self.views['office_email'] = tk.Label(self.frame, text="Office Email: " + self.user.office_email, foreground="white", background="black")
        self.views['emergency_contact'] = tk.Label(self.frame, text="Emergency Contact: " + self.user.emergency_contact, foreground="white", background="black")
        self.views['start_date'] = tk.Label(self.frame, text="Start Date: " + self.user.start_date, foreground="white", background="black")
        self.views['end_date'] = tk.Label(self.frame, text="End Date: " + self.user.end_date, foreground="white", background="black")
        self.views['bank_info'] = tk.Label(self.frame, text="Bank Info: " + self.user.bank_info, foreground="white", background="black")
        self.views['is_deactivated'] = tk.Label(self.frame, text="Is Deactivated: " + self.user.is_deactivated, foreground="white", background="black")
        self.views['social_secuitry'] = tk.Label(self.frame, text= "Social Secuitry: " + self.user.social_secuitry, foreground="white", background="black")

        rlim = 9
        clim = 4
        r, c = 1, 0
        for key, view in self.views.items():
            # print('dict values', view, key)
            view.grid(row=r, column=c, padx=10, pady=20)
            r += 1
            if r >= rlim:
                r = 1
                c += 1



        
    
    def go_back(self):
        from view_employees import ViewEmployeeEmp, ViewEmployeeAdmin
        self.frame.destroy()
        #TODO Insert total data  in place of the user below
        if self.viewer.permission == 'admin':
            self.app = ViewEmployeeAdmin(self.master, employee_data=self.viewer)
        else:
            self.app = ViewEmployeeEmp(self.master, employee_data=self.viewer)
    def printpayInfo(self):
        messagebox.showinfo("payslip has been generated", "it is payslip.txt")
        with open("payslip.txt", 'w') as fh:
            fh.write(f"payslip for {self.user.fname} {self.user.lname}" + "\n")
            fh.write(f"Bank is {self.user.bank_info}" + "\n")
            fh.write(f"Pay is {self.user.wage}$ {self.user.pay_type}" + "\n")
        

class SingleEmployeePub():
    def __init__(self,master,viewer,  employee: Employee) -> None:
        self.master = master
        self.master.title("View Employee Screen")
        self.master.geometry('1000x720')

        
        self.frame =tk.Frame(width=1000, height=720)
        self.frame.grid(row=0, column=0)
        # In center of screen, create welcome message, username and password input boxes with username and password headings
        self.user = employee
        self.viewer = viewer
        self.back_button = tk.Button(self.frame, text='Back', command=self.go_back)
        self.back_button.grid(row=0, column=0, padx=0)
        self.back_button1 = tk.Button(self.frame, text='Print Pay', command=self.printpayInfo)
        self.back_button1.grid(row=0, column=2, padx=0)
        self.title_view = tk.Label(self.frame, text=f"{self.user.fname} {self.user.lname}'s Profile", font=('Arial', 50))
        self.title_view.grid(row=0, column=1, padx=0, sticky=tk.W)
        self.views: dict[tk.Label] = {}
        self.views['id'] = tk.Label(self.frame, text="ID: " + self.user.emp_id)
        self.views['fname'] = tk.Label(self.frame, text="First Name: " + self.user.fname)
        self.views['lname'] = tk.Label(self.frame, text="Last Name: " + self.user.lname)
        self.views['office_phone'] = tk.Label(self.frame, text="Office Phone: " + self.user.office_phone)
        self.views['birthday'] = tk.Label(self.frame, text="Birthday: " + self.user.birthday)
        self.views['title'] = tk.Label(self.frame, text="Title: " + self.user.title)
        self.views['department'] = tk.Label(self.frame, text="Department: " + self.user.department)
        self.views['office_email'] = tk.Label(self.frame, text="Office Email: " + self.user.office_email)
        self.views['emergency_contact'] = tk.Label(self.frame, text="Emergency Contact: " + self.user.emergency_contact)

        rlim = 5
        clim = 4
        r, c = 1, 0
        for key, view in self.views.items():
            # print('dict values', view, key)
            view.grid(row=r, column=c, padx=10, pady=20)
            r += 1
            if r >= rlim:
                r = 1
                c += 1
    
    def go_back(self):
        from view_employees import ViewEmployeeEmp
        self.frame.destroy()
        #TODO Insert total data  in place of the user below
        self.app = ViewEmployeeEmp(self.master, employee_data=self.viewer)