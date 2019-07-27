from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import docx

application = app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return "Hello World"

api.add_resource(HelloWorld, '/')

class text(Resource):
    def get(self, text, text2):

        doc = docx.Document()
        doc.add_paragraph(text)
        doc.add_paragraph(text2)
        doc.save('pythontowordflask.docx') 

api.add_resource(text, '/text/<text>/<text2>')

if __name__ == '__main__':
    app.run(debug=True)