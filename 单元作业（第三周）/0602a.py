import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
 
boston_housing = tf.keras.datasets.boston_housing
(train_x, train_y), (_,_) = boston_housing.load_data(test_split=0)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

titles = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGC","DIS","RAD","TAX","PTRATIO","B-1000","LSTAT","MRDV"]

for i in range(13):
    print(i,"--",titles[i])
t = int(input("请选择属性："))
# print(t)
plt.scatter(train_x[:,t],train_y)
plt.xlabel(titles[t])
plt.ylabel("Price($1000's)")
plt.title(str(t+1)+"."+titles[t]+" - Price")

plt.show()
