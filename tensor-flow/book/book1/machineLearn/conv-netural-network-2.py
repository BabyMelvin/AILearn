import tensorflow as tf

"""
    CNN：至少包含一个卷积层。单层CNN一种实际用途是检测边缘。
        图像识别和分类任务,使用不同层类型支持某个卷积层，降低拟合，加速训练。
    CNN可以和其他网络架构设计混合使用
"""
# 常见层
# 卷积层
"""
    1.tf.nn.conv2d(),TensorFlow采用一种对不同类型卷积层运算，加速技术
    2.tf.nn.depthwise_conv2d()
        将一个卷积层作为输出连接到另一个卷积层输入时
    3.tf.nn.separable_conv2d()
        与tf.nn.conv2d()类似，规模较大的模型，在不牺牲准确性前提下实现训练加速。
        加快收敛，但准确较低
    4.tf.nn.conv2d_transpose
        将一个卷积核运用于新的特征图。特征图中每一部分都填充了卷积核相同的值。
    当该卷积遍历新图像时，任何重叠部分都相加在一起，用于降采样的问题。

"""
# 激活函数
"""
    这些函数与其它层的输出联合使用可生成特征图。
    作用：某些运算的结果进行平滑(或微分)。
    目标：为神经网络引入非线性，非线性能够刻画输入中更为复杂的变化。
        非线性能够描述那些大部分时间都很少，但某单点周期性出现极值的输入。
    
    用户可以自定义激活函数，几个因素：
     1.单调性。 输出随增长而增长，可利用梯度下降法寻找局部极值点
     2.可微分。 保证定义域任意一点可导，从而使得梯度下降法能够正常使用来自这类激活函数的输出。
"""
# 1.tf.nn.relu ，修正线性单元也被称为斜坡函数，函数图形与滑板斜坡非常相似
# ReLU是分段线性的。
# 输入为非负：输出与输入相同
# 输入为负  : 输出为0
# 优点：不受梯度消失影响。且取值范围[0,+∞]
# 缺点：较大学习效率，易受到饱和神经元影响
features = tf.range(-2, 3)
sess = tf.Session()
print(sess.run([features, tf.nn.relu(features)]))
# [array([-2, -1,  0,  1,  2]), array([0, 0, 0, 1, 2])]

# 2.tf.sigmoid，返回值[0.0,1.0].输入较大趋于1，输入较小趋于0.
# tf.sigmoid(tf.nn.sigmoid) 目前仅支持接收浮点
features0 = tf.to_float(tf.range(-1, 3))
print(sess.run([features0, tf.sigmoid(features0)]))
# [array([-1.,  0.,  1.,  2.], dtype=float32), array([0.26894143, 0.5       , 0.7310586 , 0.880797  ], dtype=float32)]


# 3.tf.tanh,双曲正切函数(tanh)与tf.sigmoid非常接近，优缺点相类似。
# 值域为[-1,1]，特定网络架构中能够输出赋值的能力可能非常有用
# tf.tanh(tf.nn.tanh)目前只支持浮点类型输入
features1 = tf.to_float(tf.range(-1, 3))
print(sess.run([features1, tf.tanh(features1)]))
# [array([-1.,  0.,  1.,  2.], dtype=float32), array([-0.7615942,  0.       ,  0.7615942,  0.9640276], dtype=float32)]

# 4.tf.nn.dropout,根据某个可配置概率输出设为0.0
# 引入少量随机性有助于训练
# 场景:当要学习一些模式与其邻近特征耦合过强，将输出添加少量噪声

# 这种模型应该只在训练层使用。如果在测试阶段使用该层，引入随机噪声将对齐结果产生误导。
features2 = tf.constant([-0.1, 0.0, 0.1, 0.2])
print(sess.run([features2, tf.nn.dropout(features2, keep_prob=0.5)]))

