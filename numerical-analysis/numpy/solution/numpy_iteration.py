import numpy as np


a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

for row in a:
    for element in row:
        if element % 2 == 0:
            print(element)
# 2
# 4
# 6
# 8


## Alternative solution
for element in a.ravel():
    if element % 2 == 0:
        print(element)
# 2
# 4
# 6
# 8
