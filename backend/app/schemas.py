from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Literal


class EmployeeBase(BaseModel):
    employee_id: str = Field(..., min_length=1)
    full_name: str = Field(..., min_length=1)
    email: EmailStr
    department: str = Field(..., min_length=1)


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: str


class AttendanceBase(BaseModel):
    employee_id: str = Field(..., min_length=1)
    date: date
    status: Literal["Present", "Absent"]


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceResponse(AttendanceBase):
    id: str