import tensorflow as tf

# Create a constant op #tf를 불러온다.
# This op is added as a node to the default graph #constant를 불러온다 .
hello = tf.constant("Hello, TensorFlow!")

# start a TF session #실행을 위해 세션을 만듦
sess = tf.Session()

# run the op and get result
print(sess.run(hello))

#출력 : b'Hello, TensorFlow!' #b는 bytestream
