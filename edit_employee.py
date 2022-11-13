import tkinter as tk
import os
import csv
from addEmployee import LabelData
from Employee import Employee
class EditEmployee():
    def __init__(self,master,user, employee: Employee) -> None:
        self.master = master
        self.master.title("Edit Employee Screen")
        self.master.geometry('1000x720')
        self.frame =tk.Frame(width=1000, height=720)
        self.frame.grid(row=0, column=0)
        self.user = user
        self.emp = employee
        self.back_button = tk.Button(self.frame, text='Back', command=self.go_back)
        self.back_button.grid(row=0, column=0, padx=0)
        self.title_view = tk.Label(self.frame, text=f"{self.emp.fname} {self.emp.lname}'s Profile", font=('Arial', 50))
        self.title_view.grid(row=0, column=1, padx=0, sticky=tk.W)
        #UI desing 
        #Have a list of entries. Simply submit the full entry with
        #the initial values of the employees is the value
        #Not needed: disable the etnry until a person clicks a button right next to the vlaue
        self.views: dict[tk.Label] = {}
        self.make_editable_entry('id', employee.emp_id)
        self.make_editable_entry('fname', employee.fname)
        self.make_editable_entry('lname', employee.lname)
        self.make_editable_entry('department', employee.department)
        self.make_editable_entry('title', employee.title)
        self.make_editable_entry('office_email', employee.office_email)
        self.make_editable_entry('street number', employee.address.street_address)
        self.make_editable_entry('apt number', employee.address.apt_no)
        self.make_editable_entry('city', employee.address.city)
        self.make_editable_entry('state', employee.address.state)
        self.make_editable_entry('zipcode', employee.address.zip_code)
        self.make_editable_entry('Country', employee.address.country)
        self.make_editable_entry('office_phone', employee.office_phone)
        self.make_editable_entry('Pay Type', employee.pay_type)
        self.make_editable_entry('wage', employee.wage)
        self.make_editable_entry('Date of Birth', employee.birthday)
        self.make_editable_entry('social_secuitry', employee.social_secuitry)
        self.make_editable_entry('start_date', employee.start_date)
        self.make_editable_entry('end_date', employee.end_date)
        self.make_editable_entry('bank_info', employee.bank_info)
        self.make_editable_entry('permission', employee.permission)
        self.make_editable_entry('emergency_contact', employee.emergency_contact)
        self.make_editable_entry('is_deactivated', employee.is_deactivated)
        

        rlim = 17
        clim = 4
        r, c = 1, 0
        for key, view in self.views.items():
            # print('dict values', view, key)
            view.grid(row=r, column=c, padx=30, pady=5)
            r += 1
            if r >= rlim:
                r = 1
                c += 1
        self.submit_btn = tk.Button(self.frame, text="💾 Save", command=self.submit, font=('Arial', 25))
        self.submit_btn.grid(row=15, column=2, rowspan=4, sticky=tk.NSEW)
    def submit(self):
        #TODO do form validation
        allInfo = {}
        data = {}
        holder = []
        employee = self.emp
        dataHolder = [employee.emp_id, employee.fname, employee.lname, employee.department, employee.title, employee.office_email
        ,employee.address.street_address, employee.address.apt_no, employee.address.city, employee.address.state, employee.address.zip_code
        , employee.address.country, employee.office_phone, employee.pay_type, employee.wage, employee.birthday, employee.social_secuitry,  
        employee.start_date,  employee.end_date, employee.bank_info, employee.permission,employee.emergency_contact , employee.is_deactivated,  "skip" ]
        cat = ['EmpID','First','Last','Dept','Title','OfficeEmail','StreetNumber','Apt',
                'City','State','ZipCode','Country','OfficePhone','PayType','Wage','DateOfBirth',
                'SocialSecurity','StartDate','EndDate','BankInfo','PermissionLevel','EmergencyContact','Deactivated','Password']
        for key, value in self.views.items():
            is_label = key[-6:] == '_label'
            found = False
            if not is_label:
                print(key, value.get())
                #TODO do the form validation with a dictionary to look up how
                #TODO should be implemented in the employee class
                filename = './employee.csv'
                if os.path.exists('./employeetemp.csv'):
                    filename = './employeetemp.csv'
                with open(filename) as file:
                    reader = csv.reader(file)  
                    for i,row in enumerate(reader):
                        if i == 0:
                            continue
                        id = employee.emp_id
                        name = employee.fname
                       
                        db_id = row[0]
                        db_name = row[1]
                        db_name = db_name.strip()
                        #print("here")
                        if name == db_name and id == db_id:
                            print('Found it ', name, db_name, db_id, id)
                            found = True
                           
                        #move on to the next window
                            fullstring = ""
                            index = 0
                            #allInfo.clear()
                            for keys, j in self.views.items():
                                 is_label = keys[-6:] == '_label'
                                 if not is_label:
                                    allInfo[cat[index]] = j.get()
                                    dataHolder[index] = j.get()
                                    index += 1
                                
                           # print(*allInfo.items())
                            allInfo['Password'] = employee.row[-1]
                            holder.append(allInfo.copy())
                            
                            allInfo.clear()

                           
                        else:
                            index = 0
                            for j in row:
                                allInfo[cat[index]] = j
                                index += 1
                            #print(*allInfo.items())     
                            holder.append(allInfo.copy())
                            allInfo.clear()   
                        
                if found:
                    print("wee ", holder)
                    datestring = "temp"
                    filename = f"employee{datestring}.csv"
                    newfile = not os.path.exists(filename)
                    if os.path.exists(filename):
                        os.remove(filename)
                 
                    for data in holder:
                        newfile = not os.path.exists(filename)
                        with open(filename, 'a') as fh:
                            csvwriter = csv.DictWriter(fh, fieldnames=data.keys())
                            if newfile:
                                csvwriter.writeheader()
                            csvwriter.writerow(data)  
                      
                 
                    break                            
        
        self.go_back()
    def make_editable_entry(self, key, value):
        self.views[key + '_label'] = tk.Label(self.frame, text=key)
        self.views[key] = tk.Entry(self.frame)
        self.views[key].insert(0, value)
    def go_back(self):
        from view_employees import ViewEmployeeEmp, ViewEmployeeAdmin
        self.frame.destroy()
        #TODO Insert total data  in place of the user below
        if self.user.permission == 'admin':
            self.app = ViewEmployeeAdmin(self.master, employee_data=self.user)
        else:
            self.app = ViewEmployeeEmp(self.master, employee_data=self.user)
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
    frame = EditEmployee(window, employee)
    window.mainloop()