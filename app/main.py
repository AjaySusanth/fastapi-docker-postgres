from fastapi import FastAPI
import psycopg2
import os
from .models import Base
from .routers import users
from .database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(users.router)

def connect_db():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )

@app.get("/db")
async def root():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT VERSION();")
        version = cur.fetchone()
        conn.close()
        return {"message":"Connected to PostgresSQL","version":version}
    except Exception as e:
        return {"error":str(e)}


@app.get('/')
def root():
    return {"message":"FastAPI with Postgres and Docker"}

