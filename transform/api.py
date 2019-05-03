#coding: utf-8
from flask import Flask, render_template, request
from flask_restful import Resource, Api, abort
from neural_network.neural import Identify_Number
from flask_socketio import SocketIO
from neural_network.image_processing import splitter, Image_Manager
from random import shuffle
import os

app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app)


fichier = os.listdir("dataset")
tab = []
for k in fichier:
    value = splitter(k)
    value.label_feature_associate()
    tab.append(value.get_tab())
# print(tab)
shuffle(tab)
print(tab)
feature = [k[1:] for k in tab]
label = [k[0] for k in tab]

neural = Identify_Number(label, feature)
neural.exec()


@app.route("/")
def index():
    return render_template("index.html")


def websocket_visu(data):
    socketio.emit("my_response", data)


class Image(Resource):

    def get(self):
        return {"Hello": "world!"}

    def post(self):
        if not request.json:
            abort(400)
        image = request.json.get("image")
        res = neural.predict(image)
        websocket_visu(image)
        return {"res": res}

api.add_resource(Image, "/image/")

if __name__ == "__main__":
    app.run(debug=True)