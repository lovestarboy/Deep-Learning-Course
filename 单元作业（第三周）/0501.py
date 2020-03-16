import numpy as np
import math

np.random.seed(612)
arr = np.random.rand(1001)
# print(arr[999])
a = int(input('请输入一个数字（1~ 1000）：'))
i = j = 1
while i < 1000:
    i += 1
    if i % a == 0:
        k = arr[i]
        print(j,i,k)
        j += 1
