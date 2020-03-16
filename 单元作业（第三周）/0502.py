import numpy as np
import math

x = [64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]
y = [62.55,82.42,132.62,73.13,131.05,86.57,85.49,127.44,55.25,104.84]

x1 = np.mean(x)
y1 = np.mean(y)

k = len(x)
numx = numy = 0
for i in range(k):
    numx += (x[i] - x1)*(y[i] - y1)
for i in range(k):
    numy += (x[i] - x1)**2
# print(numy)
w = numx/numy
b = y1 - w*x1
print("w与b的值分别为:",w,b)