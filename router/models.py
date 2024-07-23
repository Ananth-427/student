from pydantic import BaseModel, Field
from typing_extensions import Optional


class Smod(BaseModel):
    name:str
    age:int
    grade:str

