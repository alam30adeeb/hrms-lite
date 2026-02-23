from fastapi import APIRouter, HTTPException, Query
from app.database import get_collection
from app.schemas import AttendanceCreate, AttendanceResponse
from datetime import datetime
from typing import Optional

router = APIRouter(prefix="/attendance", tags=["Attendance"])

attendance_collection = get_collection("attendance")
employees_collection = get_collection("employees")


def serialize_attendance(record) -> dict:
    return {
        "id": str(record["_id"]),
        "employee_id": record["employee_id"],
        "date": record["date"],
        "status": record["status"],
    }


@router.post("/", status_code=201)
async def mark_attendance(attendance: AttendanceCreate):

    # Check if employee exists
    employee = await employees_collection.find_one(
        {"employee_id": attendance.employee_id}
    )

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    parsed_date = datetime.strptime(str(attendance.date), "%Y-%m-%d")

    # Prevent duplicate attendance
    existing_record = await attendance_collection.find_one(
        {
            "employee_id": attendance.employee_id,
            "date": parsed_date,
        }
    )

    if existing_record:
        raise HTTPException(
            status_code=409,
            detail="Attendance already marked for this date",
        )

    data = attendance.dict()
    data["date"] = parsed_date

    result = await attendance_collection.insert_one(data)

    new_record = await attendance_collection.find_one(
        {"_id": result.inserted_id}
    )

    return serialize_attendance(new_record)


@router.get("/{employee_id}", response_model=list[AttendanceResponse])
async def get_attendance(
    employee_id: str,
    date: Optional[str] = Query(default=None)
):

    query = {"employee_id": employee_id}

    if date:
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
            query["date"] = parsed_date
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Invalid date format. Use YYYY-MM-DD",
            )

    records = []

    async for record in attendance_collection.find(query):
        records.append(serialize_attendance(record))

    return records

@router.get("/summary/{employee_id}")
async def get_attendance_summary(employee_id: str):

    employee = await employees_collection.find_one(
        {"employee_id": employee_id}
    )

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    total_present = await attendance_collection.count_documents(
        {
            "employee_id": employee_id,
            "status": "Present"
        }
    )

    total_absent = await attendance_collection.count_documents(
        {
            "employee_id": employee_id,
            "status": "Absent"
        }
    )

    total_records = await attendance_collection.count_documents(
        {
            "employee_id": employee_id
        }
    )

    return {
        "employee_id": employee_id,
        "total_present_days": total_present,
        "total_absent_days": total_absent,
        "total_records": total_records
    }