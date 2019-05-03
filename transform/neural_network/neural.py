# coding: utf-8
from sklearn.neural_network import MLPRegressor


class Identify_Number:

    def __init__(self, label, features):
        # label of the feature aka the true value of the data send in test
        self.label = label
        self.features = features
        self.clf = ""

    def exec(self):
        # the real objects who made all of the work
        self.clf = MLPRegressor(hidden_layer_sizes=(666, 666, 666), max_iter=2000)

    def predict(self, data):
        # the method who predict you image 
        return self.clf.predict([data])
