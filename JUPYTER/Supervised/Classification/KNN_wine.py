import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

def KNN_plot_wine(n_neighbors, x1=0, x2=9, metric='uniform'):
    # import some data to play with
    wine = datasets.load_wine()

    # we only take the first two features. We could avoid this ugly
    # slicing by using a two-dim dataset
    X = wine.data[:, [x1, x2]]
    y = wine.target

    h = .02  # step size in the mesh

    # Create color maps
    cmap_light = ListedColormap(['#aec7e8', '#ffbb78', '#98df8a' ])
    cmap_bold = ListedColormap(['#1f77b4', '#ff7f0e', '#2ca02c'])

    for weights in [metric]:
        # we create an instance of Neighbours Classifier and fit the data.
        clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
        clf.fit(X, y)

        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, x_max]x[y_min, y_max].
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.figure()
        plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

        # Plot also the training points
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
                    edgecolor='k', s=20)
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.title("3-Class classification (k = %i, weights = '%s')"
                  % (n_neighbors, weights))
        plt.xlabel('Feature '+str(x1+1))
        plt.ylabel('Feature '+ str(x2+1))

    plt.show()
