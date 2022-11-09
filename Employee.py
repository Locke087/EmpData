from datetime import datetime
from typing import Dict
class Address:
    street_address: str
    apt_no: int
    city: str
    state: str
    zip_code: int
class PayTypeEnum:
    hourly: str = "Hourly"
    salary: str = "Salary"
class PermissionEnum:
    admin: str = "admin"
    emp: str = "employee"
class Employee():
    def __init__(self,fname,lname,address: Address,office_phone, emp_id, pay_type: str,
                 wage, birthday,permission: str,title,department,office_email,
                 emergency_contact,end_date,is_deactivated) -> None:
        self.fname: str = fname
        self.lname: str = lname
        self.address: Address =address
        self.office_phone: str = office_phone
        self.emp_id: int = emp_id
        self.pay_type: str = PayTypeEnum.hourly
        self.wage: float = wage
        self.birthday: datetime = birthday
        self.permission: str = permission
        self.title: str = title
        self.department: str = department
        self.office_email: str = office_email
        self.emergency_contact: Dict[str, str] = emergency_contact
        self.end_date: datetime = end_date
        self.is_deactivated: bool = is_deactivated