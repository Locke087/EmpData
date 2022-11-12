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

class Employee():
    def __init__(self) -> None:
        self.reg_refs = {}
        self.reg_refs['fname'] = r'[a-zA-Z]{1,}'
        self.reg_refs['lname'] = r'[a-zA-Z]{1,}'
        self.reg_refs['street'] = r'[1-9].[0-0]*[a-zA-Z]'
        self.reg_refs['city'] = r'[a-zA-Z]{1,}'
        self.reg_refs['state'] = r'[a-zA-Z]{1,}'
        self.reg_refs['country'] = r'[a-zA-Z]{1,}'
        self.reg_refs['zipcode'] = r'[0-9]{5}'
        self.reg_refs['id'] = r'[0-9]{1,}'
        self.reg_refs['wage'] = r'[0-9]{1,}\.?[0-9]*'
    def validate(self, key):
        pass
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