import tensorflow as tf
import os

"""
线性回归模型：
    预测一个连续值或任意实数
    1.线性函数一般表示为
        y(x1,x2,...,xK)=w1*x1+w2*x2+...+wk*xk+b
        其矩阵形式
        Y=XW.T+b,其中X=（x1,x2,...,xk),W=(w1,w2,w3...)
        含义：
            Y带预测值
            x1,x2,...,xk独立一组独立预测变量
                新样本预测时，需提供这些值。
                矩阵形式，一次提供多个样本，每一样对应一个样本。
            w1,w2,w3...,wk.模型训练参数，或赋予每个变量的“权值”
            b也是一个学习的参数，模型的偏置（bias)
    2.最小损失目标
        loss=sum(numpy.square(yI-y_predictedI)
"""
# 初始化模型参数
W = tf.Variable(tf.zeros([2, 1]), name="weights")
b = tf.Variable(0., name="bias")


def inference(X):
    return tf.matmul(X, W) + b


def loss(X, Y):
    Y_predicted = inference(X)
    return tf.reduce_sum(tf.squared_difference(Y, Y_predicted))


# 年龄-体重 和 血液-脂肪含量
def inputs():
    weight_age = [[84, 46], [73, 20], [65, 52], [70, 30],
                  [76, 57], [69, 25], [63, 28], [72, 36], [79, 57], [75, 44],
                  [27, 24], [89, 31], [65, 52], [57, 23], [59, 60], [69, 48],
                  [60, 34], [79, 51], [75, 50], [82, 34], [59, 46], [67, 23],
                  [85, 37], [55, 40], [63, 30]]
    blood_fat_content = [354, 190, 405, 263, 451, 302, 288,
                         385, 402, 365, 209, 290, 346, 254, 395, 434, 220, 374, 308,
                         220, 311, 181, 274, 303, 244]
    return tf.to_float(weight_age), tf.to_float(blood_fat_content)


def train(total_loss):
    learning_rate = 0.0000001
    return tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(total_loss)


def evaluate(sess1, X1, Y1):
    print(sess.run(inference([[80., 25.]])))
    print(sess.run(inference([[65., 25.]])))


# 创建一个Saver对象
saver = tf.train.Saver()

# 在一个会话对象中启动数据流图，搭建流程
with tf.Session() as sess:
    initial_step = 0
    # 验证之前是否已经保存了检查点文件
    # ckpt = tf.train.get_checkpoint_state(os.path.dirname(__file__) + '/my-model/')
    ckpt = tf.train.get_checkpoint_state(
        "C:\\Users\\dell\\PycharmProjects\\tensorflow\\machineLearn\\my-model\\\\-1000")
    print(os.path.dirname(__file__) + '/my-model/')
    if ckpt and ckpt.model_checkpoint_path:
        # 检查点恢复模型参数
        saver.restore(sess, ckpt.model_checkpoint_path)
        initial_step = int(ckpt.model_checkpoint_path.rsplit('-')[1])
    sess.run(tf.global_variables_initializer())
    X, Y = inputs()
    total_loss = loss(X, Y)
    train_op = train(total_loss)
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    # 实际的训练迭代次数
    training_steps = 1000
    for step in range(initial_step, training_steps):
        sess.run([train_op])
        # 学习的目的，查看损失在训练过程递减过程
        if step % 10 == 0:
            print("loss:", sess.run([total_loss]))
        if step % 100 == 0:
            saver.save(sess, r'C:\Users\dell\PycharmProjects\tensorflow\machineLearn\my-model\\', global_step=step)
    # 模型评估
    evaluate(sess, X, Y)
    saver.save(sess, r'C:\Users\dell\PycharmProjects\tensorflow\machineLearn\my-model\\', global_step=training_steps)

    coord.request_stop()
    coord.join()
    sess.close()
