from flask_restful import Resource, reqparse
from flask import abort, request
from db import DbConn
import os

DIR_IMAGE = f"{os.path.abspath}/img/"
COLUM_DATA = "id, CONCAT(first_name, ' ', last_name) as name, age, phone, address, CONCAT(date_reg, '') as date FROM student"

parser = reqparse.RequestParser()

parser.add_argument('first_name', type=str, required=True, help="First name is required")
parser.add_argument('middle_name', type=str)
parser.add_argument('last_name', type=str, required=True, help="Last name is required")
parser.add_argument('second_surname', type=str)
parser.add_argument('age', type=int, required=True, help="Age is required")
parser.add_argument('phone', type=int, required=True, help="Phone is required")
parser.add_argument('address', type=str, required=True, help="Address is required")
parser.add_argument('image', type=str)

class Student(Resource):

    def __init__(self):
        super().__init__()
        self.dbconnect = DbConn.DbConn()

    def get(self, id_student=None):
        try:
            condition = f"AND id = {id_student}" if id_student else ""

            data = self.dbconnect.query(f"SELECT {COLUM_DATA} WHERE status = 1 {condition} LIMIT 10")

            if data["error"] == 0:
                response = {'count':data['count'], 'data' : data['data']}
            else:
                response = {'error' : data['message']}, 400

            return response
        except Exception as error:
            return {'error' : f"An error was generated when executing the data ({error})"}, 400
    
    def post(self):
        args = parser.parse_args()
        
        colum = list(i for i, j in args.items() if j)
        value = list(j for i, j in args.items() if j)
        item = ("%s" for i, j in args.items() if j)

        try:

            data = self.dbconnect.insert(f"INSERT INTO student ({ ','.join(colum)}) VALUES({','.join(item)})", value)

            if data["error"] == 0:
                data = dbconnect.query(f"SELECT {COLUM_DATA} WHERE id = %s", (data["id"],))

                return {'data' : data["data"]}
            else:
                return {'error' : data["message"]}, 400

            return {'number' : args['telefono'] }
        except Exception as error:
            return {'error' : f"An error was generated when the data was inserted ({error})"}, 400

    def put(self, id_student=None):
        try:
            if id_student:
                args = parser.parse_args()
                colum = list(f"{i}=%s" for i, j in args.items() if j)
                value = list(j for i, j in args.items() if j)

                value.append(id_student)

                data = self.dbconnect.update(f"UPDATE student set {','.join(colum)} WHERE id = %s", value)

                if data["error"] == 0:
                    data = self.dbconnect.query(f"SELECT {COLUM_DATA} WHERE id = %s", (id_student,))

                    return {'data': data["data"]}
                else:
                    return {'error' : data["message"]}, 400
            else:
                return {'message':"student id is required"}, 400
        except Exception as error:
            return {'error' : f"An error was generated when update data ({error})"}, 400

    def delete(self, id_student=None):
        try:
            if id_student:
                data = self.dbconnect.update(f"UPDATE student set status = 0 WHERE id = %s", (id_student,))
                resp = {'total': data['count']} if data["error"] == 0 else ({'error' : data["message"]}, 400)
                return resp
            else:
                self.dbconnect.update(f"UPDATE student set status = 0")
                resp = {'total': data['count']} if data["error"] == 0 else ({'error' : data["message"]}, 400)
                return resp
        except Exception as error:
            return {'error' : f"An error was generated when delete data ({error})"}, 400
