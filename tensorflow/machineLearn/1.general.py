import tensorflow as tf
import os

"""
    监督学习的模型代码
"""
"""
    Saver类将数据流图中变量保存到专门二进制文件中
        需要周期保存所有变量，创建检查点(checkPoint）文件
        必要时从最近检查点恢复训练
"""


# 初始化变量和模型参数,定义训练闭环中的运算
def inference(X):
    # 计算推断模型和在哪个数据X上的输出，并将结果返回
    return


def loss(X, Y):
    # 依赖训练数据X及其期望输出的Y计算损失
    return


def inputs():
    # 读取或生成训练数据X及其期望输出Y
    return


def train(totoal_loss):
    # 依据计算的损失训练或调整模型参数
    return


def evaluate(sess, X, Y):
    # 对训练得到的模型进行评估
    return


# 创建一个Saver对象
saver = tf.train.Saver()

# 在一个会话对象中启动数据流图，搭建流程
with tf.Session() as sess:
    initial_step = 0
    # 验证之前是否已经保存了检查点文件
    ckpt = tf.train.get_checkpoint_state(os.path.dirname(__file__))
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
            saver.save(sess, 'my-model', global_step=step)
    # 模型评估
    evaluate(sess, X, Y)
    saver.save(sess, 'my-model', global_step=training_steps)

    coord.request_stop()
    coord.join()
    sess.close()
