from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routes import employee, attendance

app = FastAPI(title="HRMS Lite API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development
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