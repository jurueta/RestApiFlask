from flask_restful import Resource, reqparse
from db import DbConn
import os

DIR_IMAGE = f"{os.path.abspath}/img/"

class Student(Resource):

    def get(self, id_student=None):
        try:
            dbdata = DbConn.DbConn()

            condition = f"WHERE id = {id_student}" if id_student else ""

            data = dbdata.query(f"""SELECT CONCAT(first_name, ' ', last_name) as name, age, phone, address, CONCAT(date_reg, '') as date
                                FROM student {condition} LIMIT 10""")

            if data["error"] == 0:
                response = {'count':data['count'], 'data' : data['data']}
            else:
                response = {'error' : data['message']}, 500

            return response
        except Exception as error:
            return {'error' : f"An error was generated when executing the data {error}"}
    
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('first_name', type=str, required=True, help="First name is required")
        parser.add_argument('middle_name', type=str)
        parser.add_argument('last_name', type=str, required=True, help="Last name is required")
        parser.add_argument('second_surname', type=str)
        parser.add_argument('age', type=int, required=True, help="Age is required")
        parser.add_argument('phone', type=int, required=True, help="Phone is required")
        parser.add_argument('address', type=str, required=True, help="Address is required")
        parser.add_argument('identification', type=str, required=True, help="Identification is required")
        parser.add_argument('image', type=str)

        args = parser.parse_args()
        
        colum = list(i for i, j in args.items() if j)
        value = list(j for i, j in args.items() if j)
        item = ("%s" for i, j in args.items() if j)

        try:
            dbconnect = DbConn.DbConn()
            
            dbconnect.insert(f"INSERT INTO student ({ ','.join(colum)}) VALUES({','.join(item)})", value)

        except Exception as error:
             return {'error' : f"An error was generated when the data is insert {error}"}

        return {'number' : args['telefono']}
