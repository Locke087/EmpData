import pytest

from Employee import Employee
import csv
import os
from unittest import TestCase
from shutil import copy
from time import sleep
class TestEmployee(TestCase):
    def setUp(self) -> None:
        copy('./employee.csv', './employeetest.csv')
        return super().setUp()
    def test_employee(self):
            allInfo = {}
            data = {}
            holder = []
            employee = Employee()
            emp_data = None

            with open('./employee.csv') as file:
                    reader = csv.reader(file)
                    for i,row in enumerate(reader):
                        if i == 0:
                            continue
                        else:
                            emp_data = row
                            break 
            employee.row_init(emp_data)
            self.assertTrue( employee.fname == "John" )
            self.assertTrue( employee.lname == "Doe" )
            self.assertTrue( employee.emp_id == "1" )
            self.assertTrue( employee.wage == "40" )
            self.assertTrue( employee.title == "Magic Teacher" )
            self.assertTrue( employee.department == "Green Pixies" )
            self.assertTrue( employee.office_email == "john.doe@gmail.com" )
            self.assertTrue( employee.address.street_address == "123 abc street" )
            self.assertTrue( employee.address.city == "Spanish Fork" )
            self.assertTrue( employee.address.state == "Utah" )
            self.assertTrue( employee.address.zip_code == "14323" )
            self.assertTrue( employee.address.country == "USA" )
            self.assertTrue( employee.office_phone == "801-123-1234" )
            self.assertTrue( employee.pay_type == "Hourly" )
            self.assertTrue( employee.social_secuitry == "123-123-123" )
            self.assertTrue( employee.is_deactivated == "n" )
    def test_read(self):
        i = 0
        rows = []
        with open('./employeetest.csv') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        i += 1
                        if i == 1:
                            continue
                        
                        rows.append(row)
        
        self.assertTrue(i == 13) #Base csv file has just 13 rows
        self.assertTrue(rows[0][0] != "EmpID")
    def test_create(self):
        i = 0
        row = None
        with open('./employeetest.csv') as file:
                    reader = csv.reader(file)
                    for i, val in enumerate(reader):
                        if i == 0:
                            continue
                        row = val.copy()
                        break
        row[0] = '9999'
        print(row)
    
        with open('./employeetest.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(row)
        
        rows = []
        with open('./employeetest.csv') as file:
                    reader = csv.reader(file)
                    for i,row in enumerate(reader):
                        
                        if i == 0:
                            continue
                        
                        rows.append(row)
        self.assertTrue(len(rows) == 13) #Base csv file has just 13 rows
        self.assertTrue(rows[0][0] != "EmpID")
        self.assertTrue(rows[-1][0] == "9999")
    def tearDown(self) -> None:
        # os.remove('employeetest.csv')
        return super().tearDown()
    
