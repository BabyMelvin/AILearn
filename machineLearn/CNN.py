import tensorflow as tf
import glob
from collections import defaultdict
from itertools import groupby

"""
    CNN:
      当输入经过网络时，其高度和宽度都会减少，而其深度会增加。
        深度值的增加减少了使用该网络所需的计算量  
      模型中数据集80%用于训练，其余20%做测试。如果一个产品模型，
    预留一些原始数据做交叉测试验证。
"""
# 每个标签都被转化为一个代表包含所有狗吗、品种名称索引的整数。
# 找到imagenet-dogs路径下所有的目录名称
labels = list(map(lambda c: c.split("\\")[-1], glob.glob(r".\imagenet-dogs")))

sess = tf.Session()
# 1.将图像转成TFRecord文件
image_filenames = glob.glob(r".\imagenet-dogs\n02*\*.jpg")
print(image_filenames[0:2])

training_dataset = defaultdict(list)
testing_dataset = defaultdict(list)

# 将文件名分解为品种和相应文件名，品种对应于文件夹名称
# help('map')
# map(function, sequence[, sequence, ...]) -> list
image_filename_with_breed = map(lambda filename: (filename.split("\\")[2], filename), image_filenames)

# 依据品种(上述返回元组的第0个分量)对图像分组
# 得到training_dataset["n02085620"]=["n02085620_10131.jpg",...]
# 可计算迭代的次数,狗的种类数
count = [0]
for dog_breed, breed_images in groupby(image_filename_with_breed, lambda x: x[0]):
    # 枚举每个品种的图像，并将大致20%图像划入测试集
    # print(dog_breed, breed_images)
    count[0] += 1
    for i, breed_image in enumerate(breed_images):
        if i % 5 == 0:
            testing_dataset[dog_breed].append(breed_image[1])
        else:
            training_dataset[dog_breed].append(breed_image[1])
    # 检查每个品种测试图像至少有全部图像的18%
    breed_training_count = len(training_dataset[dog_breed])
    breed_testing_count = len(testing_dataset[dog_breed])
    # round小数精度
    assert round(breed_testing_count / (breed_training_count + breed_testing_count), 2) > 0.18, "Not enough testing"

print("count:", count[0])


# 预处理阶段所有文件都会被处理
def write_records_file(dataset, record_location):
    """
    用dataset中图像填充一个TFRecord文件，将类别包含进来
    :param dataset:dict(list) 字典中，键值为标签，列表为文件夹下文件
    :param record_location:str 存储TFRecord输出路径
    :return:
    """
    writer = None
    # 枚举dataset，因为当前索引用于对文件进行划分，每隔100幅图像，训练样本信息就被写入到一个新的TFRecord文件中，加快写操作的进程
    current_index = 0
    for breed, images_filenames in dataset.items():
        for image_filename in images_filenames:
            if current_index % 100 == 0:
                if writer:
                    writer.close()
                record_filename = "{record_location}-{current_index}.tfrecords".format(record_location=record_location,
                                                                                       current_index=current_index)
                print(record_filename)
                writer = tf.python_io.TFRecordWriter(record_filename)
            current_index += 1
            # for file in images_filenames:
            image_file = tf.read_file(image_filename)
            # 在ImageNet,有少量无法被TensorFlow识别为JPEG图像，利用try/catch可将这些图像忽略
            try:
                image = tf.image.decode_jpeg(image_file)
            except:
                print(image_filenames)
                continue
                # 转化为灰度图像可减少处理计算量和内存占用，但这并不是必需的
            grayscale_image = tf.image.rgb_to_grayscale(image)
            resize_image = tf.image.resize_images(images=grayscale_image, size=[250, 151])
            # 这里用tf.cast，因为虽然尺寸更改后图像数据类型是浮点型，但RGB值尚未转换到[0,1)区间
            image_bytes = sess.run(tf.cast(resize_image, tf.uint8)).tobytes()
            # 将标签按字符串存储较高效，推荐做法其转化为整数索引或读热编码的秩为1张量
            image_label = breed.encode("utf-8")
            example = tf.train.Example(features=tf.train.Features(feature={
                'label':
                    tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_label])),
                'image':
                    tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_bytes]))
            }))
            writer.write(example.SerializeToString())
        print("current_index=", current_index)
    writer.close()


