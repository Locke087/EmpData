from Employee import Employee
import tkinter as tk
import csv
class ViewEmployee():
    def __init__(self,master, employee_data) -> None:
        self.master = master
        self.master.title("View Employee Screen")
        self.master.geometry('1000x720')

        #TODO fix the alignment of the UI
        self.frame =tk.Frame()
        # In center of screen, create welcome message, username and password input boxes with username and password headings
        self.user = Employee()
        self.user.row_init(employee_data)
        print(self.user.fname)
        self.employees: list[Employee] = []
        with open('./employee.csv') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                emp = Employee()
                emp.row_init(row)
                self.employees.append(emp)
        self.frame.grid()
        self.usertitle = tk.Label(self.frame, text=f'Hello, {self.user.fname} {self.user.lname}', font=('Arial', 35), anchor=tk.W)
        self.usertitle.grid(row=0, column=0, padx=40)
        self.perm = tk.Label(self.frame, text=f'Permission:{self.user.permission.upper()}', font=('Arial', 25), anchor=tk.E)
        self.perm.grid(row=1,column=0,pady=10, padx=40)

        #TODO fix up the code to include the search bar 
        #TODO and make it so it updates the listbox eachtime we update the value
        #TODO which is easily done by clearing the listbox and populating the values
        #TODO according to the value
        #TODO Add a entry on right below the title of the list of employees
        self.emp_title = tk.Label(self.master, text="Employee list", font=('Arial', 25))
        self.emp_title.grid(row=0, column=1, columnspan=2)
        self.scroll = tk.Scrollbar(self.master)
        self.scroll.grid(row=1, column=3, sticky=tk.NS)
        self.list_box = tk.Listbox(self.master, width= 50, height=30,yscrollcommand=self.scroll.set)
        for employee in self.employees:
            self.list_box.insert(tk.END, f"{employee.fname} {employee.lname}")
        self.list_box.grid(row=1, column=2)
        self.go_to_emp = tk.Button(self.master, text="Go to employee", command=self.goEmp, font=('Arial', 15))
        self.go_to_emp.grid(row=2, column=1, columnspan=2, pady=20)
        self.scroll.config(command=self.list_box.yview)
    def goEmp(self):
        pass
        