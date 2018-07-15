import tensorflow as tf
import sys

"""
    打印文本信息
"""
print("文件名:", sys._getframe().f_code.co_filename)
print("当前函数:", sys._getframe().f_code.co_name)
print("当前行号:", sys._getframe().f_lineno)
"""
    Variable
        可变的变量（Tensor对象和Op对象是不可变的）
"""

my_var = tf.Variable(3, name="my_variable")
add = tf.add(5, my_var)
mul = tf.multiply(8, my_var)
"""
    手动初始化
"""
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

"""
    对象修改
    Variable.assign()方法进行修改，是一个Op,要在Session对象中运行
"""
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

"""
    不同的Session维护独立的变量值，在Graph对象中定义Variable对象的当前值.
"""
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

"""
    Variable对象重置为初始值，再次调用tf.global_variables_initializer()
    某个变量初始值tf.initialize_variables()
"""

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

"""
 trainable
    Optimizer类中，自动修改Variable对象的值，无须显示做出请求。
    允许将变量设置成手动修改的变量,trainable
"""
not_trainable = tf.Variable(0, trainable=False)
