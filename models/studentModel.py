from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId

class Address(BaseModel):
    city: str
    country: str

class StudentCreate(BaseModel):
    name: str
    age: int
    address: Address

class StudentResponse(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()))

class StudentResponseData(BaseModel):
    name: str
    age: int

class StudentResponseFullData(StudentResponseData):
    address: Address

class StudentFinalRespond(BaseModel):
    data: List[StudentResponseData]


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[Address] = None

