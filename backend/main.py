from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
from test import cursor, conn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

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
    department: str
    post: str
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
        subdivision_id = user_data.department
        sql = "INSERT INTO employees(name, surname, patronymic, post_id, subdivision_id, email, password) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (user_data.name, user_data.lastname, user_data.patronymic, post_id, subdivision_id, user_data.email, user_data.password))
        conn.commit()

        return {"status": "success", "message": "Пользователь успешно зарегистрирован"}
    except Exception as e:
        return {"status": "fail", "error": str(e)}

@app.post('/api/login')
async def find_user(user_data: UserLogin):
    try:
        sql = "SELECT name FROM employees WHERE email=%s AND password=%s"
        cursor.execute(sql, (user_data.email, user_data.password))

        res = cursor.fetchone()
        name = res[0]

        return {"status": "success", "message": f"Здравствуйте, {name}"}
    except Exception as e:
        return {"status": "fail", "error": str(e)}