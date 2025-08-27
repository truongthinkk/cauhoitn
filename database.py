import mysql.connector
from datetime import datetime

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="course_registration"
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def fetch_all(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()
    @staticmethod
    def search_student(db, mssv):
        query = "SELECT * FROM students WHERE mssv = %s"
        result = db.fetch_all(query, (mssv,))
        formatted_students = []
        for student in result:
            mssv, name, dob, email, phone, address = student
            formatted_dob = dob.strftime("%d-%m-%Y")  # Định dạng lại ngày tháng
            formatted_students.append((mssv, name, formatted_dob, email, phone, address))
        
        return formatted_students if formatted_students else []
