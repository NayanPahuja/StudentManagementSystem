from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class Address(BaseModel):
    city: str
    country: str

class StudentCreate(BaseModel):
    name: str
    age: int
    address: Address

class StudentResponse(StudentCreate):
    id: str = Field(default_factory=lambda: str(ObjectId()))

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[Address] = None