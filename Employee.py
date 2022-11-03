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
    fname: str
    lname: str
    address: Address
    office_phone: str
    EmpID: int
    pay_type: str = PayTypeEnum.hourly
    wage: float
    birthday: datetime
    permission: str = PermissionEnum.emp
    title: str
    department: str
    office_email: str
    emergency_contact: Dict[str, str]
    end_date: datetime
    is_deactivated: bool