import tkinter as tk
import csv
from Employee import Employee
from hashlib import sha256
from shutil import copy
import os
class AddEmployee():
    def __init__(self,master, employee: Employee) -> None:
        self.master = master
        self.master.title("Add Employee Screen")
        self.master.resizable(width=False, height=False)
        self.master.geometry('1000x720')
        self.frame =tk.Frame(width=1000, height=720)
        self.frame.grid(row=0, column=0)
        self.user = employee
        self.back_button = tk.Button(self.frame, text='Back', command=self.go_back)
        self.back_button.grid(row=0, column=0, padx=0)
        self.title_view = tk.Label(self.frame, text=f"Add Employee", font=('Arial', 50))
        self.title_view.grid(row=0, column=1, padx=0, sticky=tk.W+tk.E)
        self.title_view = tk.Label(self.frame, text=f"""Please fill out all the fields below.""", font=('Arial', 15))
        self.title_view.grid(row=1, column=1, padx=0, sticky=tk.W+tk.E, pady=10)
        #UI desing 
        #Have a list of entries. Simply submit the full entry with
        #the initial values of the employees is the value
        #Not needed: disable the etnry until a person clicks a button right next to the vlaue
        self.views: dict[tk.Label] = {}
        self.make_editable_entry('Employee ID', employee.emp_id)
        self.make_editable_entry('First Name', employee.fname)
        self.make_editable_entry('Last Name', employee.lname)
        self.make_editable_entry('department', employee.department)
        self.make_editable_entry('title', employee.title)
        self.make_editable_entry('office_email', employee.office_email)

        self.make_editable_entry('street number', employee.address.street_address)
        self.make_editable_entry('apt number', employee.address.apt_no)
        self.make_editable_entry('city', employee.address.city)
        self.make_editable_entry('state', employee.address.state)
        self.make_editable_entry('zipcode', employee.address.zip_code)
        self.make_editable_entry('country', employee.address.country)
        
        self.make_editable_entry('office_phone', employee.office_phone)
        self.make_editable_entry('Paytype(Hourly/Salary)')
        self.make_editable_entry('Wage', employee.wage)
        self.make_editable_entry('Date of Birth', employee.birthday)
        self.make_editable_entry('social_secuitry', employee.social_secuitry)
        self.make_editable_entry('start_date', employee.start_date)
        self.make_editable_entry('end_date', employee.end_date)
        self.make_editable_entry('bank_info', employee.bank_info)
        self.make_editable_entry('permission', employee.permission)
        self.make_editable_entry('emergency_contact', employee.emergency_contact)
        self.make_editable_entry('is_deactivated(y/n)', employee.is_deactivated)
        self.make_editable_entry('Password')
        rlim = 18
        clim = 4
        r, c = 2, 0
        for key, view in self.views.items():
            # print('dict values', view, key)
            view.grid(row=r, column=c, padx=40, pady=5)
            r += 1
            if r >= rlim:
                r = 2
                c += 1
        self.submit_btn = tk.Button(self.frame, text="💾Save", command=self.submit, font=('Arial', 25))
        self.submit_btn.grid(row=18, column=2, rowspan=4, sticky=tk.NSEW)
    def submit(self):
        #TODO do form validation
        row = []
        if not os.path.exists('./employeetemp.csv'):
            copy('./employee.csv', 'employeetemp.csv')
        for key, value in self.views.items():
            is_label = key[-6:] == '_label'
            if not is_label:
                #TODO do the form validation with a dictionary to look up how
                #TODO should be implemented in the employee class
                #TODO add the employee to the csv file
                #Hasing the passwrod
                
                if key == 'Password':
                    hasher = sha256()
                    hasher.update(value.get().encode('utf-8'))
                    hash_pass= hasher.hexdigest()
                    row.append(hash_pass)
                else:
                    row.append(value.get())
        with open('./employeetemp.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(row)
        
        self.go_back()
    def make_editable_entry(self, key, value=None):
        self.views[key + '_label'] = tk.Label(self.frame, text=key)
        self.views[key] = tk.Entry(self.frame)
    def go_back(self):
        from view_employees import ViewEmployeeAdmin
        self.frame.destroy()
        #TODO Insert total data  in place of the user below
        self.app = ViewEmployeeAdmin(self.master, employee_data=self.user)
if __name__ == '__main__':
    window = tk.Tk()
    emp_data = None
    with open('./employee.csv') as file:
            reader = csv.reader(file)
            for i,row in enumerate(reader):
                if i == 0:
                    continue
                else:
                    emp_data = row
                    break
    employee = Employee()
    employee.row_init(emp_data)
    frame = AddEmployee(window, employee)
    window.mainloop()