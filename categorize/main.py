# coding: utf-8
from tf_idf import *
from flask import Flask, render_template, request
from flask_restful import Resource, Api, abort
import os

app = Flask(__name__)
api = Api(app)

fichier = os.listdir("dataset")



# the api who can access to our objects to predict
class File_Worker(Resource):

    def get(self):
        return {"title": "your title", "content": "your content"}

    def post(self):
        if not request.json:
            abort(400)
        title = request.json.get("title")
        content = request.json.get("content")
        if f"{title}.txt" not in fichier:
            print("write file")
            with open(f"dataset/{title}.txt", "a+") as file:
                file.write(content)
            fichier.append(f"{title}.txt")
        else:
            print("already exist")
        res = "ok"
        return {"res": fichier}


class Result(Resource):

    def get(self):
        work = {f: worker(f) for f in fichier}
        return work

# our endpoint api
api.add_resource(File_Worker, "/file/")
api.add_resource(Result, "/result/")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5050)