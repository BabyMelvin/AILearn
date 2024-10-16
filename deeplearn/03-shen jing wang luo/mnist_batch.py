import sys, os
import pickle
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image
from network import sigmoid, softmax

# 神经网络 的输入层有 784 个神经元，输出层有 10 个神经元。
#   输入层的 784 这个数字来 源于图像大小的 28 × 28 = 784，
#   输出层的 10 这个数字来源于 10 类别分类（数 字 0 到 9，共 10 类别）。
#   这个神经网络有 2 个隐藏层，第 1 个隐藏层有 50 个神经元，第 2 个隐藏层有 100 个神经元。（50和100可以设置任何值）


# 推理过程
# 1.首先获得MNIST 数据集，生成网络
# 2.用 for 语句逐一取出保存 在 x 中的图像数据，用 predict() 函数进行分类。
# 3.我们 取出这个概率列表中的最大值的索引（第几个元素的概率最高），作为预测结 果。
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    # 保存权重参数，推理阶段加载学习阶段的参数
    # 假设学习已经完成，所以学习到的参数被保存下来。
    # 假设保存在 sample_weight.pkl 文件中，在推理阶段，我们直接加载这些已经学习到的参数。

    # 文件中以字典变量的形式保存了权重和偏置参数
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network

# predict() 函数以 NumPy 数 组的形式输出各个标签对应的概率。比如输出 [0.1, 0.3, 0.2, ..., 0.04] 的 数组，
# 该数组表示“0”的概率为 0.1，“ 1”的概率为 0.3，等等。
def predict(network, x):
     W1, W2, W3 = network['W1'], network['W2'], network['W3']
     b1, b2, b3 = network['b1'], network['b2'], network['b3']

     a1 = np.dot(x, W1) + b1
     z1 = sigmoid(a1)
     a2 = np.dot(z1, W2) + b2
     z2 = sigmoid(a2)
     a3 = np.dot(z2, W3) + b3
     y = softmax(a3)

     return y

x, t = get_data()
network = init_network()
accuracy_cnt = 0
batch_size = 100  # 批处理

# range(start, end)生成列表： start到end-1
# range(start, end, step)：step步长，列表
for i in range(0, len(x), batch_size):
    x_batch = x[i: i+ batch_size]
    y_batch = predict(network, x_batch)

    # 这指定了在 100 × 10 的数组中，沿着第 1 维方向（以 第 1 维为轴）
    # 找到值最大的元素的索引（第 0 维对应第 1 个维度）
    p = np.argmax(y_batch, axis=1) # # 获取概率最高的元素的索引
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))