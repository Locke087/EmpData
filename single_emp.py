from Employee import Employee
import tkinter as tk
import csv

class SingleEmployee():
    def __init__(self,master, employee) -> None:
        self.master = master
        self.master.title("View Employee Screen")
        self.master.geometry('1000x720')

        #TODO Binding is a tiny bit buggy when clicking. Maybe removing the feature to begin with?
        #TODO actually document this document
        self.frame =tk.Frame(width=1000, height=720)
        self.frame.grid(row=0, column=0)
        # In center of screen, create welcome message, username and password input boxes with username and password headings
        self.user = employee
        self.back_button = tk.Button(self.frame, text='Back', command=self.go_back)
        self.back_button.grid(row=0, column=0, padx=0)
        self.title_view = tk.Label(self.frame, text=f"{self.user.fname} {self.user.lname}'s Profile", font=('Arial', 50))
        self.title_view.grid(row=0, column=1, padx=0, sticky=tk.W)
        self.views: dict[tk.Label] = {}
        self.views['id'] = tk.Label(self.frame, text=self.user.emp_id)
        self.views['fname'] = tk.Label(self.frame, text=self.user.fname)
        self.views['lname'] = tk.Label(self.frame, text=self.user.lname)
        self.views['address'] = tk.Label(self.frame, text=str(self.user.address))
        self.views['office_phone'] = tk.Label(self.frame, text=self.user.office_phone)
        self.views['pay_type'] = tk.Label(self.frame, text=self.user.pay_type)
        self.views['wage'] = tk.Label(self.frame, text=self.user.wage)
        self.views['birthday'] = tk.Label(self.frame, text=self.user.birthday)
        self.views['permission'] = tk.Label(self.frame, text=self.user.permission)
        self.views['title'] = tk.Label(self.frame, text=self.user.title)
        self.views['department'] = tk.Label(self.frame, text=self.user.department)
        self.views['office_email'] = tk.Label(self.frame, text=self.user.office_email)
        self.views['emergency_contact'] = tk.Label(self.frame, text=self.user.emergency_contact)
        self.views['start_date'] = tk.Label(self.frame, text=self.user.start_date)
        self.views['end_date'] = tk.Label(self.frame, text=self.user.end_date)
        self.views['bank_info'] = tk.Label(self.frame, text=self.user.bank_info)
        self.views['is_deactivated'] = tk.Label(self.frame, text=self.user.is_deactivated)
        self.views['social_secuitry'] = tk.Label(self.frame, text= "Social Secuitry: " + self.user.social_secuitry)

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
        from view_employees import ViewEmployee
        self.frame.destroy()
        #TODO Insert total data  in place of the user below
        self.app = ViewEmployee(self.master, employee_data=self.user)
        