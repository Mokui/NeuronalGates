# coding: utf-8
from sklearn.neural_network import MLPRegressor


class identify_number:

    def __init__(self, label, features):
        self.label = label
        self.features = features

    def exec():
        clf = MLPRegressor(hidden_layer_sizes=(666, 666, 666), max_iter=2000)
        return clf.fit(self.features, self.label)

    def predict(clf, data):
        return clf.predict([data])
