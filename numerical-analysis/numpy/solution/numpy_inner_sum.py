import numpy as np
np.random.seed(0)


a = np.random.randint(0, 10, size=(16, 16))
b = a[6:-6, 6:-6]

print(b.sum())

