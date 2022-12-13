import tkinter as tk
import tkinter.messagebox as messagebox
import csv
from Employee import Employee
from hashlib import sha256
from shutil import copy
import os
import csvalchemy
from hover_button import HoverButton
class AddEmployee():
    def __init__(self,master, employee: Employee, is_test_mode=False) -> None:
        self.master = master
        self.test_mode = is_test_mode
        self.master.title("Add Employee Screen")
        self.master.resizable(width=False, height=False)
        self.master.geometry('1200x900')
        self.master['bg'] = '#007385'
        self.frame =tk.Frame(width=1200, height=900, background='#007385')
        self.frame.grid(row=0, column=0)
        self.user = employee
        self.back_button = HoverButton('Back', 'Go back to previous screen', self.go_back, self.frame)
        self.back_button.grid(row=0, column=0, padx=0, pady=(10,0))
        self.title_view = tk.Label(self.frame, text=f"Add Employee", font=('Arial', 50), background='#007385')
        self.title_view.grid(row=0, column=1, padx=0, sticky=tk.W+tk.E)
        self.title_view = tk.Label(self.frame, text="Please fill out all the fields below.", font=('Arial', 15), background='#007385')
        self.title_view.grid(row=1, column=1, padx=0, sticky=tk.W+tk.E, pady=10)
        #UI desing 
        #Have a list of entries. Simply submit the full entry with
        #the initial values of the employees is the value
        #Not needed: disable the etnry until a person clicks a button right next to the vlaue
        self.views: dict[tk.Label] = {}
        self.make_editable_entry('ID')
        self.make_editable_entry('First Name')
        self.make_editable_entry('Last Name')
        self.make_editable_entry('Department')
        self.make_editable_entry('Title')
        self.make_editable_entry('Office Email')
        self.make_editable_entry('Street Number')
        self.make_editable_entry('Apt Number')
        self.make_editable_entry('City')
        self.state_val = tk.StringVar()
        self.state_val.set('Utah')
        state_names = ["I am not American", "Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California",
         "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia",
          "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana",
           "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi",
            "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey",
             "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
              "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
               "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
        self.make_editable_entry('State', is_dropdown=True, options=state_names, clicked=self.state_val)
        self.make_editable_entry('Zipcode')
        self.make_editable_entry('Country')
        self.make_editable_entry('Office Phone (xxx-xxx-xxxx)')
        self.pay_type_val = tk.StringVar()
        self.pay_type_val.set('Hourly')
        self.make_editable_entry('Pay Type',is_dropdown=True, options=['Hourly', 'Commission', 'Salary'], clicked=self.pay_type_val)
        self.make_editable_entry('Wage(Put 0 if commission)')
        self.make_editable_entry('Date of Birth (mm/dd/yyyy)')
        self.make_editable_entry('Social Securitry (xxx-xx-xxxx)')
        self.make_editable_entry('Start Date (mm/dd/yyyy)')
        self.make_editable_entry('End Date (mm/dd/yyyy)')
        self.bank_info_val = tk.StringVar()
        self.bank_info_val.set('Direct Method')
        self.make_editable_entry('Bank Info', is_dropdown=True, options=['Direct Method', 'Mail Method'], clicked=self.bank_info_val)
        self.permission_val = tk.StringVar()
        self.permission_val.set('Employee')
        self.make_editable_entry('Permission', is_dropdown=True, options=['Admin', 'Employee'], clicked=self.permission_val)
        self.make_editable_entry('Emergency Contact')
        self.active_value = tk.StringVar()
        self.active_value.set('No')
        self.make_editable_entry('Is Deactivated', is_dropdown=True, options=['Yes', 'No'], clicked=self.active_value)
        self.make_editable_entry('Password')
        self.make_editable_entry('Route')
        self.make_editable_entry('Account Number')
        

        rlim = 21
        clim = 4
        r, c = 3, 0
        for key, view in self.views.items():
            # print('dict values', view, key)
            view.grid(row=r, column=c, padx=60, pady=5)
            r += 1
            if r >= rlim:
                r = 3
                c += 1
        self.submit_btn = HoverButton("💾 Save", "Click here to save the entry", self.submit, self.frame,font=('Arial', 50))
        self.submit_btn.grid(row=19, column=2, rowspan=2, sticky=tk.NSEW)
    def submit(self):
        #TODO do form validation
        row = []
        keys = []
        dropdowns = ['Bank Info', 'Is Deactivated', 'State', 'Pay Type', 'Permission']
        if not os.path.exists('./employeetemp.csv'):
            copy('./employee.csv', 'employeetemp.csv')
        for key, value in self.views.items():
            is_label = key[-6:] == '_label'
            if not is_label:
                #TODO do the form validation with a dictionary to look up how
                #TODO should be implemented in the employee class
                #TODO add the employee to the csv file
                #Hasing the passwrod
                keys.append(key)
                if key == 'Password':
                    hasher = sha256()
                    hasher.update(value.get().encode('utf-8'))
                    hash_pass= hasher.hexdigest()
                    row.append(hash_pass)
                else:
                    if key == dropdowns[0]:
                        row.append(self.bank_info_val.get())
                    elif key == dropdowns[1]:
                        row.append(self.active_value.get())
                    elif key == dropdowns[2]:
                        row.append(self.state_val.get())
                    elif key == dropdowns[3]:
                        row.append(self.pay_type_val.get())
                    elif key == dropdowns[4]:
                        row.append(self.permission_val.get())
                    else:
                        row.append(value.get())
        if self.test_mode:
            #Asserts are only for testing
            assert len(row) > 0
            assert row[0] != ""
            assert row[1] != ""
            assert row[20] != ""
            assert row[22] != ""
            assert row[23] != ""
        error = csvalchemy.singleton.validate_row(keys,row)
        if error[0]:
            #It returns boolean how things went
            csvalchemy.singleton.add_employee(row)
            self.go_back()
        else:
            messagebox.showerror(error[1][0], error[1][1])
    def make_editable_entry(self, key, is_dropdown=False, options=None, clicked=None):
        self.views[key + '_label'] = tk.Label(self.frame, text=key, font=('Arial', 25), background='#007385')
        if is_dropdown:
            self.views[key] = tk.OptionMenu(self.frame,clicked, *options)
        else:
            self.views[key] = tk.Entry(self.frame, background="silver")
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
    frame = AddEmployee(window, employee, is_test_mode=False)
    window.mainloop()