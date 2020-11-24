# import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


tf.set_random_seed(777)  # for reproducibility

#1. 그래프 구현#

# H(x) = Wx + b 
# X and Y data, H(x) = Y
#x_train = [1, 2, 3]
#y_train = [1, 2, 3]
X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])
#                                   1차원이고 값은 마음데로 넣을 수 있다.

W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")
#                                rank

# Our hypothesis XW+b
hypothesis = X * W + b

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

#t = [1. , 2. , 3. , 4.]
#tf.reduce_mean(t) ==> 2.5 평균을 내주는 명령어

# GradientDescent (Minimize/optimizer)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)



#2. Run/update 세션#

# Launch the graph in a session.
sess = tf.Session()

# Initializes global variables in the graph.
sess.run(tf.global_variables_initializer())

# Fit the line
for step in range(2001):
    cost_val, W_val, b_val, _ = sess.run([cost, W, b, train], feed_dict={X: [1, 2, 3, 4, 5], Y: [2.1, 3.1, 4.1, 5.1, 6.1]})
#                                 feed_dict를 이용해서 입력값을 넣을 수 있음
    if step % 20 == 0:
        print(step, cost_val, W_val, b_val)


# Testing our model
print(sess.run(hypothesis, feed_dict={X: [5]}))
print(sess.run(hypothesis, feed_dict={X: [2.5]}))
print(sess.run(hypothesis, feed_dict={X: [1.5, 3.5]}))

