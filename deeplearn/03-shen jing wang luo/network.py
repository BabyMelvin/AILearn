import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def identity_function(x):
    return x

# A = X W + B
def init_network():
    network = {'W1': np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]), 'b1': np.array([0.1, 0.2, 0.3]),
               'W2': np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]), 'b2': np.array([0.1, 0.2]),
               'W3': np.array([[0.1, 0.3], [0.2, 0.4]]), 'b3': np.array([0.1, 0.2])}

    # network = {}
    # network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    # network['b1'] = np.array([0.1, 0.2, 0.3])
    # network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    # network['b2'] = np.array([0.1, 0.2])
    # network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    # network['b3'] = np.array([0.1, 0.2])

    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y

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

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)