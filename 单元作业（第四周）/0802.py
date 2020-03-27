import tensorflow as tf

x = [64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]
y = [62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]

x1 = tf.convert_to_tensor(x)
y1 = tf.convert_to_tensor(y)

a = tf.reduce_sum(tf.add(x1,y1))
b = tf.multiply(tf.reduce_sum(x1),tf.reduce_sum(y1))

a1 = tf.reduce_sum(tf.square(x1))
b1 = tf.square(tf.reduce_sum(x1))

w = tf.divide(tf.subtract(a,b),tf.subtract(a1,b1))


a2 = tf.subtract(tf.reduce_sum(y1),tf.multiply(w,tf.reduce_sum(x1)))

bp = tf.divide(a2,tf.size(x1,tf.float32))

print(w)
print(bp)