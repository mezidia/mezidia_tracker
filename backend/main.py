from typing import Optional

import uvicorn
from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder

from database import Client
from models import User

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/", response_description="Add new student", response_model=User)
async def create_student(student: User = Body(...)):
    student = jsonable_encoder(student)
    new_student = await client.create_document(student)
    return new_student

if __name__ == '__main__':
    uvicorn.run('main:app')
