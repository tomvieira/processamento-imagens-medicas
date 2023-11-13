from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
import time
X, y = make_classification(n_samples=3500)

model = MLPClassifier()
t0 = time.time()
model.fit(X, y)
print("Training time:", time.time()-t0)
