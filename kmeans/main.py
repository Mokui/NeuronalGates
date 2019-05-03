import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.svm import SVC
from scipy.stats import mode

def main():
    # Loading sklearn dataset digits
    digits = load_digits()
    data = digits['data']
    target = digits['target']

    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.3)
    # print(data.shape)

    kmeans = KMeans(n_clusters=10, random_state=0)
    # Fit the data
    clusters = kmeans.fit_predict(x_train,y_train)
    # print(kmeans.cluster_centers_.shape)

    # Plotting
    centers = kmeans.cluster_centers_.reshape(10, 8, 8)
    plt.xticks([])
    plt.yticks([])

    for center in centers:
        plt.imshow(center, interpolation='nearest', cmap=plt.cm.binary)
    plt.show()

    # Precision pourcent
    nbr_tests = 0.0
    correct_prediction = 0.0
    svclassifier = SVC(kernel='linear').fit(x_train, y_train)

    for idx, elem in enumerate(x_test):
        
        # print(idx, elem, kmeans.predict([elem]) , y_test[idx].reshape(1))
        if int(svclassifier.predict([elem])) == y_test[idx]:
            correct_prediction += 1.0
        nbr_tests += 1.0

    print(f"Precision calcul of the predictions : {(correct_prediction/nbr_tests) * 100}%")


if __name__ == "__main__":
    main()