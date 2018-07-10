import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

def true_fun(X):
    return np.cos(1.5 * np.pi * X)

np.random.seed(0)
n_samples = 30

X = np.sort(np.random.rand(n_samples)*2)
y = true_fun(X) + np.random.randn(n_samples) * 0.1

def fit_plot(X, y, degrees, score=None):
    plt.figure(figsize=(14, 5))
    for i in range(len(degrees)):
        ax = plt.subplot(1, len(degrees), i + 1)
        plt.setp(ax, xticks=(), yticks=())

        polynomial_features = PolynomialFeatures(degree=degrees[i],
                                                 include_bias=False)
        linear_regression = LinearRegression()
        pipeline = Pipeline([("polynomial_features", polynomial_features),
                             ("linear_regression", linear_regression)])
        pipeline.fit(X[:, np.newaxis], y)
        scores = np.linalg.norm( y - pipeline.predict(X[:, np.newaxis]) )
        cv_scores = cross_val_score(pipeline, X[:, np.newaxis], y,
                                 scoring="neg_mean_squared_error", cv=10)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        pipeline2 = Pipeline([("polynomial_features", polynomial_features),
                             ("linear_regression", linear_regression)])
        pipeline2.fit(X_train[:, np.newaxis], y_train)
        score_split = np.linalg.norm( y_test - pipeline2.predict(X_test[:, np.newaxis]) )
        
        
        
        
        X_plot = np.linspace(0, 2, 100)
        plt.plot(X_plot, pipeline.predict(X_plot[:, np.newaxis]), label="Model")
        plt.plot(X_plot, true_fun(X_plot), label="True function")
        plt.scatter(X, y, edgecolor='b', s=20, label="Samples")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.xlim((0, 2.2))
        plt.ylim((-2, 2))
        plt.legend(loc="best")
        if score == 'cv':
            plt.title("Degree {}\nMSE = {:.2e}".format(
                degrees[i], -cv_scores.mean()))
        elif score == "split":
            plt.title("Degree {}\nMSE = {:.2e}".format(
                degrees[i], score_split))
        else:
            plt.title("Degree {}\nMSE = {:.2e}".format(
                degrees[i], scores))

    plt.show()
