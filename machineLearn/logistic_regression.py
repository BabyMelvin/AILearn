import tensorflow as tf
import os

"""
对数几率回归 
    回答Yes-No模型（垃圾邮件分类)
    1.logistic函数也称为sigmoid函数(S型函数)
        f(x)=1/(1+exp(-x))
        a.是一个概率分布函数
            给定特定输入，函数计算输出为"success" 概率,"Yes"概率
        b.函数就收单个值
            接收多维数据或自训练集样本特征，需将他们合并为单个值。
            可利用线性回归模型实现
    2.loss函数
       logistic函数会计算回答“YES”的概率。 
       a.平方误差
            训练集中，“YES”回答代表100%概率，或者值为1.
        损失应当刻画对于特定样本，模型为其分配一个小于1值的概率.
        回答为“NO”将表示概率值为0，损失模型为那个样本的概率并取平方值
        分析:
            建设样本期望输出为“YES",但是模型预测一个非常低接近于0的概率，意味着几乎100%地认为回答为”NO"
            平方误差所惩罚是与损失为同一个数量级情形，好比"NO"输出赋予概率20%,30%,甚至50%
       b.cross_entropy交叉熵
            loss=sum(yI*log(y_predicted)+(1-yI)*log(1-y_predicted))
            借助交叉熵，当模型对期望输出为"YES"样本预测为0是，惩罚项趋于无穷大。这样不可能发生，这使得交叉熵更适合模型函数
    3.属性数据(categorical data)
         a.船票等级和性别都属于字符串特征，取值来自一个预定的集合。
         为了推断数据，需要转化成数值型特征。
         
         b.错误的做法：如果为每个可能取值分配一个数值如，1：一等，2:二等，3：三等。不能认为3等是1等的3倍。 强加了一种线性关系。
         正确做法看成是独立的，扩展N维布尔型,每个取值对应1维。
         c.使用属性数据时，通常先将其转换为多维布尔型，每个可能取值对应一维。
            这使得模型能够取值独立加权
         对于智能取两个值属性，单个变量表示已经足够。因为属性键存在线性关系。如,male+female=1
"""

# 与对数几率回归相同的参数和变量初始化
W = tf.Variable(tf.zeros([5, 1]), name="weights")
b = tf.Variable(0., name="bias")


# 之前推断用于值的合并
def combine_inputs(X2):
    return tf.matmul(X2, W) + b


# 新的推断值是将sigmiod函数运用到前面合并值输出
def inference(X):
    return tf.sigmoid(combine_inputs(X))


# 单个优化步骤中直接为一个sigmoid函数计算交叉熵的方法
def loss(X, Y):
    return tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=combine_inputs(X), labels=Y))


# 读写文件基本代码,创建一个批次来读取排列在某个张量中多行数据
def read_csv(batch_size, file_name, record_defaults):
    file_name_queue = tf.train.string_input_producer([os.path.dirname(__file__) + "\\" + file_name])
    reader = tf.TextLineReader(skip_header_lines=1)
    key, value = reader.read(file_name_queue)
    # decode_csv会将字符串（文本行）转换到由张量列构成具有指定默认值元组中，还会为每一列设置数据类型
    decoded = tf.decode_csv(value, record_defaults=record_defaults)
    # 实际上会读取一个文件，并加载一个张量中的batch_size行
    return tf.train.shuffle_batch(decoded, batch_size=batch_size, capacity=batch_size * 50,
                                  min_after_dequeue=batch_size)


def inputs():
    passenger_id, survived, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked = \
        read_csv(100, "train.csv", [[0.0], [0.0], [0], [""], [""], [0.0], [0.0], [0.0], [""], [0.0], [""], [""]])
    # 转换属性数据
    is_first_class = tf.to_float(tf.equal(pclass, [1]))
    is_second_class = tf.to_float(tf.equal(pclass, [2]))
    is_third_class = tf.to_float(tf.equal(pclass, [3]))
    gender = tf.to_float(tf.equal(sex, ["female"]))
    # 最终将所有特征排列在一个矩阵中，然后转置，使其没行对应一个样本，每列对应一种特征。
    features = tf.transpose(tf.stack([is_first_class, is_second_class, is_third_class, gender, age]))
    survived = tf.reshape(survived, [100, 1])
    return features, survived


def train(total_loss):
    learning_rate = 0.01
    return tf.train.GradientDescentOptimizer(learning_rate).minimize(total_loss)


# 结果评估，对训练集中一些数据进行推断，并统计已经正确预测样本总数。这方法叫做度量准确率
def evaluate(sess1, X1, Y1):
    predicted = tf.cast(inference(X1) > 0.5, tf.float32)
    # reduce_mean正确预测样本数，并除以该批次中样本总数
    print(sess1.run(tf.reduce_mean(tf.cast(tf.equal(predicted, Y1), tf.float32))))


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
