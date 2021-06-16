from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int


app = FastAPI()

server = 2


@app.post("/student")
async def create_item(student: Student):
    print(f"{server}: {student.json()}")
    return student




"""
curl -X 'POST'  'http://localhost:8000/student' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "string", "age": 0}'

curl -X 'POST' \
  'http://127.0.0.1:8000/student' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Bob",
  "age": 25
}'
"""