# 池化层
"""
    能够减少过拟合，并通过减小输入尺寸来提高性能。
    可用于对输入降采样，但会为后续层保留重要信息。
    只是用tf.nn.conv2d来减少输入也是可以的，但池化层效率更高。
    最大池化：
        利用2x2接受域（高度和宽度均为2卷积核）完成。使用2x2接收域原因是单个通路上能够实施最小数量降采率
    1x1接受域，则输出将于输入相同
"""
# 1.tf.nn.max_pool,跳跃遍历某个张量，并从卷积核覆盖的元素中找出最大的数值作为卷积结果。
# 当输入数据的灰度与图像中重要特性相关时，这种池化方式非常有用。
# 输入通常为前一层的输出，而非直接为图像
batch_size = 1
input_height = 3
input_width = 3
input_channels = 1
# layer_input类似于tf.nn.conv2d某个激活函数输出张量，目标仅保留一个值，张量中最大元素。
layer_input = tf.constant([
    [
        [[1.0], [0.2], [1.5]],
        [[0.1], [1.2], [1.4]],
        [[1.1], [0.4], [0.4]]
    ]
])
# strides会使用image_height和image_width遍历整个输入
kernel = [batch_size, input_height, input_width, input_channels]
max_pool = tf.nn.max_pool(layer_input, kernel, [1, 1, 1, 1], padding="VALID")
print(sess.run(max_pool))

# 2.tf.nn.avg_pool,跳跃遍历一个张量，并被卷积核覆盖的各深度值取平均。都很重要时，平均池化。
# 例如，输入张量宽度和高度很大，但是深度很小的情况。
batch_size1 = 1
input_height1 = 3
input_width1 = 3
input_channels1 = 1
layer_input1 = tf.constant([
    [
        [[1.0], [1.0], [1.0]],
        [[1.0], [0.5], [0.0]],
        [[0.0], [0.0], [0.0]]
    ]
])
# strides会使用image_height和image_width遍历整个输入
kernel1 = [batch_size1, input_height1, input_width1, input_channels1]
max_pool1 = tf.nn.avg_pool(layer_input1, kernel1, [1, 1, 1, 1], "VALID")
print(sess.run(max_pool1))

# 归一化
# 归一化非CNN所独有。ReLU是无界函数，利用某些形式归一化识别那些高频特征十分有用的。
# tf.nn.local_normalization(tf.nn.lm)
# 局部响应归一化是一个依据求和操作而形输出函数。在某个给定向量中，每个分量都被depth_radius覆盖的输入的加权和所除。
# 归一化目标之一将输入保持在一个可接受的范围内。如[0,1]
# 创建一组浮点数值
layer_input2 = tf.constant([
    [[[1.]], [[2.]], [[3.]]]
])
lrn = tf.nn.local_response_normalization(layer_input2)
print(sess.run([layer_input, lrn]))

# 高级层
"""
    为使标准层定在创建时简单，TensorFlow引入一些高级网络层。
    这些曾不是必须的，有助于减少代码冗余，遵循最佳实践
"""
# 1.tf.contrib.layer.convolution2d
# 类似tf.nn.con2d逻辑相同，包含权值初始化，偏置初始化，可训练变量输出，偏置相加以及添加激活函数的功能。
# CNN目标是训练卷积核
# 权值初始化用于卷积核首次运行时填充，tf.truncated_normal
# 其余与之前类似
image_input = tf.constant([
    [
        [[0., 0., 0.], [255, 255., 255.], [254., 0., 0.]],
        [[0., 191., 0.], [3., 108., 233.], [0., 191., 0.]],
        [[254., 0., 0.], [255., 255., 255.], [0., 0., 0.]]
    ]
])
conv2d = tf.contrib.layers.convolution2d(
    image_input,
    num_outputs=4,
    kernel_size=(1, 1),  # 仅有录波器高度和宽度
    activation_fn=tf.nn.relu,
    stride=(1, 1),  # 对image_batch和input_channels跨度值
    trainable=True
)
# 有必要对在convolution2d的设置中所使用的变量初始化
sess.run(tf.global_variables_initializer())
print(sess.run(conv2d))

# 2.tf.contrib.layers.fully_connected
# 全连接层，每个输入与每个输出都存在连接。CNN最后一层通常为全连层。
# TensorFlow全连层格式tf.matmul(features,weight)+bias
# feature，weight和bias均为张量。
features = tf.constant([
    [[1.2], [3.4]]
])
fc = tf.contrib.layers.fully_connected(features,
                                       num_outputs=2)
sess.run(tf.global_variables_initializer())
print(sess.run(fc))

# 输入层
"""
    无论是训练还是测试，原始输入都是需要传递给输入层。
对目标识别与分类，输入层为tf.nn.conv2d，负责接收图像。
"""
