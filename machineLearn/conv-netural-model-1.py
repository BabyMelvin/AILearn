import tensorflow as tf
import numpy as np

"""
    多幅图像所需信息
        image_batch_size 
        image_height     
        image_width
        image_channels
"""
image_batch = tf.constant([
    [  # 第1幅图
        [[0, 255, 0], [0, 255, 0], [0, 255, 0]],
        [[0, 255, 0], [0, 255, 0], [0, 255, 0]],
    ],
    [  # 第二幅图
        [[0, 0, 255], [0, 0, 255], [0, 0, 255]],
        [[0, 0, 255], [0, 0, 255], [0, 0, 255]]
    ]
])

print(image_batch.get_shape())
# (2,2,3,3)-》（几幅图，高度[像素],宽度[像素],像素格式)->(image_channels,image_height,image_width,image_batch_size)
with tf.Session() as sess:
    print(sess.run(image_batch)[0][0][0])  # 第一个像素点

# 输入和卷积核
input_batch = tf.constant([
    [  # 第一个输入
        [[0.0], [1.0]],
        [[2.0], [3.0]]
    ],
    [  # 第二个输入
        [[2.0], [4.0]],
        [[6.0], [8.0]]
    ]
])
# 卷积核，也称为权值，滤波器，卷积矩阵或模板(filter)
# 该卷积核作用第一通道不变，第二通道放大两倍 [R,G,B]三个通道
kernel = tf.constant([
    [
        [[1.0, 2.0]]
    ]
])
with tf.Session() as sess:
    conv2d = tf.nn.conv2d(input_batch, kernel, strides=[1, 1, 1, 1], padding='SAME')
    print(sess.run(conv2d))
    # 查看对应像素点转换后的值
    low_right_image_pixel = sess.run(input_batch)[0, 1, 1]
    low_right_image_kernel_pixel = sess.run(conv2d)[0, 1, 1]
    print('-' * 40)
    print(low_right_image_pixel, low_right_image_kernel_pixel)

# 跨度
# 计算机视觉上，卷积价值体现在降维上
"""
    2D图像维度包括宽度，高度和通道数。维度和运算时间成指数级
    对图像的降维是通过修改卷积核strides(跨度)参数实现的
"""
input_batch1 = tf.constant([
    [  # 第1个输入(1x6x6x1)
        [[0.0], [1.0], [2.0], [3.0], [4.0], [5.0]],
        [[0.1], [1.1], [2.1], [3.1], [4.1], [5.1]],
        [[0.2], [1.2], [2.2], [3.2], [4.2], [5.2]],
        [[0.3], [1.3], [2.3], [3.3], [4.3], [5.3]],
        [[0.4], [1.4], [2.4], [3.4], [4.4], [5.4]],
        [[0.5], [1.5], [2.5], [3.5], [4.5], [5.5]],
    ],
])
kernel1 = tf.constant([  # 卷积核3X3x1
    [
        [[0.0], [0.5], [0.0]],
        [[0.0], [1.0], [0.0]],
        [[0.0], [0.5], [0.0]],
    ],
])

# 设置跨度与输入向量相同(image_batch_size_stride,image_height_strike,image_width_stride,image_channels_strike),
#                    一般修改image_height_stride和image_width_stride参数
conv2d1 = tf.nn.conv2d(input_batch1, kernel1, strides=[1, 3, 3, 1], padding='SAME')
print('-' * 40)
sess = tf.Session()
print(sess.run(conv2d1))
print('*' * 20)
num = np.arange(9).reshape(3, 3, 1, 1)
print(num)

# 边界填充
# 当卷积核与图像重叠时，应当落在图像的边界内。两尺寸可能不匹配。好的补救方法进行图像缺失区域进行边界填充，边界填充
# TensorFlow会用0进行边界填充，或当不匹配是不允许填充，引发一个错误。
"""
    边界填充由padding参数控制
        SAME：卷积输出与输入尺寸相同，计算如何跨越图像时，不考虑滤波器的尺寸
            选用改设置，缺失的像素用0填充，卷积核扫过的像素将超过图像的实际像素
        VALID：在计算卷积核如何在图像上跨越时，需要考虑滤波器尺寸。
            使卷积核尽量不要超越图像的边界，某些情况下，可能边界也会被填充。
        
"""
"""
    数据格式
        输入张量不是[batch_size,height,width,channel]
        data_format: 指定输入和输出格式。默认NHWC
            N batchsize
            H height
            W width
            C channels
"""

"""
    深入卷积运算
        滤波器常用于调整图片的属性。
        摄影者之所以能够利用滤波器进行图片修改，因为滤波器能够识别到达透镜的光线特定属性。
            如。红色透镜滤波器会吸收（或阻止）不同于红色的每种频率的光，使得只有红色可通过该滤波器。
        
        计算机视觉中
            卷积核（滤波器）常用于识别数字图像中的重要属性。某些过滤器感兴趣特征图像中存在时，
        滤波器会使用特定模式突出的这些特征。如红色过滤器，除红色外将被减小
"""
kernel2 = tf.constant([
    [
        [[-1., 0., 0.], [0. - 1., 0.], [0., 0., -1.]],
        [[-1., 0., 0.], [0. - 1., 0.], [0., 0., -1.]],
        [[-1., 0., 0.], [0. - 1., 0.], [0., 0., -1.]]
    ],
    [
        [[-1., 0., 0.], [0. - 1., 0.], [0., 0., -1.]],
        [[8., 0., 0.], [0., 8., 0.], [0., 0., 8.]],
        [[-1., 0., 0.], [0., -1., 0.], [0., 0., -1.]]
    ],
    [
        [[-1., 0., 0.], [0. - 1., 0.], [0., 0., -1.]],
        [[-1., 0., 0.], [0. - 1., 0.], [0., 0., -1.]],
        [[-1., 0., 0.], [0. - 1., 0.], [0., 0., -1.]]
    ]
])
conv2d = tf.nn.conv2d(image_batch, kernel, [1, 1, 1, 1], padding="SAME")
# 调用tf.minimum和tf.nn.relu将卷积值保存在RGB颜色值合法范围[0,255]
activation_map = sess.run(tf.minimum(tf.nn.relu(conv2d)))

