from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from config.db import get_database
from models.studentModel import StudentCreate, StudentResponse, StudentUpdate, StudentResponseData, StudentFinalRespond, StudentResponseFullData
from bson.objectid import ObjectId
from config.logger import logger

router = APIRouter(prefix="/students", tags=["students"])



@router.post("", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db=Depends(get_database)):
    new_student = db.students.insert_one(student.dict())
    logger.info("Successfully posted data into the DB")
    return StudentResponse(id=str(new_student.inserted_id), **student.dict())

@router.get("", response_model = StudentFinalRespond)
def get_students(
    country: Optional[str] = Query(None),
    age: Optional[int] = Query(None),
    db=Depends(get_database)
):
    filters = {}
    if country:
        filters["address.country"] = country
    if age is not None:
        filters["age"] = {"$gte": age}
    students = db.students.find(filters)
    studentList = [StudentResponseData(id=str(student["_id"]), **student) for student in students]
    logger.info("Successfully retrieved data from the DB")
    return StudentFinalRespond(data=studentList)

@router.get("/{id}", response_model=StudentResponseFullData)
def get_student(id: str, db=Depends(get_database)):
    student = db.students.find_one({"_id": ObjectId(id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    logger.info("Successfully got student: %s data from the DB", id)
    return StudentResponseFullData(id=str(student["_id"]), **student)

@router.patch("/{id}", status_code=204,response_description="No Content")
def update_student(
    id: str,
    student_update: StudentUpdate,
    db=Depends(get_database)
):
    student = db.students.find_one({"_id": ObjectId(id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    update_data = student_update.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No update data provided")

    db.students.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    logger.info("Successfully updated student: %s data into the DB", id)

    
 
@router.delete("/{id}", status_code=200,response_description="sample response",response_model=dict)
def delete_student(id: str, db=Depends(get_database)):
    result = db.students.delete_one({"_id": ObjectId(id)})
    logger.info("Successfully deleted student: %s data from the DB", id)
    return {}
