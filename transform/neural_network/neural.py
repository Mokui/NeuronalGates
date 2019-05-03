# coding: utf-8
from sklearn.neural_network import MLPRegressor


class Identify_Number:

    def __init__(self, label, features):
        self.label = label
        self.features = features
        self.clf = ""

    def exec(self):
        self.clf = MLPRegressor(hidden_layer_sizes=(666, 666, 666), max_iter=2000)

    def predict(self, data):
        return self.clf.predict([data])
