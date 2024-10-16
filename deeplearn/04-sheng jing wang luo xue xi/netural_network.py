import sys, os
sys.path.append(os.pardir)
import numpy as np

from gradient_method import numerical_gradient

# softmax 函数的输出是 0.0 到 1.0 之间的实数。
# softmax 函数的输出值的总和是 1。
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

#################  损失函数  #######################
# 均方误差
def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)


# 交叉熵误差
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

########### 数值微分 ####################
# 数值微分
def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x-h)) / (2 * h)

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3) # 用高斯分布进行初始化

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss





net = simpleNet()
print(net.W) # 权重参数

x = np.array([0.6, 0.9])
p = net.predict(x)
print(p)

np.argmax(p) # 最大索引值
t = np.array([0, 0, 1]) #正确解标签
net.loss(x, t)

def f(W):
    return net.loss(x, t)

# f = lambda w: net.loss(x, t)
dW = numerical_gradient(f, net.W)
print(dW)