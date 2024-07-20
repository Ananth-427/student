from fastapi import APIRouter

from router.db import execute_query
from router.models import Smod

get_data = APIRouter()

@get_data.post("/student/{name}/{age}/{grade}")
async def create_student(student: Smod):
    query = """
    insert into student(name,age,grade)
    values($1,$2,$3) returning id;
    """
    student_id = await execute_query(query,student.name,student.age,student.grade)
    return {**student.dict(),"id":student_id}

