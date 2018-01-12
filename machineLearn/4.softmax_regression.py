import tensorflow as tf
import os
from logistic_regression import read_csv

"""
对数几率回归，对YES-NO型回答进行建模,大于2个选择用softmax分类
    1.softmax函数,C个可能不同值上的推广
        f(x)C=exp(-xC)/sum(exp(-xJ)) (C和J为下标:j=0-C-1)
        a.函数返回值含有C个分量概率向量，每个分量对应一个输出类别概率。
        b.各个分量为概率，C个分量之后始终为1. 这是因为softmax每个样本必须属于某个输出类别
            ，且所有可能的样本均被覆盖。
            各个分量之和小于1，存在一些隐藏类别。
            各个分量之和大于1，可能同时属于多个类别
        c.可以证明类别总数为2时，所得到输出概率与对数几何概率回归模型相同
        
"""
# 数据集中包含4个数据特征及3个输出类型，权值矩阵的维数为4X3
"""
Y=X.W+b(x1,x2,x3,x4): 4个特征值
Y(1x3)=X(1X4)*W(4x3)+b(1x3)
zeros[4,3]=
       [0., 0., 0.]
       [0., 0., 0.]
       [0., 0., 0.]
       [0., 0., 0.]
       zeros[3]=[0,0,0]
"""
# 此时权值构成一个矩阵，而非向量，每个“特征权值列”对应一个输出类别
W = tf.Variable(tf.zeros([4, 3]), name="weights")
# 偏置也是如此，每个偏置对应一个输出类
b = tf.Variable(tf.zeros([3]), name="bias")


def combine_inputs(X):
    return tf.matmul(X, W) + b


def inference(X):
    return tf.nn.softmax(combine_inputs(X))


def loss(X, Y):
    return tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=combine_inputs(X), labels=Y))


"""
另一种形式每个样本属性类别的概率信息训练集
def loss(X, Y):
    return tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(combine_inputs(X), Y))
"""


def train(total_loss):
    learning_rate = 0.0001
    return tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(total_loss)


def inputs():
    sepal_length, sepal_width, petal_length, petal_width, label = \
        read_csv(100, "iris.data", [[0.0], [0.0], [0.0], [0.0], [""]])
    # 将类名称转化成从0开始计的类别名
    label_number = \
        tf.to_int32(tf.argmax(tf.to_int32(tf.stack([
            tf.equal(label, ["Iris-setosa"]),
            tf.equal(label, ["Iris-versicolor"]),
            tf.equal(label, ["Iris-virginica"])]
        )), 0))
    # 将所关心的所有特征装入单个矩阵中，然后对该矩阵转置，使得每个行对一个样本，每列对应一个特征
    features = tf.transpose(tf.stack([
        sepal_length, sepal_width, petal_length, petal_width
    ]))
    return features, label_number


def evaluate(sess, X, Y):
    # 最大概率类别进行评估
    predicted = tf.cast(tf.argmax(inference(X), 1), tf.int32)
    print(sess.run(tf.reduce_mean(tf.cast(tf.equal(predicted, Y), tf.float32))))


saver = tf.train.Saver()
with tf.Session() as sess:
    initial_step = 0
    # ckp = tf.train.get_checkpoint_state(os.path.dirname(__file__) + "\my-model")
    ckp = tf.train.get_checkpoint_state("C:\\Users\\dell\\PycharmProjects\\tensorflow\\machineLearn\\my-model\\\\-1000")
    if ckp and ckp.model_checkpoint_path:
        saver.restore(sess, ckp.model_checkpoint_path)
        initial_step = int(ckp.model_checkpoint_path.rsplit("-")[1])
    sess.run(tf.global_variables_initializer())
    X, Y = inputs()
    total_loss = loss(X, Y)
    train_op = train(total_loss)
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    train_steps = 1000
    for step in range(initial_step, train_steps):
        sess.run([train_op])
        if step % 100 == 0:
            saver.save(sess, r'C:\Users\dell\PycharmProjects\tensorflow\machineLearn\my-model\\', global_step=step)

    saver.save(sess, r'C:\Users\dell\PycharmProjects\tensorflow\machineLearn\my-model\\', global_step=train_steps)
    # 评估模型
    evaluate(sess, X, Y)
    coord.request_stop()
    coord.join()
    sess.close()
