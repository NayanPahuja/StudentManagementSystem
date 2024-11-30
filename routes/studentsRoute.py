from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from config.db import get_database
from models.studentModel import StudentCreate, StudentResponse, StudentUpdate
from bson.objectid import ObjectId

router = APIRouter()

@router.get("/")
async def route_health():
    return {"msg" : "Route health checks passed!"}

# @router.post("/", response_model=StudentResponse, status_code=201)
# async def create_student(student: StudentCreate, db=Depends(get_database)):
#     new_student = await db.students.insert_one(student.dict())
#     return StudentResponse(id=str(new_student.inserted_id), **student.dict())

# @router.get("/", response_model=List[StudentResponse])
# async def get_students(
#     country: Optional[str] = Query(None),
#     age: Optional[int] = Query(None),
#     db=Depends(get_database)
# ):
#     filters = {}
#     if country:
#         filters["address.country"] = country
#     if age is not None:
#         filters["age"] = {"$gte": age}

#     students = await db.students.find(filters).to_list(None)
#     return [StudentResponse(id=str(student["_id"]), **student) for student in students]

# @router.get("/{id}", response_model=StudentResponse)
# async def get_student(id: str, db=Depends(get_database)):
#     student = await db.students.find_one({"_id": ObjectId(id)})
#     if not student:
#         raise HTTPException(status_code=404, detail="Student not found")

#     return StudentResponse(id=str(student["_id"]), **student)

# @router.patch("/{id}", status_code=204)
# async def update_student(
#     id: str,
#     student_update: StudentUpdate,
#     db=Depends(get_database)
# ):
#     student = await db.students.find_one({"_id": ObjectId(id)})
#     if not student:
#         raise HTTPException(status_code=404, detail="Student not found")

#     update_data = student_update.dict(exclude_unset=True)
#     if not update_data:
#         raise HTTPException(status_code=400, detail="No update data provided")

#     await db.students.update_one({"_id": ObjectId(id)}, {"$set": update_data})

# @router.delete("/{id}", status_code=200)
# async def delete_student(id: str, db=Depends(get_database)):
#     result = await db.students.delete_one({"_id": ObjectId(id)})
#     if result.deleted_count == 0:
#         raise HTTPException(status_code=404, detail="Student not found")