# write_records_file(testing_dataset, r".\output\testing-image")
write_records_file(training_dataset, r".\output\training-image")
# 加载图像
filename_queue = tf.train.string_input_producer([r".\output\testing-image*"])
reader = tf.TFRecordReader()
_, serialized = reader.read(filename_queue)
features = tf.parse_single_example(
    serialized,
    features={
        'label': tf.FixedLenFeature([], tf.string),
        'image': tf.FixedLenFeature([], tf.string)
    }
)
record_image = tf.decode_raw(features['image'], tf.uint8)
# 修改图像的形状有助于训练和输出可视化
image = tf.reshape(record_image, [250, 151, 1])
label = tf.cast(features['label'], tf.string)
min_after_dequeue = 10
batch_size = 3
capacity = min_after_dequeue + 3 * batch_size
image_batch, label_batch = tf.train.shuffle_batch(
    [image, label], batch_size=batch_size,
    capacity=capacity, min_after_dequeue=min_after_dequeue
)

# 模型
float_image_batch = tf.image.convert_image_dtype(image_batch, tf.float32)
conv2d_layer_one = tf.contrib.layers.convolution2d(
    float_image_batch,
    num_output_channes=32,
    kernel_size=(5, 5),
    activation_fn=tf.nn.relu,
    weight_init=tf.random_normal,  # 正态随机值，第一组滤波器填充服从正态分布随机数
    stride=(2, 2),
    trainable=True)  # 权值能够调整
pool_layer_one = tf.nn.max_pool(conv2d_layer_one, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
# 卷积输出的第1维和最后一维未发生变化，但中间两维发生变化
print(conv2d_layer_one.get_shape(), pool_layer_one.get_shape)

conv2d_layer_two = tf.contrib.layers.convolution2d(
    pool_layer_one,
    num_output_channels=64,  # 更多输出通道意味着滤波器数量增加
    kernel_size=(5, 5),
    activate_fn=tf.nn.relu,
    weight_init=tf.random_normal,
    stride=(1, 1),
    trainable=True)
pool_layer_two = tf.nn.max_pool(conv2d_layer_two,
                                ksize=[1, 2, 2, 1],
                                strides=[1, 2, 2, 1],
                                padding='SAME')
print(conv2d_layer_two, pool_layer_two)

# 全连接
# 图像中每个点都与输出神经元建立全连接，由于用softmax，因此全连接层修改为二阶张量。
# 张量的第一维用于区分图像，第2维对应于每个输入张量的秩1张量。
flattened_layer_two = tf.reshape(
    pool_layer_two,
    [
        batch_size,  # image_batch中每幅图像
        -1  # 输入的其他所有维
    ])
print(flattened_layer_two.get_shape())
# 池化层展开后，便可将当前状态与所预测的狗品种关联两个全连层进行整合

# weight_init参数也可接收一个可调用参数，lambda表示是返回一个截断正态分布
hidden_layer_three = tf.contrib.layers.fully_connected(
    flattened_layer_two,
    512,
    weight_init=lambda i, dtype: tf.truncated_normal([38912, 512], stddev=0.1),
    activation_fn=tf.nn.relu
)
# 对一些神经元进行dropout处理,削减它们在模型的重要性
hidden_layer_three = tf.nn.dropout(hidden_layer_three, 0.1)

# 输出是前面的层与训练中可用的120个不同的狗的品种全连接
finally_fully_connected = tf.contrib.layers.fully_connected(
    hidden_layer_three,
    120,  # ImageNet Dogs数据集中狗的品种
    weight_init=lambda i, dtype: tf.truncated_normal([512, 120], stddev=0.1)
)

# 训练
"""
    依据输入训练优化器(作用优化每层的权值),训练数据的真实指标标签和模型预测结果结算模型损失。
    这个过程会经过数次迭代，每次迭代提升模型的准确率
    softmax无法处理字符串，应该转化成一个独一无二数字,这些应该预处理阶段进行
"""
# 匹配每个来自label_batch的标签并返回他们类别列表中索引
train_labels = tf.map_fn(lambda l: tf.where(tf.equal(labels, l))[0, 0:1], label_batch, dtype=tf.int64)
