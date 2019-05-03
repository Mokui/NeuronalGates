#coding: utf-8
from flask import Flask, render_template, request
from flask_restful import Resource, Api, abort
from neural_network.neural import Identify_Number
from flask_socketio import SocketIO
from neural_network.image_processing import splitter, Image_Manager
from random import shuffle
from numpy import argmax
import os

# call the lib to start the rest api and the websocket
app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app)

# access to the class who permit the predictive system
# execute before the main function in a simple variable to get the variable global
fichier = os.listdir("dataset")
tab = []
for k in fichier:
    value = splitter(k)
    value.label_feature_associate()
    tab.append(value.get_tab())
shuffle(tab)
feature = [k[1:] for k in tab]
label = [k[0] for k in tab]

neural = Identify_Number(label, feature)
neural.exec()

# a simple web page to print in the futurethe result of the work
@app.route("/")
def index():
    return render_template("index.html")


# a websocket to print the data
def websocket_visu(data):
    socketio.emit("my_response", data)


# the api who can access to our objects to predict
class Image(Resource):

    def get(self):
        return {"Hello": "world!"}

    def post(self):
        if not request.json:
            abort(400)
        image = request.json.get("image")
        res = neural.predict(image)
        for k in range(0,len(res[0])):
            print(k," : ",res[0][k])
        return {"res": str(argmax(res))}

# our endpoint api
api.add_resource(Image, "/image/")

# main function declaration
if __name__ == "__main__":
    app.run(debug=True)