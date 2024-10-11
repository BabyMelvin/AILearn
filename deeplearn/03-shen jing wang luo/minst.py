# coding: utf-8

import sys, os

from mpmath.libmp import normalize
from setuptools.namespaces import flatten

sys.path.append(os.pardir)
from dataset.mnist import load_mnist

# (训练图像,训练标签)，(测试图像，测试标签)
(x_train, t_train), (x_test, t_test) = load_mnist(flatten = True, normalize = False)


# 第 1 个参数 normalize 设置是否将输入图像正规化为 0.0～1.0 的值。False则保持0-255
# 第 2 个参数 flatten 设置 是否展开输入图像（变成一维数组）。False则是1x28x28 三维数组
#          若设置为 True，则输入图像会保存为由 784 个 元素构成的一维数组。
# 第 3 个参数 one_hot_label 设置是否将标签保存为 onehot 表 示（ one-hot representation）。
#          one-hot 表示是仅正确解标签为1，其余 皆为 0 的数组，就像 [0,0,1,0,0,0,0,0,0,0] 这样。
#          当 one_hot_label 为 False 时， 只是像 7、2 这样简单保存正确解标签；

# load_mnist(normalize=True, flatten=True, one_hot_label=False)

print(x_train.shape)
print(t_train.shape)

print(x_test.shape)
print(t_test.shape)