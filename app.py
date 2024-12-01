from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from config.db import MongoDB
from routes import students
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        MongoDB.get_client()
        yield
    finally:
        MongoDB.close_connection()

app = FastAPI(
    title="StudentManagementSystem",
    description="A FastAPI backend for a student management system.",
    version="1.0.0",
    lifespan=lifespan
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students.router, tags=["students"])

@app.get("/healthCheck")
async def healthChecker():
    return {
        "msg" : "Hello! Health checks passed!"
    }

@app.get("/")
async def root():
    return {"message": "Welcome to Student Management System"}

if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, host="127.0.0.1", port=8000)