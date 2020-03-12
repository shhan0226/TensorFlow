import tensorflow as tf

X = [1, 2, 3]
Y = [1, 2, 3]

# W = tf.placeholder(tf.float32)
W = tf.Variable(-3.0)  # 말도 안되는 W의 값을 넣고 제대로 가는지 확인

# Our hypothesis for linear model X * W
hypothesis = X * W

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize: Gradient Desent Maigc
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)

# sess = tf.Session()
# sess. run(tf.global_variables_initializer())
# sess 초기화 대체

# Launch the graph in a session.
with tf.Session() as sess:
    # Initializes global variables in the graph.
    sess.run(tf.global_variables_initializer())

    for step in range(100):
        print(step, sess.run(W))
        sess.run(train)



