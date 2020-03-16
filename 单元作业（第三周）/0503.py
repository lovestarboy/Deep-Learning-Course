import numpy as np
import math

x0 = np.ones((10))
x1 = [64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]
x2 = [2,3,4,2,3,4,2,4,1,3]
y = np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])

x = np.stack((x0,x1,x2),axis=1)
y = y.reshape(10,1)
# print(Y)
X = np.mat(x)
Y = np.mat(y)

W = ((X.T*X)**-1)*X.T*Y
s = W.shape
# print(2**-1)
print("w的shape属性结果是",s)
print("X是",x,"Y是",y,"W是",W)