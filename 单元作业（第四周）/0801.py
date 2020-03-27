import tensorflow as tf

x = [64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]
y = [62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]

x1 = tf.convert_to_tensor(x)
y1 = tf.convert_to_tensor(y)

x2 = tf.reduce_mean(x1)
y2 = tf.reduce_mean(y1)

x3 = tf.subtract(x,x2)
y3 = tf.subtract(y,y2)

num = tf.multiply(x3,y3)
num1 = tf.reduce_sum(num)

num2 = tf.square(x3)
num3 = tf.reduce_sum(num2)

w = tf.divide(num1,num3)

num4 = tf.multiply(w,x2)
b = tf.subtract(y2,num4)

print(w)
print(b)