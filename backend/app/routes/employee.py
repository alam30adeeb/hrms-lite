from fastapi import APIRouter, HTTPException
from app.database import get_collection
from app.schemas import EmployeeCreate, EmployeeResponse
from bson import ObjectId

router = APIRouter(prefix="/employees", tags=["Employees"])

employees_collection = get_collection("employees")


def serialize_employee(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "employee_id": employee["employee_id"],
        "full_name": employee["full_name"],
        "email": employee["email"],
        "department": employee["department"],
    }


@router.post("/", status_code=201)
async def create_employee(employee: EmployeeCreate):

    existing = await employees_collection.find_one(
        {"employee_id": employee.employee_id}
    )

    if existing:
        raise HTTPException(status_code=409, detail="Employee ID already exists")

    result = await employees_collection.insert_one(employee.dict())

    new_employee = await employees_collection.find_one(
        {"_id": result.inserted_id}
    )

    return serialize_employee(new_employee)


@router.get("/", response_model=list[EmployeeResponse])
async def get_employees():

    employees = []
    async for emp in employees_collection.find():
        employees.append(serialize_employee(emp))

    return employees


@router.delete("/{employee_id}")
async def delete_employee(employee_id: str):

    result = await employees_collection.delete_one(
        {"employee_id": employee_id}
    )

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee deleted successfully"}