# import tensorflow as tf

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

X = [1, 2, 3]
Y = [1, 2, 3]

#W = tf.placeholder(tf.float32)
W = tf.Variable(5.) #말도 안되는 W의 값을 넣고 제대로 가는지 확인

# Our hypothesis for linear model X * W
hypothesis = X * W

#===> Manual Gradient #
gradient = tf.reduce_mean((W * X- Y) * X) * 2

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer =  tf.train.GradientDescentOptimizer(learning_rate=0.1)

#===> Get Gradient #
gvs = optimizer.compute_gradients(cost)

# gvs 수정 해도됨 #

#===> Apply Gradients #
apply_gradients = optimizer.apply_gradients(gvs)


#sess = tf.Session()
#sess. run(tf.global_variables_initializer())
#sess 초기화 대체

# Launch the graph in a session.
with tf.Session() as sess:
    # Initializes global variables in the graph.
    sess.run(tf.global_variables_initializer())

    for step in range(100):
        print(step, sess.run([gradient, W, gvs] ))
              # 출력은 순서, [손으로한 gradient, W값, [컴퓨터의 gredient, w값]]
        sess.run(apply_gradients)

        

