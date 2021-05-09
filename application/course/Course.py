from flask_restful import Resource, reqparse, inputs
from flask import abort, request
from db import DbConn
from globalFun import functions

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
            data = self.dbconnect.query(f"SELECT COUNT(*) AS cuantity FROM {DB_TABLE} WHERE status = 1 {condition}")

            initial_page, final_page, hasnext, hasprevius = functions.pagination(request.args.get("page"), data['data'][0]['cuantity'], request.base_url)

            data = self.dbconnect.query(f"SELECT {COLUM_DATA} WHERE status = 1 {condition}")

            response = {'count':data['count']}

            response.update(hasnext)
            response.update(hasprevius)
            response.update({'data' : data['data']})

            return response
        except Exception as error:
            return {'error' : f"An error was generated when executing the data ({error})"}, 400

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=functions.validatestr, nullable=False,  help="name valid is required")
        parser.add_argument('description', type=functions.validatestr, help="description valid is required")

        args = parser.parse_args()

        try:
            # Verify course in the BD
            if self.dbconnect.query(f"SELECT * FROM {DB_TABLE} WHERE name = '{args['name']}' and status = 1")['data']:
                return {'error': 'This course exist'}, 400
            
            colum = list(i for i, j in args.items() if j)
            value = list(j for i, j in args.items() if j)
            item = ("%s" for i, j in args.items() if j)

            data = self.dbconnect.insert(f"INSERT INTO {DB_TABLE} ({ ','.join(colum)}) VALUES({','.join(item)})", value)

            data = self.dbconnect.query(f"SELECT {COLUM_DATA} WHERE id = %s", (data["id"],))
            
            return {'data' : data["data"]}

        except Exception as error:
            return {'error' : f"An error was generated when the data was inserted ({error})"}, 400


    def put(self, id_course=None):
        
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=functions.validatestr, help="name valid is required")
        parser.add_argument('description', type=functions.validatestr, help="description valid is required")

        if id_course:
            args = parser.parse_args()
            colum = list(f"{i}=%s" for i, j in args.items() if j)

            if colum:
                try:
                    # Save colums and values in the DB
                    value = list(j for i, j in args.items() if j)
                    value.append(id_course)

                    self.dbconnect.update(f"UPDATE {DB_TABLE} set {','.join(colum)} WHERE id = %s", value)

                    data = self.dbconnect.query(f"SELECT {COLUM_DATA} WHERE id = %s", (id_course,))

                    return {'data': data["data"]}
                except Exception as error:
                    return {'error' : f"An error was generated when update data ({error})"}, 400
            else:
                return {'error': 'please enter the data'}, 400
        else:
            return {'message':"course id is required"}, 400
    
    def delete(self, id_course=None):
        try:
            # delete Logic
            if id_course:
                data = self.dbconnect.update(f"UPDATE {DB_TABLE} set status = 0 WHERE id = %s", (id_course,))
                resp = {'total': data['count']} if data["error"] == 0 else ({'error' : data["message"]}, 400)
                return resp
        except Exception as error:
            return {'error' : f"An error was generated when delete data ({error})"}, 400
