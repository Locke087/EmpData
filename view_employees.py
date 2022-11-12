from Employee import Employee
import tkinter as tk
import csv
from single_emp import SingleEmployee
from edit_employee import EditEmployee
from add_employee import AddEmployee
import tkinter.messagebox as messagebox

class ViewEmployee():
    def __init__(self,master, employee_data) -> None:
        self.master = master
        self.master.title("View Employee Screen")
        self.master.geometry('1000x720')

        #TODO actually document this document
        #TODO Make the thing read once only or use asyncrounous programming
        #TODO (cont) to make the page load more seemless
        self.frame =tk.Frame(width=1000, height=720)
        self.frame.grid(row=0, column=0)
        # In center of screen, create welcome message, username and password input boxes with username and password headings
        self.user: Employee = employee_data
   
        self.employees: list[Employee] = []
        with open('./employee.csv') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                emp = Employee()
                emp.row_init(row)
                self.employees.append(emp)
        
        self.usertitle = tk.Label(self.frame, text=f'Hello, {self.user.fname} {self.user.lname}', font=('Arial', 35), anchor=tk.W)
        self.usertitle.grid(row=0, column=0, padx=40)
        self.perm = tk.Label(self.frame, text=f'Permission:{self.user.permission.upper()}', font=('Arial', 25), anchor=tk.E)
        self.perm.grid(row=1,column=0,pady=10, padx=40)

        self.edit_emp_btn = tk.Button(self.frame, text="Edit Employee", command=self.goEdit, font=('Arial', 15))
        self.edit_emp_btn.grid(row=3, column=0,pady=10)
        self.edit_emp_btn = tk.Button(self.frame, text="Add Employee", command=self.goAdd, font=('Arial', 15))
        self.edit_emp_btn.grid(row=4, column=0, pady=10)
        self.edit_emp_btn = tk.Button(self.frame, text="Remove Employee", command=self.goRemove, font=('Arial', 15))
        self.edit_emp_btn.grid(row=5, column=0, pady=10)

        self.emp_title = tk.Label(self.frame, text="Employee list", font=('Arial', 50))
        self.emp_title.grid(row=0, column=1, columnspan=3)


        self.emp_title = tk.Label(self.frame, text="🔍", font=('Arial', 25))
        self.emp_title.grid(row=1, column=1, padx=0)
        self.search_var = tk.StringVar()#search value to be stored in here
        self.search_entry = tk.Entry(self.frame, textvariable=self.search_var, width=30, font=('Arial', 25))
        self.search_entry.grid(row=1, column=2, padx=0, sticky=tk.NSEW)
    
        
        self.scroll = tk.Scrollbar(self.frame)
        self.scroll.grid(row=2, column=3, sticky=tk.NS)

        self.list_box = tk.Listbox(self.frame, height=15,yscrollcommand=self.scroll.set, font=('Arial', 25))
        for employee in self.employees:
            self.list_box.insert(tk.END, f"{employee.fname} {employee.lname}")
        self.list_box.grid(row=2, column=1, columnspan=2, sticky=(tk.W + tk.E))

        

        self.go_to_emp = tk.Button(self.frame, text="View employee", command=self.goEmp, font=('Arial', 15))
        self.go_to_emp.grid(row=3, column=1, columnspan=2, pady=10)
        self.scroll.config(command=self.list_box.yview)

        #Binding for events such as when the listbox element is selected and when we type in the search box
        self.list_box.bind('<<ListboxSelect>>', self.fillout)
        self.search_entry.bind("<KeyRelease>", self.update_search)

    def fillout(self,event):
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, self.list_box.get(tk.ANCHOR))
    def update_search(self, event):
        data = None
        #removing whitespace, which is annoying to deal with
        typed = self.search_var.get().replace(' ', '')
        if typed == '':
            #If there nothing but spaces or empty box, then just put everything back
            data = self.employees
        else:
            #TODO Chagne this into a search funciton in the CSV writer class
            #Otherwise do a simple search
            data = []
            for item in self.employees:
                comb = f"{item.emp_id}{item.fname}{item.lname}"
                is_ok = typed.lower() in item.fname.lower() or typed.lower() in item.lname.lower() \
                        or typed.lower() in comb.lower() or typed.lower() in comb.lower()
                if is_ok:
                    data.append(item)
        #clear the listbox first
        self.list_box.delete(0, tk.END)
        #Enter in the filtered results
        for emp in data:
            self.list_box.insert(tk.END, f"{emp.fname} {emp.lname}")
        
    def goEdit(self):
        employee = None
        typed = self.list_box.get(tk.ANCHOR).replace(' ', '')
        for item in self.employees:
            comb = f"{item.emp_id}{item.fname}{item.lname}"
            is_ok = typed.lower() in item.fname.lower() or typed.lower() in item.lname.lower() \
                    or typed.lower() in comb.lower() or typed.lower() in comb.lower()
            if is_ok:
                employee = item
                break
        self.frame.destroy()
        self.app = EditEmployee(self.master, employee)
    def goRemove(self):
        selected = self.list_box.get(tk.ANCHOR)
        if selected.replace(' ', '') != '':
            is_yes = messagebox.askyesno('Delete the employee?', 'Are you sure you want to delete the employee')
            if is_yes:
                self.list_box.delete(tk.ANCHOR)
            #TODO remove the thing actually from a the database
    def goAdd(self):
        if self.user.permission.lower().replace(' ', '') == 'admin':
            self.frame.destroy()
            self.app = AddEmployee(self.master, self.user)
        else:
            messagebox.showerror(title="Access Denied", message="You must be an admin in order to access this")
    def goEmp(self):
        #move on to the next window
        #1. Destory the current window
        
        #Must be initialized to variable or it will get dumped by the garbage collector
        #TODO Replace the employee with the searching for the user below
        #TODO which will have to perform a quick search
        employee = None
        typed = self.list_box.get(tk.ANCHOR).replace(' ', '')
        for item in self.employees:
            comb = f"{item.emp_id}{item.fname}{item.lname}"
            is_ok = typed.lower() in item.fname.lower() or typed.lower() in item.lname.lower() \
                    or typed.lower() in comb.lower() or typed.lower() in comb.lower()
            if is_ok:
                employee = item
                break
        self.frame.destroy()
        self.app = SingleEmployee(self.master, employee)
        