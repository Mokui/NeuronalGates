import time
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from scipy.stats import mode

def display_digits(x_train, y_train, x_test, y_test):
    # Time calcul
    t1_start = time.perf_counter()
    t2_start = time.process_time()

    kmeans = KMeans(n_clusters=10, random_state=0)
    kmeans.fit_predict(x_train, y_train)

    # Plotting
    centers = kmeans.cluster_centers_.reshape(10, 8, 8)
    plt.xticks([])
    plt.yticks([])

    for center in centers:
        plt.imshow(center, interpolation='nearest', cmap=plt.cm.binary)

    svclassifier = SVC(kernel='linear').fit(x_train, y_train)
    y_test_pred = svclassifier.predict(x_test)

    # Precision pourcent
    nbr_tests = 0.0
    correct_prediction = 0.0

    # Calcul correlation; It take all the different digits (0 to 9), so this score is general
    for idx, elem in enumerate(x_test):
        if svclassifier.predict([elem])[0] == y_test[idx]:
            correct_prediction += 1.0
        nbr_tests += 1.0
    print(f"Precision calcul of the predictions : {(correct_prediction/nbr_tests) * 100}%")
    print('correct / nbr = {cor} / {nbr}'.format(
        cor=correct_prediction, nbr=nbr_tests
    ))

    # End Time calcul
    t1_stop = time.perf_counter()
    t2_stop = time.process_time()
    print("Elapsed time for digit determination: %.1f [sec]" % ((t1_stop-t1_start)))
    print("CPU process time for digit determination: %.1f [sec]" % ((t2_stop-t2_start)))
    plt.show()


def display_kmeans(x_train, y_train, x_test, y_test):
    # Time calcul
    t1_start = time.perf_counter()
    t2_start = time.process_time()

    n_digits = len(np.unique(y_train))
    # Passing by PCA first
    reduced_data = PCA(n_components=2).fit_transform(x_train)
    kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
    kmeans.fit(reduced_data)

    # Step size of the mesh. Decrease to increase the quality of the precision.
    h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].

    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh. Use last trained model.
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
            extent=(xx.min(), xx.max(), yy.min(), yy.max()),
            cmap=plt.cm.Paired,
            aspect='auto', origin='lower')

    plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
    # Plot the centroids as a white X
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=169, linewidths=3,
                color='w', zorder=10)
    plt.title('K-means clustering on the digits dataset (PCA-reduced data)\n'
            'Centroids are marked with white cross')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())

    # End Time calcul
    t1_stop = time.perf_counter()
    t2_stop = time.process_time()
    print("Elapsed time for kmeans clustering: %.1f [sec]" % ((t1_stop-t1_start)))
    print("CPU process time for kmeans clustering: %.1f [sec]" % ((t2_stop-t2_start)))
    plt.show()

def heatmap_data(x_train, y_train, x_test, y_test, target_names):
    # Time calcul
    t1_start = time.perf_counter()
    t2_start = time.process_time()

    y_test_pred = show_accuracy(x_train, y_train, x_test,y_test)

    mat = confusion_matrix(y_test, y_test_pred)
    sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
                xticklabels=target_names,
                yticklabels=target_names)
    plt.xlabel('true label')
    plt.ylabel('predicted label')

    # End Time calcul
    t1_stop = time.perf_counter()
    t2_stop = time.process_time()
    print("Elapsed time: %.1f [sec]" % ((t1_stop-t1_start)))
    print("CPU process time: %.1f [sec]" % ((t2_stop-t2_start)))
    plt.show()

def show_accuracy(x_train, y_train, x_test, y_test):
    # We use SVC classifier because the linear model seems more relevant than kmeans
    fitter = OneVsRestClassifier(LinearSVC(random_state=0, max_iter=300000)).fit(x_train, y_train)
    y_test_pred = fitter.predict(x_test)
    
    # Precision pourcent
    nbr_tests = 0.0
    correct_prediction = 0.0

    # Calcul correlation; It take all the different digits (0 to 9), so this score is general
    for idx, elem in enumerate(x_test):
        if fitter.predict([elem]) == y_test[idx]:
            correct_prediction += 1.0
        nbr_tests += 1.0
    
    print(f"Precision calcul of the predictions : {(correct_prediction/nbr_tests) * 100}%")
    print('correct / nbr = {cor} / {nbr}'.format(
        cor=correct_prediction, nbr=nbr_tests
    ))
    return y_test_pred


def main():
    # Loading sklearn dataset digits
    digits = load_digits()
    data = digits['data']
    target = digits['target']
    target_names = digits['target_names']

    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.2)

    #display_digits(x_train, y_train, x_test, y_test)
    #display_kmeans(x_train, y_train, x_test, y_test)
    #heatmap_data(x_train, y_train, x_test, y_test, target_names)

if __name__ == "__main__":
    main()