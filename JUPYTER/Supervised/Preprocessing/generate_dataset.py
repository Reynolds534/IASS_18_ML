import numpy as np

def generate_dataset(n_features):
    if n_features <6:
        print 'Please enter a number of features strictly bigger than 5'
        return None, None
    target = np.random.uniform(0,10,100)
    X1 = target**2 - target + np.random.uniform(0,25,100)
    X2 = target + np.random.uniform(0,15,100)
    X3 = target + target**2 + np.random.uniform(0,50,100)
    X4 = X3 + np.random.uniform(0,5,100)
    X5 = X1 + X2 + X3
    random_state = np.random.RandomState(0)
    X = np.array([X1,X2,X3,X4,X5]).T
    X = np.c_[X, random_state.randn(100, (n_features-5) )]
    Z = X[:, np.random.permutation(X.shape[1])]
    return Z, target
