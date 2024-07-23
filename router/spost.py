from fastapi import HTTPException

from fastapi import APIRouter

from router.db import execute_query, fetch_query
from router.models import Smod

get_data = APIRouter()

@get_data.post("/student/{name}/{age}/{grade}", tags=["POST data"])
async def create_student(student: Smod):
    query = """
    insert into student(name,age,grade)
    values($1,$2,$3) returning id;
    """
    student_id = await execute_query(query,student.name,student.age,student.grade)
    return {**student.dict(),"id":student_id}


@get_data.put("/student/{student_id}", tags=["PUT data"])
async def update_student(student_id: int, student: Smod):
    query = """
    UPDATE student
    SET name = $1, age = $2, grade = $3
    WHERE id = $4
    RETURNING id;
    """
    updated_student_id = await execute_query(query, student.name, student.age, student.grade, student_id)
    return {**student.dict(), "id": updated_student_id}


@get_data.get("/student/{student_id}", tags=["GET data"])
async def get_student(student_id: int):
    query = """
    SELECT *
    FROM student
    WHERE id = $1
    """

    result = await fetch_query(query, student_id)
    student_record = result[0]

    return {
        "id": student_record["id"],
        "name": student_record["name"],
        "age": student_record["age"],
        "grade": student_record["grade"]
    }


@get_data.delete("/student/{student_id}", tags=["DELETE data"])
async def delete_student(student_id: int):
    query = """
    DELETE FROM student
    WHERE id = $1
    RETURNING id;
    """

    result = await execute_query(query, student_id)
    return {"id": student_id, "message": "Student deleted successfully"}