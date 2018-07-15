import tensorflow as tf

my_var = tf.Variable(1)
sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(my_var))
writer = tf.summary.FileWriter("C:\\Users\\dell\\PycharmProjects\\tensorflow\\my_graph", tf.get_default_graph())
writer.close()
