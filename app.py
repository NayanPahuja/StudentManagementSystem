from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from config.db import get_database
from routes.studentsRoute import router as student_router




app = FastAPI(title="StudentManagementSystem",
              description="A FastAPI backend for a student management system.",
              version="1.0.0",)


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
async def startup_event():
    get_database()


@app.get("/healthCheck")
async def healthChecker():
    return {
        "msg" : "Hello! Health checks passed!"
    }

@app.include_router(student_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Student Management System"}


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, host="127.0.0.1", port=8000)