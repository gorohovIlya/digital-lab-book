from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from test import cursor, conn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from argon2 import PasswordHasher
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime, timedelta
import jwt

env_path = Path(__file__).parent / '.env'
load_dotenv(env_path)

app = FastAPI()
security = HTTPBearer()


ph = PasswordHasher(
    time_cost=3,
    memory_cost=65536,
    parallelism=4,
    hash_len=int(os.environ["HASH_LEN"]),
    salt_len=int(os.environ["SALT_LEN"])
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

class Responce(BaseModel):
    access_token: str
    token_typy: str = "bearer"
    user_id: int

def create_access_token(data: dict):
    data_encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"]))
    data_encode.update({"exp": expire})
    result = jwt.encode(data_encode, os.environ["SECRET_KEY"], os.environ["ALGORITHM"])
    return result


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        pl = jwt.decode(token, os.environ["SECRET_KEY"], os.environ["ALGORITHM"])
        user_id = pl.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, details="Invalid token")
        else:
            return int(user_id)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

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

        data = {
            "sub": str(id),
            "email": user_data.email
        }

        access_token=create_access_token(data)

        return {"status": "success", "message": "Пользователь успешно зарегистрирован", "access_token": access_token}
    except Exception as e:
        return {"status": "fail", "error": str(e)}

@app.post('/api/login')
async def find_user(user_data: UserLogin):
    try:
        sql = "SELECT * FROM employees WHERE email=%s"
        cursor.execute(sql, (user_data.email,))
        res = cursor.fetchone()
        if res is None:
            raise HTTPException(status_code=404, detail="User not found")
        if ph.verify(res[6], user_data.password):

            id = res[0]
            name = res[1]

            data = {
            "sub": str(id),
            "email": user_data.email
            }

            access_token=create_access_token(data)


            return {"status": "success", "text": f'Hello, {name}', "access_token": access_token}
        else:
            raise HTTPException(status_code=404, detail="Uncorrect password")
    except Exception as e:
        return {"status": "fail", "error": str(e)}

