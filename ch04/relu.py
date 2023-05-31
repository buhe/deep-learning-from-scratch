import numpy as np
x = np.array([-1, 2, 3, -4, 5])
mask = (x <= 0)
print(mask)
x[mask] = 0
print(x)