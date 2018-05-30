import tensorflow as tf
import __future__ as print_function

"""
    TensorFlow core programs ,two discrete section:
        1.build the computational graph
        2.running the computational graph
"""
"""
    tensor:
        3           # a rank 0 tensor; a scalar with shape[]      
        [1,2,3]     #a rank 1 tensor;a vector with shape [3]
        [[1,2,3],[4,5,6]] # a rank 2 tensor; a matrix with shape [2,3]
        [[[1,2,3]],[[4,5,6]]]# a rank 3 tensor with shape [2,1,3]
"""
# nodes: inputs zero or more tensor,output zero or more tensor

# constant(one type of node):input->no,output->a value(store internally)
# 1.build
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0)
print(node1, node2)
# 2.run,session:runtime of control and state TensorFlow
sess = tf.Session()
print(sess.run([node1, node2]))

# operations(one type of node)
node3 = tf.add(node1, node2)
print("node3:", node3)
print("sess.run(node3)", sess.run(node3))

# placeholder：accept external inputs as parameters
# lambda like.  method:adder_node,param:dict
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + is shortcut for tf.add(a,b)
print(sess.run(adder_node, {a: 3, b: 4.5}))
print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))

add_and_triple = adder_node * 3
print(sess.run(add_and_triple, {a: 3, b: 4.5}))

# Variables:allow us add trainable parameters to a graph
# model trainable need modify the graph to get the same outputs with inputs
W = tf.Variable([-1.], dtype=tf.float32)
b = tf.Variable([1.], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b
# initialize the variable,handle the sub-graph initialize all the global variable
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(linear_model, {x: [1, 2, 3, 4]}))

# loss 07-function,x as the model outputs,y placeholder as desire values.
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))
# machine learning whole point:find the correct model parameters(such:W,b) automatically



