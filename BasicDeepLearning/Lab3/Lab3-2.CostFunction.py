import tensorflow as tf
import matplotlib.pyplot as plt

X = [1, 2, 3]
Y = [1, 2, 3]

W = tf.placeholder(tf.float32)

# Our hypothesis for linear model X * W
hypothesis = X * W

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

#sess = tf.Session()
#sess. run(tf.global_variables_initializer())
#sess 초기화 대체

# Variables for plotting cost function
# W와 cost값을 받을 리스트를 생성
W_history = [] 
cost_history = []

# Launch the graph in a session.
with tf.Session() as sess: #sess초기화를 위한 구간
    for i in range(-30, 50):
        curr_W = i * 0.1 #-3에서 5까지, 0.1간격으로 움직이겠다.
        #curr_cost = sess.run([cost, W], feed_dict={W: curr_W})
        curr_cost = sess.run(cost, feed_dict={W: curr_W})

        W_history.append(curr_W)
        cost_history.append(curr_cost)

# Show the cost function
plt.plot(W_history, cost_history)
plt.show()
