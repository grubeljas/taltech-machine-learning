import numpy as np
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

X = np.genfromtxt("happysadpixels.csv", delimiter=",", dtype=int)
y = np.genfromtxt("happysadlabels.csv", delimiter=",", dtype=int)
norm = Normalize(-1, 1, clip=True)

X.shape
y.shape

nn = MLPClassifier(hidden_layer_sizes=(3,), max_iter=2000)
nn = nn.fit(X, y)

print("Iterations", nn.n_iter_, "Final loss", nn.loss_)

output_weights = nn.coefs_[0]
out_weights1 = [i[0] for i in nn.coefs_[1]]
out_weights2 = [i[0] for i in nn.coefs_[1]]


for n in range(1):
    plt.imshow(np.array(X[n]).reshape(6, 6), norm=norm)
    plt.show()
    first = [i[0] for i in nn.coefs_[0]] * X[n]
    plt.imshow(np.array(first).reshape(6, 6), norm=norm)
    plt.show()
    second = [i[1] for i in nn.coefs_[0]] * X[n]
    plt.imshow(np.array(second).reshape(6, 6), norm=norm)
    plt.show()
    third = [i[2] for i in nn.coefs_[0]] * X[n]
    plt.imshow(np.array(third).reshape(6, 6), norm=norm)
    plt.show()
    plt.imshow(np.array([i[0] for i in nn.coefs_[1]]).reshape(3, 1))
    plt.show()
    plt.imshow(np.array([i[1] for i in nn.coefs_[1]]).reshape(3, 1))
    plt.show()
