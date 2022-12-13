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
            return f'{self.street_address} {self.city},\n{self.state},{self.country} {self.zip_code}'
        return f'{self.street_address} #{self.apt_no} {self.city},{self.state} {self.country} {self.zip_code}'

class Employee():

    def row_init(self, row):
        '''This only works to exist with legacy code that will be fixed later'''
        self.__init__(row=row)
    def sync_row(self):
        self.row[0] = self.emp_id
        self.row[1] = self.fname
        self.row[2] = self.lname
        self.row[3] = self.department
        self.row[4] = self.title
        self.row[5] = self.office_email
        self.row[6],self.row[7], self.row[8], self.row[9], self.row[10], self.row[11] = self.address.street_address, self.address.apt_no,\
                                                          self.address.city, self.address.state,\
                                                          self.address.zip_code,self.address.country
        self.row[12] = self.office_phone
        self.row[13] = self.pay_type
        self.row[14] = self.wage
        self.row[15] = self.birthday
        self.row[16] = self.social_secuitry
        self.row[17] = self.start_date
        self.row[18] = self.end_date
        self.row[19] = self.bank_info
        self.row[20] = self.permission
        self.row[21] = self.emergency_contact
        self.row[22] = self.is_deactivated
        self.row[23] = self.password
        self.row[24] = self.route
        self.row[25] = self.acct_no
    def __init__(self, row=None):
        if not row:
            return
        self.row = row
        self.emp_id: int = row[0]
        self.fname: str = row[1]
        self.lname: str = row[2]
        self.department: str = row[3]
        self.title: str = row[4]
        self.office_email: str = row[5]
        self.address: Address = Address(row[6],row[7], row[8], row[9], row[10], row[11] )
        self.office_phone: str = row[12]
        self.pay_type: str = row[13]
        self.wage = row[14]
        self.birthday: datetime = row[15]
        self.social_secuitry: float = row[16]
        self.start_date: datetime = row[17]
        self.end_date: datetime = row[18]
        self.bank_info = row[19]
        self.permission: str = row[20]
        self.emergency_contact: Dict[str, str] = row[21]
        self.is_deactivated: bool = row[22]
        self.password = row[23]
        self.route = row[24]
        self.acct_no = row[25]
    def is_active(self):
        return self.is_deactivated == 'y'
    def mail_method(self):
        pass
        