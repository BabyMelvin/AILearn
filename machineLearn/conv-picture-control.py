import tensorflow as tf

""" 
    图像操作最好预处理阶段完成
        预处理：图像裁剪、缩放、灰度调整等
    训练时对图像进行操作有一个重要,被加载后进行翻转或者扭曲处理，输入给网格训练信息化多样化。
    图像更丰富图像操作(PIL和OpenCV)
"""

# 1.裁剪
image_filename = "test-input-image.jpg"
filename_queue = tf.train.string_input_producer([image_filename])
reader = tf.WholeFileReader()
_, image_file = reader.read(filename_queue)
image = tf.image.decode_jpeg(image_file)
with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    print(sess.run(image))
    print("*" * 5 + "中心裁剪" + "*" * 5)
    print(sess.run(tf.image.central_crop(image, 0.1)))
    # 背景也有用，可随机裁剪区域起始位置裁剪
    real_image = sess.run(image)
    # 左上角开始裁剪
    bounding_crop = tf.image.crop_to_bounding_box(
        real_image, offset_height=0, offset_width=0,
        target_height=2, target_width=1
    )
    print("*" * 5 + "接收实值输入" + "*" * 5)
    print(sess.run(bounding_crop))
    coord.request_stop()
    coord.join(threads)
# 边界填充
"""
    为使得输入符合期望尺寸，可用0边界填充。
    对尺寸过小图像，该方法会围绕图像的边界填充一些灰度值为0的像素
    其他小尺寸图像会产生扭曲
"""
image_filename = "test-input-image.jpg"
filename_queue = tf.train.string_input_producer([image_filename])
reader = tf.WholeFileReader()
_, image_file = reader.read(filename_queue)
image = tf.image.decode_jpeg(image_file)
with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    print(sess.run(image))
    print("~" * 10)
    # 边界填充方法仅可接收实值输入
    real_image = sess.run(image)
    pad = tf.image.pad_to_bounding_box(
        real_image, offset_width=0, offset_height=0,
        target_height=4, target_width=4
    )
    print(sess.run(pad))
    # 调整长短不一多个图像时候用
    crop_or_pad = tf.image.resize_image_with_crop_or_pad(
        real_image, target_width=5, target_height=2
    )
    print("@" * 10)
    print(sess.run(crop_or_pad))
    coord.request_stop()
    coord.join(threads)
# 3.翻转
"""
    水平或垂直方向翻转
"""
image_filename = "test-input-image.jpg"
filename_queue = tf.train.string_input_producer([image_filename])
reader = tf.WholeFileReader()
_, image_file = reader.read(filename_queue)
image = tf.image.decode_jpeg(image_file)
top_left_pixels = tf.slice(image, [0, 0, 0], [2, 2, 3])
flip_horizon = tf.image.flip_left_right(top_left_pixels)
flip_vertical = tf.image.flip_up_down(flip_horizon)
with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    print("==" * 20)
    print(sess.run(image))
    print(sess.run([top_left_pixels, flip_vertical]))
    coord.request_stop()
    coord.join(threads)

# 4.饱和和平衡
"""
    互联网上的图片大多数经过处理过的编辑的。
    许多图片过饱和(大量彩色),可能会误导CNN模型去寻找那些与编辑过图像相关模式,而非本身的模式
    饱和度，色度，对比度，亮度调整
    不同光照条件进行调整图像
"""
# 红色为主的像素灰度值增加0.2
print("#" * 20)
example_red_pixel = tf.constant([254., 2., 15.])
adjust_brightness = tf.image.adjust_brightness(example_red_pixel, 0.2)
with tf.Session() as sess:
    print(sess.run(adjust_brightness))

image_filename = "test-input-image.jpg"
filename_queue = tf.train.string_input_producer([image_filename])
reader = tf.WholeFileReader()
_, image_file = reader.read(filename_queue)
image = tf.image.decode_jpeg(image_file)
# 调整对比度-0.5，生成一个识别度相当差的新图像。
# 调整对比度最好选择一个较小的增量避免对图像“过曝“
# 过曝：达到最大值而无法恢复。
# 对比度变化时，图像中像素可能会呈现出全白和全黑的情形
adjust_contract = tf.image.adjust_contrast(image, -.5)

# 调整色度
gray = tf.image.rgb_to_grayscale(image)

# 饱和度，很常见。增加饱和度突出颜色变化
adjust_saturation = tf.image.adjust_saturation(imag, 0.4)
with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    print(sess.run(tf.slice(adjust_contract, [1, 0, 0], [1, 3, 3])))
    print(sess.run(tf.slice(gray, [0, 0, 0], [1, 3, 1])))
    print(sess.run(tf.slice(adjust_saturation, [1, 0, 0], [1, 3, 3])))
    coord.request_stop()
    coord.join(threads)

# 颜色
"""
    CNN通常使用单一颜色图像来训练。
        当一幅图只有单一颜色时，我们称它为灰度空间，即单颜色通道。
    计算机中使用灰度是合理的，了解图像形状，无须借助颜色信息。缩减颜色空间可加速训练过程。
    灰度只需单个分量即可。
    CNN训练中使用颜色，对图像进行颜色空间变换有时非常young
"""
# 1.灰度
# 灰度图像只有单个分量，取值范围为[0,255]
"""将RGB转化为灰度图"""
image_filename = "test-input-image.jpg"
filename_queue = tf.train.string_input_producer([image_filename])
reader = tf.WholeFileReader()
_, image_file = reader.read(filename_queue)
image = tf.image.decode_jpeg(image_file)
gray = tf.image.rgb_to_grayscale(image)
with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    print("==" * 20)
    print(sess.run(tf.slice(gray, [0, 0, 0], [1, 3, 1])))
    coord.request_stop()
    coord.join(threads)

# 2.HSV空间
# 色度、饱和度和灰度构成HSV颜色空间。与RGB空间类似，颜色空间有3个分量和秩为1的张量表示。
# HSV度量更为贴近人感知属性。HSV有时较HSB，B代表亮度值
image_filename = "test-input-image.jpg"
filename_queue = tf.train.string_input_producer([image_filename])
reader = tf.WholeFileReader()
_, image_file = reader.read(filename_queue)
image = tf.image.decode_jpeg(image_file)
hsv = tf.image.rgb_to_hsv(tf.image.convert_image_dtype(image, tf.float32))
with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    print("==" * 20)
    print(sess.run(tf.slice(hsv, [0, 0, 0], [1, 3, 1])))
    coord.request_stop()
    coord.join(threads)

# 3.RGB空间
# 恢复到RGB时，RGB每个像素个通道都被灰度图像对应的像素灰度值填充
rgb_hsv = tf.image.hsv_to_rgb(hsv)
rgb_gray_scale = tf.image.grayscale_to_rgb(gray)

# 4.为对LAB空间提供原生支持
# 能够映射出大量可感知的颜色

# 图像类型转换
# tf.to_float()是可以的
# tf.image.convert_image_dtype(image,dtype,saturate=False)更便捷
