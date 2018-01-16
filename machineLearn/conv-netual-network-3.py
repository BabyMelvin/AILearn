import tensorflow as tf
import os

"""
  TensorFlow支持加载格式(JPG,PNG),不同的空间(RGB,ARGB)
  通道：用一个包含每个通道中颜色数量的标量的秩1张量
  red=tf.constant([255,0,0])
"""

# 图像加载
# 图像加载和其他大型为进制文件相同，只是图内容需要解码
"""
def read_img(filenames, num_epochs, shuffle=True):
    filename_queue = tf.train.string_input_producer([filenames])
    reader = tf.WholeFileReader()
    key, value = reader.read(filename_queue)
    img = tf.image.decode_jpeg(value, channels=3)
    img = tf.image.resize_images(img, size=(256, 256), method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    return img


# match_filename_once接收一个正则表达式
# image_filename = "[os.path.dirname(__file__) + "\\" + file_name]"
image = read_img("test-input-image.jpg", num_epochs=None, shuffle=True)
with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    sess.run(tf.global_variables_initializer())
    print(sess.run([image]))
    coord.request_stop()
    coord.join(threads)
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
    coord.request_stop()
    coord.join(threads)

print('-' * 20)
# 图像格式
# 使用图像时，不同的格式可用于解决不同的问题
# 1.JPEG与PNG
# JPEG图像不会存储任何alpha通道信息，但PNG会。
# 训练模型时，这点很重要。将帽子移除对应区域alpha值为0
# JPEG图像时，不要进行过于频繁操作，不然会留下一些伪影(artifact)。任何必要操作，获取图像的原始数据，并将它们导出JPEG文件。
# PNG无损压缩，缺点体积大点。


# TFRecord
"""
    将二进制文件和标签(训练类别标签)数据存储同一个文件中，TF内置文件格式，该格式称为TFRecord
    训练之前通过预处理将图像转为TFRecord格式
"""
# 复用之前的图像，并赋予一个加标签
image_label = b'\x01'
# 将该张量转换为字节型，加载整个图像文件
with tf.Session() as sess1:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    image_loaded = sess1.run(image)
    image_bytes = image_loaded.tobytes()
    image_height, image_width, image_channels = image_loaded.shape
    # 导出TFRecord
    writer = tf.python_io.TFRecordWriter("tfrecord")

    # 本样本中不保存图像宽度，高度或通道数，以便节约不要求分配的空间
    example = tf.train.Example(features=tf.train.Features(feature={
        'label':
            tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_label])),
        'image':
            tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_bytes]))
    }))

    # 样本保存在一个文件tfrecord中
    writer.write(example.SerializeToString())
    coord.request_stop()
    coord.join()
    writer.close()

# 加载TFRecord文件
tf_record_filename_queue = tf.train.string_input_producer(["tfrecord"])
# 注意记录读取器，设计意图可读取多个样本的TFRecord文件
tf_record_reader = tf.TFRecordReader()
_, tf_record_serialized = tf_record_reader.read(tf_record_filename_queue)

# 标签和图像都按字节存储，也可以按int64或float64类型存储在序列化tf.Example protobuf文件中
tf_record_features = tf.parse_single_example(
    tf_record_serialized,
    features={
        'label': tf.FixedLenFeature([], tf.string),
        'image': tf.FixedLenFeature([], tf.string),
    })

# 使用tf.uint8类型，因为所有通道信息都处于0~255
tf_record_image = tf.decode_raw(tf_record_features['image'], tf.uint8)

# 识别图像尺寸，使语气所保存图像类似，但非必要
tf_record_image = tf.reshape(tf_record_image, [image_height, image_width, image_channels])

# 用实值表示图像高度、宽度和通道，因为必须对输入的形状进行调整
tf_record_label = tf.cast(tf_record_features['label'], tf.string)

with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)
    print(sess.run(tf.equal(image, tf_record_image)))
    print(sess.run(tf_record_image))
    print(sess.run(tf_record_label))
    coord.request_stop()
    coord.join(threads)
