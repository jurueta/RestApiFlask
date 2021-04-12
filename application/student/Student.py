from flask_restful import Resource, reqparse, inputs
from flask import abort, request, make_response, current_app
from db import DbConn
from globalFun import functions


DB_TABLE = "student"
COLUM_DATA = f"id, CONCAT(first_name, ' ', last_name) as name, age, phone, address, CONCAT(date_reg, '') as date, image FROM {DB_TABLE}"


class Student(Resource):

    def __init__(self):
        super().__init__()
        try:
            self.dbconnect = DbConn.DbConn()
        except Exception as error:
            abort(500, f"Error connect with BD")

    def get(self, id_student=None):
        
        condition = f"AND id = {id_student}" if id_student else ""

        consult_limit = functions.pagination(request.args.get("page"))

        try:
            data = self.dbconnect.query(f"SELECT {COLUM_DATA} WHERE status = 1 {condition} LIMIT {consult_limit['page_initial']}, {consult_limit['page_final']}")

            for i in data['data']:
                i["image"] = f"{request.host_url}{i['image']}" if i['image'] else None

            response = {'count':data['count'], 'data' : data['data']}

            return response
        except Exception as error:
            return {'error' : f"An error was generated when executing the data ({error})"}, 400
    

    def post(self):

        parser = reqparse.RequestParser()

        parser.add_argument('identification', type=str, required=True, help="identification valid is required")
        parser.add_argument('first_name', type=inputs.regex('^[a-zA-z ]*$'), required=True, help="First name valid is required")
        parser.add_argument('middle_name', type=inputs.regex('^[a-zA-z ]*$'))
        parser.add_argument('last_name', type=inputs.regex('^[a-zA-z ]*$'), required=True, help="Last name valid is required")
        parser.add_argument('second_surname', type=inputs.regex('^[a-zA-z ]*$'))
        parser.add_argument('age', type=int, required=True, help="Age valid is required")
        parser.add_argument('phone', type=int, required=True, help="Phone valid is required")
        parser.add_argument('address', type=str, required=True, help="Address valid is required")
        parser.add_argument('image', type=str)

        args = parser.parse_args()

        try:
            # Verify student in the BD
            if self.dbconnect.query(f"SELECT * FROM {DB_TABLE} WHERE identification = {args['identification']}")['data']:
                return {'error': 'This student exist'}, 400

            # Save Image in the server
            if args["image"]:
                
                transfer = functions.Base64ToFile(args)

                if transfer:
                    return transfer

            # Save colums and values in the DB
            colum = list(i for i, j in args.items() if j)
            value = list(j for i, j in args.items() if j)
            item = ("%s" for i, j in args.items() if j)

            data = self.dbconnect.insert(f"INSERT INTO {DB_TABLE} ({ ','.join(colum)}) VALUES({','.join(item)})", value)

            data = self.dbconnect.query(f"SELECT {COLUM_DATA} WHERE id = %s", (data["id"],))
            
            return {'data' : data["data"]}

        except Exception as error:

            return {'error' : f"An error was generated when the data was inserted ({error})"}, 400

    def put(self, id_student=None):
        
        parser = reqparse.RequestParser()

        parser.add_argument('identification', type=str, help="identification valid is required")
        parser.add_argument('first_name', type=inputs.regex('^[a-zA-z ]*$'), help="First name valid is required")
        parser.add_argument('middle_name', type=inputs.regex('^[a-zA-z ]*$'))
        parser.add_argument('last_name', type=inputs.regex('^[a-zA-z ]*$'), help="Last name valid is required")
        parser.add_argument('second_surname', type=inputs.regex('^[a-zA-z ]*$'))
        parser.add_argument('age', type=int, help="Age valid is required")
        parser.add_argument('phone', type=int, help="Phone valid is required", dest="phone_number",)
        parser.add_argument('address', type=str, help="Address valid is required")
        parser.add_argument('image', type=str)

        if id_student:
            args = parser.parse_args()
            colum = list(f"{i}=%s" for i, j in args.items() if j)

            if colum:
                try:
                    # Save Image in the server
                    if args["image"]:
                        
                        transfer = functions.Base64ToFile(args)

                        if transfer:
                            return transfer

                    # Save colums and values in the DB
                    value = list(j for i, j in args.items() if j)
                    value.append(id_student)

                    self.dbconnect.update(f"UPDATE {DB_TABLE} set {','.join(colum)} WHERE id = %s", value)

                    data = self.dbconnect.query(f"SELECT {COLUM_DATA} WHERE id = %s", (id_student,))

                    return {'data': data["data"]}
                except Exception as error:
                    return {'error' : f"An error was generated when update data ({error})"}, 400
            else:
                return {'error': 'please enter the data'}, 400
        else:
            return {'message':"student id is required"}, 400


    def delete(self, id_student=None):
        try:
            # delete Logic
            if id_student:
                data = self.dbconnect.update(f"UPDATE {DB_TABLE} set status = 0 WHERE id = %s", (id_student,))
                resp = {'total': data['count']} if data["error"] == 0 else ({'error' : data["message"]}, 400)
                return resp
            else:
                self.dbconnect.update(f"UPDATE {DB_TABLE} set status = 0")
                resp = {'total': data['count']} if data["error"] == 0 else ({'error' : data["message"]}, 400)
                return resp
        except Exception as error:
            return {'error' : f"An error was generated when delete data ({error})"}, 400
