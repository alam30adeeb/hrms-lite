# HRMS Lite 🚀

A lightweight Human Resource Management System built with FastAPI, MongoDB, and React.

This application allows an admin to manage employees and track daily attendance through a clean and professional web interface.

---

## 🔥 Features

### 👨‍💼 Employee Management
- Add new employee
- View all employees
- Delete employee
- Unique employee ID validation
- Email format validation
- Proper error handling

### 📅 Attendance Management
- Mark attendance (Present / Absent)
- View attendance records per employee
- Prevent duplicate attendance for same date
- Filter attendance by date (Bonus)
- Attendance summary:
  - Total present days
  - Total absent days
  - Total records

---

## 🛠 Tech Stack

### Frontend
- React (Vite)
- Axios
- React Router DOM

### Backend
- FastAPI
- MongoDB (Atlas)
- Motor (Async MongoDB driver)
- Pydantic (Validation)

### Deployment
- Backend: Render (To be deployed)
- Frontend: Vercel (To be deployed)

---

## 📂 Project Structure


HRMS/
│
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── database.py
│ │ ├── schemas.py
│ │ └── routes/
│ │ ├── employee.py
│ │ └── attendance.py
│ ├── requirements.txt
│ └── Procfile
│
├── frontend/
│ ├── src/
│ │ ├── pages/
│ │ │ ├── Employees.jsx
│ │ │ └── Attendance.jsx
│ │ ├── App.jsx
│ │ └── main.jsx
│
└── README.md


---

## 🚀 How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/hrms-lite.git
cd hrms-lite
2️⃣ Backend Setup
cd backend
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt

Create .env file inside backend:

MONGO_URL=your_mongodb_connection_string

Run backend:

uvicorn app.main:app --reload

Backend runs on:

http://127.0.0.1:8000
3️⃣ Frontend Setup
cd frontend
npm install
npm run dev

Frontend runs on:

http://localhost:5173
📌 API Endpoints
Employee

POST /employees

GET /employees

DELETE /employees/{employee_id}

Attendance

POST /attendance

GET /attendance/{employee_id}

GET /attendance/{employee_id}?date=YYYY-MM-DD

GET /attendance/summary/{employee_id}

✅ Assumptions

Single admin user (no authentication required)

Basic HR operations only

No payroll or leave management

🎯 Bonus Features Implemented

Attendance filtering by date

Total present/absent days summary per employee

📌 Author

Built as a full-stack coding assignment demonstrating:

Frontend development

Backend API design

Database modeling

Validation & error handling

Production-ready structure


---
