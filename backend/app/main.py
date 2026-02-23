from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routes import employee, attendance
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="HRMS Lite API")

origins = [
    "http://localhost:5173",
    "https://your-vercel-app-name.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(employee.router)
app.include_router(attendance.router)


@app.get("/")
async def root():
    return {"message": "HRMS Lite API is running 🚀"}