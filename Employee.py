from datetime import datetime
from typing import Dict

class Address:
    def __init__(self, street, apt, city, state, zip_code, country='USA') -> None:
        self.street_address: str = street
        self.apt_no: int = apt if not apt else ''
        self.city: str = city
        self.state: str = state
        self.zip_code: int = zip_code
        self.country = country
    def __str__(self) -> str:
        if self.apt_no == '':
            return f'{self.street_address} {self.city},{self.state} {self.country} {self.zip_code}'
        return f'{self.street_address} #{self.apt_no} {self.city},{self.state} {self.country} {self.zip_code}'
class PayTypeEnum:
    hourly: str = "Hourly"
    salary: str = "Salary"
class PermissionEnum:
    admin: str = "admin"
    emp: str = "employee"
class Employee():
    
    def row_init(self, row):
        self.fname: str = row[1]
        self.lname: str = row[2]
        self.address: Address = Address(row[6],row[7], row[8], row[9], row[10], row[11] )
        self.office_phone: str = row[12]
        self.emp_id: int = row[0]
        self.pay_type: str = row[13]
        self.wage: float = row[16]
        self.birthday: datetime = row[15]
        self.permission: str = row[20]
        self.title: str = row[4]
        self.department: str = row[3]
        self.office_email: str = row[5]
        self.emergency_contact: Dict[str, str] = row[22]
        self.start_date: datetime = row[17]
        self.end_date: datetime = row[18]
        self.bank_info = row[19]
        self.is_deactivated: bool = row[22] == 'y'
        self.social_secuitry = row[14]
    # def __init__(self,fname,lname,address: Address,office_phone, emp_id, pay_type: str,
    #              wage, birthday,permission: str,title,department,office_email,
    #              emergency_contact,end_date,is_deactivated) -> None:
    #     self.fname: str = fname
    #     self.lname: str = lname
    #     self.address: Address =address
    #     self.office_phone: str = office_phone
    #     self.emp_id: int = emp_id
    #     self.pay_type: str = PayTypeEnum.hourly
    #     self.wage: float = wage
    #     self.birthday: datetime = birthday
    #     self.permission: str = permission
    #     self.title: str = title
    #     self.department: str = department
    #     self.office_email: str = office_email
    #     self.emergency_contact: Dict[str, str] = emergency_contact
    #     self.end_date: datetime = end_date
    #     self.is_deactivated: bool = is_deactivated