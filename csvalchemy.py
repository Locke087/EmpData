import csv
import os
from hashlib import sha256
from Employee import Employee
import re
class CSVManager():
    def __init__(self) -> None:
        self.data = []
        self.path = "./employee.csv"

        if "employeetemp.csv" in os.listdir('.'):
            self.path = './employeetemp.csv'

        self.headers = ['EmpID','First','Last','Dept','Title','OfficeEmail','StreetNumber','Apt',
                'City','State','ZipCode','Country','OfficePhone','PayType','Wage','DateOfBirth',
                'SocialSecurity','StartDate','EndDate','BankInfo','PermissionLevel','EmergencyContact','Deactivated','Password','Route', 'Account']
        self.data = self.get_rows()
    def get_rows(self,path=None):
        if not path:
            path = self.path
        data = []
        with open(path, 'r') as f:
            data = self.read_csv_rows(data, f)
        return data
    def read_csv_rows(self, data, f, isSkipFirstRow=True):
        reader = csv.reader(f)
        for i,row in enumerate(reader):
            if i==0 and isSkipFirstRow:
                    continue
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
        found = False
        with open(self.path) as file:
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
                            allInfo[self.headers[index]] = j
                            index += 1
                            
                        
                    # print(*allInfo.items())
                    allInfo['Password'] = employee.password
                    holder.append(allInfo.copy())
                    
                    allInfo.clear()

                    
                else:
                    index = 0
                    for j in row:
                        allInfo[self.headers[index]] = j
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
                    csvwriter = csv.DictWriter(fh, fieldnames=self.headers)
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
            if int(idx)== int(emp.emp_id):
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
        #I made it to allow salary employees as well, but it's assumed to be good practive for them to be included in seperate files
        rows =[]
        rows = self.read_csv_rows(rows, f, isSkipFirstRow=False)
        totals = []
        emps = []
        for row in rows:
            
            emp = self.search_emp_id(row[0])
            if not emp:
                raise Exception(f'Employee in timecard does not exist. Attempted ID: {row[0]} but it does not exist. Make sure you have an id of an employee who exists')
            if not emp.pay_type == 'Hourly' or emp.pay_type == 'Salary':
                raise Exception(f'Employee with ID:{emp.emp_id} is not hourly or salary. It is currently {emp.pay_type}. Either change the employee ID or fix the ID to the correct employee.')
            hours = sum([float(x) for x in row[1:]])
            pay_total = float(emp.wage) * hours
            print(pay_total)
            emps.append(emp)
            totals.append(pay_total)
        return (emps, totals)
    def proccess_receipts(self, f):
        '''
        Example format for commissioned employees:

        165966,241.34,146.55,237.48,96.37 
        379767,128.80,121.98,66.99,168.72 
        265154,240.20,83.69,52.31,77.29,142.12 
        160769,63.02,163.42,140.06,84.15
        """

        14,Sean,Green, Green Pixies,Magic Teacher, john.doe@gmail.com, 123 abc street,, Spanish Fork, Utah, 14323,USA, 801-123-1234,Commission,0,1/1/2000,123-123-123, 1/1/2022,12/1/2022,mm,admin,Bazinga : 123-123-1234,n,d04b98f48e8f8bcc15c6ae5ac050801cd6dcfd428fb5f9e65c4e16e7807340fa,36644938-8,244269-0000
15,Sean,Smith, Green Pixies,Magic Teacher, john.doe@gmail.com, 123 abc street,, Spanish Fork, Utah, 14323,USA, 801-123-1234,Commission,0,1/1/2000,123-123-123, 1/1/2022,12/1/2022,dm,admin,Bazinga : 123-123-1234,n,d04b98f48e8f8bcc15c6ae5ac050801cd6dcfd428fb5f9e65c4e16e7807340fa,15300058-1,828625-2906
16,Sean,Scholz, Green Pixies,Magic Teacher, john.doe@gmail.com, 123 abc street,, Spanish Fork, Utah, 14323,USA, 801-123-1234,Commission,0,1/1/2000,123-123-123, 1/1/2022,12/1/2022,mm,admin,Bazinga : 123-123-1234,n,d04b98f48e8f8bcc15c6ae5ac050801cd6dcfd428fb5f9e65c4e16e7807340fa,44553589-3,785957-2104
17,Sean,Evil, Green Pixies,Magic Teacher, john.doe@gmail.com, 123 abc street,, Spanish Fork, Utah, 14323,USA, 801-123-1234,Commission,0,1/1/2000,123-123-123, 1/1/2022,12/1/2022,dm,admin,Bazinga : 123-123-1234,n,d04b98f48e8f8bcc15c6ae5ac050801cd6dcfd428fb5f9e65c4e16e7807340fa,21038669-6,654904-8491
18,Sean,Chao, Green Pixies,Magic Teacher, john.doe@gmail.com, 123 abc street,, Spanish Fork, Utah, 14323,USA, 801-123-1234,Commission,0,1/1/2000,123-123-123, 1/1/2022,12/1/2022,mm,admin,Bazinga : 123-123-1234,n,d04b98f48e8f8bcc15c6ae5ac050801cd6dcfd428fb5f9e65c4e16e7807340fa,30417353-A,465794-1234
19,Sean,Chin, Green Pixies,Magic Teacher, john.doe@gmail.com, 123 abc street,, Spanish Fork, Utah, 14323,USA, 801-123-1234,Commission,0,1/1/2000,123-123-123, 1/1/2022,12/1/2022,dm,admin,Bazinga : 123-123-1234,n,d04b98f48e8f8bcc15c6ae5ac050801cd6dcfd428fb5f9e65c4e16e7807340fa,30417353-B,567794-5678
20,Sean,Morris, Green Pixies,Magic Teacher, john.doe@gmail.com, 123 abc street,, Spanish Fork, Utah, 14323,USA, 801-123-1234,Commission,0,1/1/2000,123-123-123, 1/1/2022,12/1/2022,mm,admin,Bazinga : 123-123-1234,n,d04b98f48e8f8bcc15c6ae5ac050801cd6dcfd428fb5f9e65c4e16e7807340fa,30417353-C,465794-9012
23,Sean,Muir, Green Pixies,Magic Teacher, john.doe@gmail.com, 123 abc street,, Spanish Fork, Utah, 14323,USA, 801-123-1234,Commission,
        '''
        rows =[]
        rows = self.read_csv_rows(rows, f, isSkipFirstRow=False)
        totals = []
        emps = []
        for row in rows:       
            emp = self.search_emp_id(row[0])
            #TODO turn exceptions into error boxes
            if not emp:
                raise Exception(f'Employee in timecard does not exist. Attempted ID: {row[0]} but it does not exist. Make sure you have an id of an employee who exists')
            if not emp.pay_type == 'Commission':
                raise Exception(f'Employee with ID:{emp.emp_id} is not commission. It is currently {emp.pay_type}. Either change the employee ID or fix the ID to the correct employee.')
            pay_total = sum([float(x) for x in row[1:]])
            print(pay_total)
            emps.append(emp)
            totals.append(pay_total)
        return (emps, totals)
    def info_report(self, f, isActive=True, isDeactive=True):
        writer = csv.writer(f)
        writer.writerow(self.headers)
        for row in self.data:
            emp: Employee = Employee(row)
            if emp.is_deactivated == 'n' and isActive:
                writer.writerow(row)
            if emp.is_deactivated == 'y' and isDeactive:
                writer.writerow(row)
    def validate_row(self, keys, row, is_edit=False):
        # 'State','Pay Type',
        custom_vals = {'ID': self.val_id,'Start Date (mm/dd/yyyy)':self.val_date,'End Date (mm/dd/yyyy)':self.val_date, 
                      'Date of Birth (mm/dd/yyyy)':self.val_date, 'Bank Info':self.val_bank,'Bank Info':self.val_info,
                      'Permission':self.val_permission, 'Is Deactivated':self.val_active, 'Route':self.val_route, 'Account Number':self.val_acct
                      }
        mutate_custom_vals = ['Permission', 'Is Deactivated', 'Bank Info']
        optional_vals = {'Apt Number', 'Emergency Contact'}
        self.reg_refs = {}
        #On some of the entries run a regex expression then the custome checks. This
        #Is just to validate the forms then the database validates it.
        self.reg_refs['ID'] = re.compile(r'^[0-9]{1,}$') #Unique
        self.reg_refs['First Name'] = re.compile(r'^[a-zA-Z]{1,}$')
        self.reg_refs['Last Name'] = re.compile(r'^[a-zA-Z]{1,}$')
        self.reg_refs['Department'] = re.compile(r'^.+$')
        self.reg_refs['Title'] = re.compile(r'^.+$')
        self.reg_refs['Office Email'] = re.compile(r'[\w]*@[\w]*\.{1}(com|gov|edu|io|net){1}$')
        self.reg_refs['Street Number'] = re.compile(r'\d+(\s\w.*)?')
        self.reg_refs['Apt Number'] = re.compile(r'(^#\d\d*$)|(^\d\d*$)|(^\s*$)')
        self.reg_refs['City'] = re.compile(r'[a-zA-Z]{1,}') #Some of these can be done with options so we may not need regex
        self.reg_refs['State'] = None #Custom validation
        self.reg_refs['Zipcode'] = re.compile(r'^[0-9]{5}$')
        self.reg_refs['Country'] = re.compile(r'[a-zA-Z]{1,}')
        self.reg_refs['Office Phone (xxx-xxx-xxxx)'] = re.compile(r'^([0-9]{1}\s?)?(\d{3}|\(\d{3}\))[\s\-]?\d{3}[\s\-]?\d{4}$')
        self.reg_refs['Pay Type'] = None #Will be option dropdown
        self.reg_refs['Wage(Put 0 if commission)'] = re.compile(r'^\d{1,}(\.\d+)?$') #Remove commas before parsing
        self.reg_refs['Date of Birth (mm/dd/yyyy)'] = re.compile(r'^\d\d?\/\d\d?\/\d\d\d\d$')
        self.reg_refs['Social Securitry (xxx-xx-xxxx)'] = re.compile(r'^\d{3}\-\d{2}\-\d{4}$') #Would nomrally be unique, but for project purposes ignore this. Remove - and format it
        self.reg_refs['Start Date (mm/dd/yyyy)'] = re.compile(r'^\d\d?\/\d\d?\/\d\d\d\d$') #Add a custom follow up where it asks if the user wants it to be the current date
        self.reg_refs['End Date (mm/dd/yyyy)'] = re.compile(r'^\d\d?\/\d\d?\/\d\d\d\d$')#Add a custom follow up where it asks if the user wants it to be the current date
        self.reg_refs['Bank Info'] = None
        self.reg_refs['Permission'] = None
        self.reg_refs['Emergency Contact'] = None
        self.reg_refs['Is Deactivated'] = None
        if not is_edit:
            self.reg_refs['Password'] = re.compile(r'\w+') #It will be hashed so it should have something otherwise it will pull an errror
        self.reg_refs['Route'] = re.compile(r'.{9}') #Remove all - temporariy then validate to see how many characters are in there because
        #The exmaple data gives numbers and characters
        self.reg_refs['Account Number']  = re.compile(r'\d{8,17}')#Custom validation where you count all the digits equalling 10 digits according to the given information
        #However looking at information online it could range between 8 to 17 depending on the bank you use.
        is_good = True
        for i,key in enumerate(keys):
            compare_val = row[i]
            if key in custom_vals:
                compare_val = custom_vals[key](compare_val)
            
            if not compare_val and key not in optional_vals:
                return False, ('Error', f'{key} is not in valid format. Check user guide for details.')
            if not self.reg_refs[key]:
                if key in mutate_custom_vals:
                    row[i] = compare_val
                continue
            form_good = self.reg_refs[key].search(compare_val)
            if not form_good:
                #ERROR and display message
                print('Not valid boy', row[i])
                return form_good, ('Error', f'{key} is not in valid format. Check user guide for details.')
            is_good = is_good and form_good
        return is_good, ()
    # def val_state(self, string):
    #     state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California",
    #      "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia",
    #       "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana",
    #        "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi",
    #         "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey",
    #          "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
    #           "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
    #            "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
    #     is_good = string in state_names
    #     if not is_good:
    #         pass #TODO display error
    def val_id(self, string:str):
        string = string.strip()
        if not string.isdigit():
            return False
        for row in self.get_rows():
            emp = Employee(row)
            #I check the first name and and last to make sure it isn't us changing an ID back to what it was previously
            if int(emp.emp_id) == int(string)\
                and emp.fname != self.search_emp_id(int(emp.emp_id)).fname \
                and emp.lname != self.search_emp_id(int(emp.emp_id)):
                return False
        return string

    def val_date(self, string):
        if len(string)!=10:
            return False
        month = int(string[:2])
        day = int(string[3:5])
        year = int(string[6:])
        
        if month > 12 or day > 31:
            return False
        return string
    def val_bank(self, string):
        '''For bank account numbers and routing numbers'''
        return string.replace('-','')
    def val_permission(self, string):
        if string == 'Admin':
            string = 'admin'
        elif string == 'Employee':
            string = 'employee'
        return string
    def val_active(self, string):
        if string == 'Yes':
            string = 'y'
        elif string == 'No':
            string = 'n'
        return string
    def val_route(self, string):
        #The examples given of a routing number is very vague, however it seems
        #it's counting the letters as numbers so we will just check the length of the 
        return string.replace('-','')
    def val_acct(self, string):
        return string.replace('-','')
    def val_info(self, string):
        '''For the Bank info'''
        if string == 'Direct Method':
            string = 'dm'
        elif string == 'Mail Method':
            string = 'mm'
        return string

        

singleton = CSVManager()