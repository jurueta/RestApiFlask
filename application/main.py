from flask import Flask, request, make_response
from flask_restful import Resource, Api, reqparse
from student import Student
from teacher import Teacher
import os

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
DIR_IMAGE = f"{PROJECT_HOME}"

app = Flask(__name__)
app.config["ROOT_FOLDER"] = DIR_IMAGE
api = Api(app)

api.add_resource(Student.Student, '/api/v1/student', '/api/v1/student/<int:id_student>')
api.add_resource(Teacher.Teacher, '/api/v1/teacher', '/api/v1/teacher/<int:id_teacher>')

@app.errorhandler(404)
def error_404(e):
    return make_response("Page not found", 404)

if __name__ == '__main__':
    app.run(debug=True, port=82)