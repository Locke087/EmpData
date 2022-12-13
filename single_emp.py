from Employee import Employee
import tkinter as tk
from tkinter import messagebox
import csv
from hover_button import HoverButton
class SingleEmployeePrivate():
    def __init__(self,master, viewer, employee) -> None:
        self.master = master
        self.master.title("View Employee Screen")
        self.master.geometry('1200x900')
        self.master['bg'] = '#007385'

        #TODO Binding is a tiny bit buggy when clicking. Maybe removing the feature to begin with?
        #TODO actually document this document
        self.frame =tk.Frame(width=1000, height=720, background='#007385')
        self.frame.grid(row=0, column=0)
        # In center of screen, create welcome message, username and password input boxes with username and password headings
        self.user = employee
        self.viewer = viewer
        self.back_button = HoverButton("Back", "Click here to go back", self.go_back, self.frame, font=('Arial', 25))
        self.back_button.grid(row=0, column=0, padx=0, pady=(10,0))
        self.title_view = tk.Label(self.frame, text=f"{self.user.fname} {self.user.lname}'s Profile", font=('Arial', 50), background='#007385')
        self.title_view.grid(row=0, column=1, padx=0, sticky=tk.W)
        self.views: dict[tk.Label] = {}
        abbr_values = {'dm':"Direct Method", 'mm':'Mail Method', 'y':'Yes', 'n':'No'}
        FONT_SIZE = 20
        self.views['id'] = tk.Label(self.frame, text="ID: " + self.user.emp_id, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['fname'] = tk.Label(self.frame, text="First Name: " + self.user.fname, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['lname'] = tk.Label(self.frame, text="Last Name: " + self.user.lname, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['address'] = tk.Label(self.frame, text="Address: " + str(self.user.address), background='#00424d',font=('Arial', FONT_SIZE))
        self.views['office_phone'] = tk.Label(self.frame, text="Office Phone: " + self.user.office_phone, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['pay_type'] = tk.Label(self.frame, text="Paytype: " + self.user.pay_type, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['wage'] = tk.Label(self.frame, text="Wage: " + self.user.wage, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['birthday'] = tk.Label(self.frame, text="Birthday" + self.user.birthday, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['permission'] = tk.Label(self.frame, text="Permission Level: " + self.user.permission, background='#00424d',font=('Arial', 25))
        self.views['title'] = tk.Label(self.frame, text="Title: " + self.user.title, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['department'] = tk.Label(self.frame, text="Department: " + self.user.department, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['office_email'] = tk.Label(self.frame, text="Office Email: " + self.user.office_email, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['emergency_contact'] = tk.Label(self.frame, text="Emergency Contact: " + self.user.emergency_contact, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['start_date'] = tk.Label(self.frame, text="Start Date: " + self.user.start_date, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['end_date'] = tk.Label(self.frame, text="End Date: " + self.user.end_date, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['bank_info'] = tk.Label(self.frame, text="Bank Info: " + abbr_values[self.user.bank_info], background='#00424d',font=('Arial', FONT_SIZE))
        self.views['is_deactivated'] = tk.Label(self.frame, text="Is Deactivated: " + abbr_values[self.user.is_deactivated], background='#00424d',font=('Arial', FONT_SIZE))
        self.views['social_secuitry'] = tk.Label(self.frame, text= "Social Secuitry: " + self.user.social_secuitry, background='#00424d',font=('Arial', FONT_SIZE))

        rlim = 8
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
   
        

class SingleEmployeePub():
    def __init__(self,master,viewer,  employee: Employee) -> None:
        self.master = master
        self.master.title("View Employee Screen")
        self.master.geometry('1200x900')
        self.master['bg'] = '#007385'

        
        self.frame =tk.Frame(width=1000, height=720, background='#007385'
)
        self.frame.grid(row=0, column=0)
        # In center of screen, create welcome message, username and password input boxes with username and password headings
        self.user = employee
        self.viewer = viewer
        self.back_button = HoverButton("Back", "Click here to go back", self.go_back, self.frame, font=('Arial', 25))
        self.back_button.grid(row=0, column=0, padx=0, pady=(10,0))
        self.title_view = tk.Label(self.frame, text=f"{self.user.fname} {self.user.lname}'s Profile", font=('Arial', 50), background='#00424d')
        self.title_view.grid(row=0, column=1, padx=0, sticky=tk.W)
        self.views: dict[tk.Label] = {}
        FONT_SIZE = 25
        self.views['id'] = tk.Label(self.frame, text="ID: " + self.user.emp_id, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['fname'] = tk.Label(self.frame, text="First Name: " + self.user.fname, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['lname'] = tk.Label(self.frame, text="Last Name: " + self.user.lname, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['office_phone'] = tk.Label(self.frame, text="Office Phone: " + self.user.office_phone, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['birthday'] = tk.Label(self.frame, text="Birthday: " + self.user.birthday, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['title'] = tk.Label(self.frame, text="Title: " + self.user.title, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['department'] = tk.Label(self.frame, text="Department: " + self.user.department, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['office_email'] = tk.Label(self.frame, text="Office Email: " + self.user.office_email, background='#00424d',font=('Arial', FONT_SIZE))
        self.views['emergency_contact'] = tk.Label(self.frame, text="Emergency Contact: " + self.user.emergency_contact, background='#00424d',font=('Arial', FONT_SIZE))

        rlim = 6
        clim = 4
        r, c = 1, 0
        for key, view in self.views.items():
            # print('dict values', view, key)
            view.grid(row=r, column=c, padx=20, pady=20)
            r += 1
            if r >= rlim:
                r = 1
                c += 1
    
    def go_back(self):
        from view_employees import ViewEmployeeEmp
        self.frame.destroy()
        #TODO Insert total data  in place of the user below
        self.app = ViewEmployeeEmp(self.master, employee_data=self.viewer)