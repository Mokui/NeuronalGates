#coding: utf-8
from flask import Flask, render_template, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    print("zoulou chibre d'or")
    return render_template('index.html')


class Image(Resource):

    def get(self):
        return {"Hello": "world!"}

    def post(self):
        if not request.json:
            abort(400)
        image = request.json.get("image")
        return {"res": image}

api.add_resource(Image, "/image/")

if __name__ == "__main__":
    app.run(debug=True)