import tensorflow as tf

a = tf.constant(5, name="input_a")
b = tf.constant(3, name="input_b")
c = tf.add(a, b, name="add_c")
sess = tf.Session()
sess.run(c)
writer = tf.summary.FileWriter("../my_graph", sess.graph)
writer.close()
sess.close()
