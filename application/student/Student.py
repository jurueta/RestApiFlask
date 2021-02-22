from flask import jsonify
from flask_restful import Resource
from db import DbConn
import json

class Student(Resource):

    def get(self):
        try:
            dbdata = DbConn.DbConn()

            data = dbdata.query("""SELECT CONCAT(first_name, ' ', last_name) as name, age, phone, address 
                                FROM student LIMIT 10""")

            return {'students' : data["data"]} if data["error"] == 0 else {'error' : data["message"]}
        except Exception as error:
            return {'error' : f"An error was generated when executing the data {error}"}