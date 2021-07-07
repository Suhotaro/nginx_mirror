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
    print("request in")
    print(f"{server}: {student.json()}")
    print("request out")
    return student

@app.get("/health")
async def health():
    print("health in")
    health = {"health": "ok"}
    print("health out")
    return health




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