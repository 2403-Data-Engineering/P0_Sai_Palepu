import os
import mysql.connector

from dotenv import load_dotenv
from mysql.connector import Error
from mysql.connector import errorcode

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("PASS"),
        database=os.getenv("DB"),
        port=os.getenv("PORT"),
        autocommit=True
    )

def select_messages() -> None:
    with get_connection() as conn:
        curso = conn.cursor(dictionary=True)

        sql = "SELECT * FROM student"

        curso.execute(sql)
        for row in curso:
            print(row)

def create_message(message: str) -> None:
    with get_connection() as conn:
        curso = conn.cursor(dictionary=True)
        sql = "INSERT INTO demo_table (message) VALUES (%s)", message

def get_message_by_id(id:int) -> str:
    with get_connection() as conn:
        curso = conn.cursor(dictionary=True)

        curso.execute("SELECT * FROM demo_table WHERE id = %(id)s", {"id":id})
        return curso.fetchone()


select_messages()





