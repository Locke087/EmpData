import csv
import os
from hashlib import sha256
from Employee import Employee
class CSVManager():
    def __init__(self) -> None:
        self.data = []
        self.path = "./employee.csv"
        if "employeetemp" in os.listdir('.'):
            self.path = './employeetemp.csv'
        self.data = self.get_rows()
    def get_rows(self,path=None):
        if not path:
            path = self.path
        data = []
        with open(path, 'r') as f:
            data = self.read_csv_rows(data, f)
        return data
    def read_csv_rows(self, data, f):
        reader = csv.reader(f)
        for i,row in enumerate(reader):
            if i==0:
                    continue
            emp = Employee(row)
            data.append(row)
        return data
    def add_employee(self, row):
        with open('./employeetemp.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(row)
        
    def archive_employee(self, emp: Employee):
        if emp.is_deactivated == 'n':
            emp.is_deactivated = 'y'
        else:
            emp.is_deactivated = 'n'
        emp.sync_row()
        self.edit_employee(emp.emp_id, emp)
    def edit_employee(self,prev_id: int, employee: Employee):
        allInfo = {}
        data = {}
        holder = []
       
        cat = ['EmpID','First','Last','Dept','Title','OfficeEmail','StreetNumber','Apt',
                'City','State','ZipCode','Country','OfficePhone','PayType','Wage','DateOfBirth',
                'SocialSecurity','StartDate','EndDate','BankInfo','PermissionLevel','EmergencyContact','Deactivated','Password','Route', 'Account']
        filename = './employee.csv'
 
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
                #We need the ID because it's a unique identifier
                #We use the previous one because an employer may decide to change
                #it for whatever reason
                if prev_id == db_id:
                    print('Found it ', name, db_name, db_id, id)
                    found = True
                    

                    index = 0
                    #allInfo.clear()
                    for j in employee.row:
                            allInfo[cat[index]] = j
                            index += 1
                            
                        
                    # print(*allInfo.items())
                    allInfo['Password'] = employee.password
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
            assert len(holder) > 0
            #print("wee ", holder)
            datestring = "temp"
            filename = f"employee{datestring}.csv"
            newfile = not os.path.exists(filename)
            if os.path.exists(filename):
                os.remove(filename)
            
            for data in holder:
                newfile = not os.path.exists(filename)
                with open(filename, 'a', newline='', encoding='utf-8') as fh:
                    csvwriter = csv.DictWriter(fh, fieldnames=cat)
                    if newfile:
                        csvwriter.writeheader()
                    csvwriter.writerow(data)  
                
        self.path = filename #update it to the temp
                         
    def search_emp_id(self, idx):
        '''Search for the employee by it's ID'''
        for row in self.data:
            #Skip it if it's the first row
            #because that contains the field names
            #not the actual data invovled
            emp = Employee(row)
            if idx == emp.emp_id:
                return emp
        return None

    def process_timecards(self, f):
        '''
        example format below. It's a list of floats of the hours they worked
        688997,5.0,6.8,8.0,7.7,6.6,5.2,7.1,4.0,7.5,7.6 
        939825,7.9,6.6,6.8,7.4,6.4,5.1,6.7,7.3,6.8,4.1 
        900100,5.1,6.8,5.0,6.6,7.7,5.1,7.5 
        969829,6.4,6.6,4.4,5.0,7.1,7.1,4.1,6.5 
        283809,7.2,5.8,7.6,5.3,6.4,4.6,6.4,5.0,7.5 
        224568,5.2,6.9,4.2,6.4,5.3,6.8,4.4 
        163695,4.8,7.2,7.2,4.7,5.1,7.3,7.5,4.5,4.6,7.0 
        454912,5.5,5.3,4.5,4.3,5.5 
        285767,7.5,6.5,6.3,4.7,6.8,7.1,6.6,6.6 
        674261,7.2,6.2,4.9,6.5,7.2,7.5,5.0,7.9 
        426824,7.4,6.5,5.7,8.0,6.9,7.5,6.5,7.5 
        934003,5.8,7.5,5.8,4.8,5.9,4.8,4.0,6.6,5.5,7.2 
        """
'''
        rows = self.read_csv_rows(f)
        print(rows)
    def proccess_receipts(self, f):
        '''
        Example format for commissioned employees:

        165966,241.34,146.55,237.48,96.37 
        379767,128.80,121.98,66.99,168.72 
        265154,240.20,83.69,52.31,77.29,142.12 
        160769,63.02,163.42,140.06,84.15
        """
        '''
        rows = self.read_csv_rows(f)

singleton = CSVManager()