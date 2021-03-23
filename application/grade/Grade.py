from flask_restful import Resource, reqparse, inputs
from flask import abort, request
from db import DbConn

DB_TABLE = "grade"
COLUM_DATA = f"id, name, description FROM {DB_TABLE}"

class Grade(Resource):

    def __init__(self):
        super().__init__()
        try:
            self.dbconnect = DbConn.DbConn()
        except Exception as error:
            abort(500, f"Error connect with BD")

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass
    
    def delete(self):
        pass