from Employee import Employee
import tkinter as tk
import csv
class ViewEmployee():
    def __init__(self,master, employee_data) -> None:
        self.master = master
        self.master.title("View Employee Screen")
        self.master.geometry('1000x720')

        #TODO Binding is a tiny bit buggy when clicking. Maybe removing the feature to begin with?
        #TODO actually document this document
        self.frame =tk.Frame(width=1000, height=720)
        self.frame.grid(row=0, column=0)
        # In center of screen, create welcome message, username and password input boxes with username and password headings
        self.user = Employee()
        self.user.row_init(employee_data)
   
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

        
        self.emp_title = tk.Label(self.frame, text="Employee list", font=('Arial', 25))
        self.emp_title.grid(row=0, column=1)

        self.search_var = tk.StringVar()#search value to be stored in here
        self.search_entry = tk.Entry(self.frame, textvariable=self.search_var, width=30, font=('Arial', 25))
        self.search_entry.grid(row=1, column=1)
    
        
        self.scroll = tk.Scrollbar(self.frame)
        self.scroll.grid(row=2, column=2, sticky=tk.NS)

        self.list_box = tk.Listbox(self.frame, width= 50, height=20,yscrollcommand=self.scroll.set)
        for employee in self.employees:
            self.list_box.insert(tk.END, f"{employee.fname} {employee.lname}")
        self.list_box.grid(row=2, column=1)

        

        self.go_to_emp = tk.Button(self.frame, text="Go to employee", command=self.goEmp, font=('Arial', 15))
        self.go_to_emp.grid(row=3, column=1, columnspan=2, pady=20)
        self.scroll.config(command=self.list_box.yview)

        #Binding for events such as when the listbox element is selected and when we type in the search box
        self.list_box.bind('<<ListboxSelect>>', self.fillout)
        self.search_entry.bind("<KeyRelease>", self.update_search)

    def fillout(self,event):
        self.search_entry.delete(0, tk.END)
        self.search_entry.insert(0, self.list_box.get(tk.ACTIVE))
    def update_search(self, event):
        data = None
        #removing whitespace, which is annoying to deal with
        typed = self.search_var.get().replace(' ', '')
        if typed == '':
            #If there nothing but spaces or empty box, then just put everything back
            data = self.employees
        else:
            #Otherwise do a simple search
            data = []
            for item in self.employees:
                comb = f"{item.fname}{item.lname}"
                is_ok = typed.lower() in item.fname.lower() or typed.lower() in item.lname.lower() \
                        or typed.lower() in comb.lower()
                if is_ok:
                    data.append(item)
        #clear the listbox first
        self.list_box.delete(0, tk.END)
        #Enter in the filtered results
        for emp in data:
            self.list_box.insert(tk.END, f"{emp.fname} {emp.lname}")
        
    
    def goEmp(self):
        pass
        