from flask import Flask, request, make_response, abort, send_from_directory
from flask_restful import Resource, Api, reqparse
from student import Student
from teacher import Teacher
from course import Course
import os

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config["ROOT_FOLDER"] = PROJECT_HOME
app.config["UPLOAD_FOLDER"] = f"{PROJECT_HOME}/upload/"

api = Api(app)

api.add_resource(Student.Student, '/api/v1/student', '/api/v1/student/<int:id_student>')
api.add_resource(Teacher.Teacher, '/api/v1/teacher', '/api/v1/teacher/<int:id_teacher>')
api.add_resource(Course.Course, '/api/v1/course', '/api/v1/course/<int:id_course>')

@app.errorhandler(404)
def error_404(e):
    return make_response("Page not found", 404)

@app.route('/img/<string:img_name>')
def getImage(img_name):
    return send_from_directory(f"{app.config['ROOT_FOLDER']}/img/", img_name) 

if __name__ == '__main__':
    app.run(debug=True, port=82)