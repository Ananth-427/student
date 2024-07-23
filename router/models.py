from pydantic import BaseModel, Field
from typing_extensions import Optional


class Smod(BaseModel):
    name:str
    age:int
    grade:str

class StudentUpdate(BaseModel):
    name: Optional[str] = Field(None, example="New Name")
    age: Optional[int] = Field(None, example=25)
    grade: Optional[str] = Field(None, example="A")