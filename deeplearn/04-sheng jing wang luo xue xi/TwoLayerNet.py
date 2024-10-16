import sys, os

sys.path.append(os.pardir)

from network import *

from numerical_gradient import  numerical_gradient
import numpy as np

class TwoLayerNet:

    '''
    # 输入图像的大小是 784（28 × 28），输出为 10 个类别
    input_size: 输入层神经元数, 784
    hidden_size: 隐藏层神经元数, 设置一个合适值即可
    output_size: 输出层神经元数, 10
    '''
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 初始化权重
        # W1, W2保存权重， b1,b2保存偏置

        # 权重使用符合高斯 分布的随机数进行初始化(权重初始值关系到学习是否成功)
        # 偏置使用0 进行初始化
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] =  np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)

    # 进行试别-推理,x是图像数据
    def predict(self, x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = sigmoid(a2)

        return y

    # x: 输入数据 , t: 监督数据
    # 计算损失函数值, t是正确解标签
    def loss(self, x, t):
        y = self.predict(x)

        return cross_entropy_error(y, t)

    # 计算试别精度
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy =  np.sum(y == t) / float(x.shape[0])

        return accuracy

    # 权重参数梯度
    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        # 保存梯度返回值
        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1']) # W1权重的梯度
        grads['b1'] = numerical_gradient(loss_W, self.params['b1']) # W2权重的梯度
        grads['W2'] = numerical_gradient(loss_W, self.params['W2']) # b1偏置的梯度
        grads['b2'] = numerical_gradient(loss_W, self.params['b2']) # b2偏置的梯度

        return grads

    # numerical_gradient高速版本
    # 误差反向传播法高效地计算梯度
    def gradient(self, x, t):
        return

if __name__ == '__main__':
    net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
    print(net.params['W1'].shape)  # (784, 100)
    print(net.params['b1'].shape) # (100,)
    print(net.params['W2'].shape) # (100, 10)
    print(net.params['b2'].shape) # (10,)

    x = np.random.rand(100, 784)
    y = net.predict(x)

    x = np.random.rand(100, 784) # 伪输入数据（100 笔）
    t = np.random.rand(100, 10)  # 伪正确解标签（100 笔）

    grads = net.numerical_gradient(x, t)  #计算梯度
    print(grads['W1'].shape)  # (784, 100)
    print(grads['b1'].shape) # (100,)
    print(grads['W2'].shape) # (100, 10)
    print(grads['b2'].shape) # (10,)
