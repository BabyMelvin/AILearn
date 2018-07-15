import tensorflow as tf
import sys


def python_original_data():
    # 0阶张量或“标量”
    t_0 = 50
    # 1阶张量或"向量"
    t_1 = [b"apple", b"peach", b"graph"]
    # 2阶张量或"矩阵"
    t_2 = [[True, False],
           [False, True]]
    # 3阶张量
    t_3 = [[0, 1], [1, 2],
           [1, 2], [2, 3]]


def tensor_shape():
    t_3 = [[0, 1], [1, 2],
           [1, 2], [2, 3]]
    # 获取张量的形状
    # 注意：和其他Op一样，tf.shape只能通过Session对象得到执行
    shape = tf.shape(t_3, name="t_3")


def tensor_flow_graph():
    # 当tensorflow被加载会创建一个默认的Graphic对象
    default_graph = tf.get_default_graph()

    # 创建一个新的数据流图
    g = tf.Graph()

    # 利用Graphic.as_default访问其上下文管理器
    # 在with内部则放入g,否则放在default_graph
    with g.as_default():
        # 象往常一样创建一些操作，添加到Graph对象g中
        a = tf.mul(2, 3)

    # 其他Tensorflow脚本文件加载之前的定义模型，利用Graphic.as_graph_def()和tf.import_graph_def()
    # 函数将其赋给Graph对象也是可行的。


def tensor_flow_session():
    # session负责数据流图的执行
    # tf.Session()接收三个参数
    # target:大多数这个默认为空。分布式设置，改参数用于连接不同的tf.train.Server实例
    # graph:指定要加载的Graph对象，默认为None，表示当前默认数据流图。
    # 当使用多个数据流图时，最好方式是显示传入你的graph对象(而不是一个with一个session)
    # config:允许用户指定配置Session所需选项，如限制CPU或GPU使用数目，为数据流图设置优化参数及日志选项等

    a = tf.constant(3)
    b = tf.constant(4)
    c = tf.multiply(a, b)
    # 等价 sess = tf.Session(graph=tf.get_default_graph())
    sess = tf.Session()
    sess.run(c)  # 得到计算结果

    # Session.run()三个可选参数：feed_dict,options,run_metadata
    # 1.fetches参数，接收任意流图元素(Op或Tensor对象)
    # 请求时Tensor对象，run()返回一数组

    # 一个对象Op,则输出将为None
    sess.run([a, b])  # 返回[3,4]

    # 执行初始化Variable，单发挥值为None
    sess.run(tf.initialize_all_variables())

    # 2.feed_dict参数
    # feed_dict用于覆盖数据流图中Tensor对象，Python字典作为输入。
    replace_dict = {a: 15}
    print(sess.run(c, feed_dict=replace_dict))  # 返回19

    # 使用完要关闭
    sess1 = tf.Session()
    sess1.close()

    # 用with语句,无需close
    with tf.Session() as sess:
        pass

    # with语句中改Session默认对象，则需要手动关闭
    with sess.as_default():
        a.eval()
    # 必须手公关闭Session对象
    sess.close()


def placeholder_add_input():
    # 接收输入值。作用预留运行Tensor位置，输入节点
    # 创建一个长度为2，数据类型为int32占位向量
    a = tf.placeholder(tf.int32, shape=[2], name="my_input")
    # 将改占位向量视为其他任意Tensor对象：
    b = tf.reduce_prod(a, name="prod_b")
    c = tf.reduce_sum(a, name='sum_c')

    # 完成数据流图定义
    d = tf.add(b, c, name="add_d")

    # placeholder参数dtype是必选参数，而shape是可选参数


def variable():
    #   Variable:可变的变量（Tensor对象和Op对象是不可变的）
    # 1.为variable对象传入一个初始值为3
    my_var = tf.Variable(3, name="my_variable")
    add = tf.add(5, my_var)
    mul = tf.multiply(8, my_var)

    # 2.手动初始化
    # 2x2零矩阵
    zeros = tf.zeros([2, 2])

    # 长度为6的全1向量
    ones = tf.ones([6])
    # 3x3x3的张量，其元素服从0~10均匀分布
    uniform = tf.random_uniform([3, 3, 3], minval=0, maxval=10)
    # 3x3x3张量，其元素服从0均值，标准差为2的正太分布
    normal = tf.random_normal([3, 3, 3], mean=0, stddev=2.0)

    # truncate_normal:创建不超过均值2倍标准差的值,避免产生显著不同的情况
    # Tensor对象不会返回任何小于3.0或大于7.0的值
    trunc = tf.truncated_normal([2, 2], mean=5.0, stddev=1.0)
    # 手工初始化值，可传给Variable对象
    # 默认均值为0，默认标准差为1.0
    random_var = tf.Variable(tf.truncated_normal([2, 2]))

    # Variable装态是由Session管理。利用Session内部初始化，便于追踪其值
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    # 对其中子集进行初始化
    var1 = tf.Variable(0, name="initialize_me")
    var2 = tf.Variable(1, name="no_initialization")
    init = tf.variables_initializer([var1], name="init_var1")
    sess.run(init)

    # 3.对象修改
    # Variable.assign()方法进行修改，是一个Op,要在Session对象中运行
    # 创建一个初始值为1的Variable对象
    my_var = tf.Variable(1)
    # 创建一个Op,使其每次运行时都将改Variable对象乘以2
    my_var_times_two = my_var.assign(my_var * 2)  # 还回Op
    # 初始化
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    # 返回2
    print(sess.run(my_var_times_two))
    # 返回4
    print(sess.run(my_var_times_two))
    # 返回8
    print(sess.run(my_var_times_two))
    # 自增1,9
    print(sess.run(my_var.assign_add(1)))
    # 自增1,10
    print(sess.run(my_var.assign_add(1)))
    # 自减1，9
    print(sess.run(my_var.assign_sub(1)))
    # 自减1,8
    print(sess.run(my_var.assign_sub(1)))

    #不同的Session维护独立的变量值，在Graph对象中定义Variable对象的当前值.
    # 创建一些Op
    my_var = tf.Variable(0)
    init = tf.global_variables_initializer()
    # 启动多个Session对象
    sess1 = tf.Session()
    sess2 = tf.Session()

    # sess1内对Variable对象进行初始化，对同一个对象进行改变
    sess1.run(init)
    # 返回5
    print(sess1.run(my_var.assign_add(5)), sys._getframe().f_lineno)
    # sess2内部做相同的运算，但是用不同的自增值
    sess2.run(init)
    # 返回2
    print(sess2.run(my_var.assign_add(2)), sys._getframe().f_lineno)

    # 返回10
    print(sess1.run(my_var.assign_add(5)), sys._getframe().f_lineno)
    # 返回4
    print(sess2.run(my_var.assign_add(2)), sys._getframe().f_lineno)

    # Variable对象重置为初始值，再次调用tf.global_variables_initializer()
    # 某个变量初始值tf.initialize_variables()

    # 创建Op
    my_var = tf.Variable(1)
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    # 修改变量值
    print(sess.run(my_var.assign(10)), sys._getframe().f_lineno)
    # 初始化Variable对象
    sess.run(init)
    print(sess.run(my_var), sys._getframe().f_lineno)

    # 4.trainable
    #Optimizer类中，自动修改Variable对象的值，无须显示做出请求。
    #允许将变量设置成手动修改的变量,trainable
    not_trainable = tf.Variable(0, trainable=False)
