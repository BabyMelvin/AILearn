import tensorflow as tf

"""
    名称作用域将Op划分为一些较大的，有名称的语句块
"""
with tf.name_scope("scope_A"):
    a = tf.add(1, 2, name="A_add")
    b = tf.multiply(a, 3, name="A_mul")

with tf.name_scope("scope_B"):
    c = tf.add(4, 5, name="B_add")
    d = tf.multiply(c, 6, name="B_mul")

e = tf.add(b, d, name="Output")

sess = tf.Session()
print(sess.run(e))
# tensorboard --logdir C:\Users\dell\PycharmProjects\tensorflow\my_graph
writer = tf.summary.FileWriter('C:\\Users\\dell\\PycharmProjects\\tensorflow\\my_graph', tf.get_default_graph())
writer.close()

"""
    可以将名称作用域嵌入在其他名称作用域内
"""

graph = tf.Graph()
with graph.as_default():
    in_1 = tf.placeholder(tf.float32, shape=[], name="input_a")
    in_2 = tf.placeholder(tf.float32, shape=[], name="input_b")
    const = tf.constant(3, dtype=tf.float32, name="static_value")
    with tf.name_scope("Transformation"):
        with tf.name_scope("A"):
            A_mul = tf.multiply(in_1, const)
            A_out = tf.subtract(A_mul, in_1)
        with tf.name_scope("B"):
            B_mul = tf.multiply(in_2, const)
            B_out = tf.subtract(B_mul, in_2)
        with tf.name_scope("C"):
            C_div = tf.div(B_out, A_out)
            C_out = tf.add(C_div, const)
        with tf.name_scope("D"):
            D_div = tf.div(B_out, A_out)
            D_out = tf.add(D_div, const)
            out = tf.maximum(C_out, D_out)
        writer = tf.summary.FileWriter('C:\\Users\\dell\\PycharmProjects\\tensorflow\\my_graph', graph=graph)
        writer.close()
