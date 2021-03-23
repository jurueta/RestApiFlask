from flask_restful import Resource, reqparse, inputs
from flask import abort, request
from db import DbConn

DB_TABLE = "course"
COLUM_DATA = f"id, name, description FROM {DB_TABLE}"


class Course(Resource):

    def __init__(self):
        super().__init__()
        try:
            self.dbconnect = DbConn.DbConn()
        except Exception as error:
            abort(500, f"Error connect with BD")

    def get(self, id_course=None):
        condition = f"AND id = {id_course}" if id_course else ""
        try:

            data = self.dbconnect.query(f"SELECT {COLUM_DATA} WHERE {condition} LIMIT 10")

            response = {'count':data['count'], 'data' : data['data']}

            return response
        except Exception as error:
            return {'error' : f"An error was generated when executing the data ({error})"}, 400

    def post(self):
        pass

    def put(self):
        pass
    
    def delete(self):
        pass