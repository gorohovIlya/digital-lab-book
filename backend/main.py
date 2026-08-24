from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
from test import cursor, conn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from argon2 import PasswordHasher

app = FastAPI()

ph = PasswordHasher(
    time_cost=3,
    memory_cost=65536,
    parallelism=4,
    hash_len=64,
    salt_len=32
)

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserRegister(BaseModel):
    name: str
    lastname: str
    patronymic: Optional[str] = None
    departments: list[int]
    post: int
    email: str
    password: str
    passwordRepeat: Optional[str] = None

class UserLogin(BaseModel):
    email: str
    password: str


@app.post('/api/submit')
async def save_to_bd(user_data: UserRegister):
    try:
        conn.rollback()
        post_id = int(user_data.post)
        subdivision_id = user_data.departments
        print(type(subdivision_id))
        hash = ph.hash(user_data.password)
        sql = "INSERT INTO employees(name, surname, patronymic, post_id, email, password) VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (user_data.name, user_data.lastname, user_data.patronymic, post_id, user_data.email, hash))
        conn.commit()

        sql = "SELECT id FROM employees WHERE email=%s"
        cursor.execute(sql, (user_data.email,))
        res = cursor.fetchone()
        id = res[0]

        for i in range(len(subdivision_id)):
            print(type(subdivision_id[i]))
            sql = "INSERT INTO employees_subdivisions(employee_id, subdivision_id) VALUES(%s, %s)"
            cursor.execute(sql, (id, subdivision_id[i]))
            conn.commit()

        return {"status": "success", "message": "Пользователь успешно зарегистрирован"}
    except Exception as e:
        return {"status": "fail", "error": str(e)}

@app.post('/api/login')
async def find_user(user_data: UserLogin):
    try:
        sql = "SELECT * FROM employees WHERE email=%s"
        cursor.execute(sql, (user_data.email,))
        res = cursor.fetchone()
        if ph.verify(res[6], user_data.password):
            return {"status": "success", "text": f'Hello, {res[1]}'}
        else:
            return {"status": "fail", "error": "uncorrected password"}
    except Exception as e:
        return {"status": "fail", "error": str(e)}
