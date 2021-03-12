from flask import Flask, request, make_response
from flask_restful import Resource, Api, reqparse
from student import Student

app = Flask(__name__)
api = Api(app)

api.add_resource(Student.Student,'/api/v1/student' ,'/api/v1/student/<int:id_student>')

@app.errorhandler(404)
def error_404(e):
    return make_response("Page not found", 404)

if __name__ == '__main__':
    app.run(debug=True, port=82)