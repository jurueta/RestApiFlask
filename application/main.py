from flask import Flask, request
from flask_restful import Resource, Api
from student import Student

app = Flask(__name__)
api = Api(app)

api.add_resource(Student.Student, '/api/v1/student')

if __name__ == '__main__':
    app.run(debug=True, port=82)