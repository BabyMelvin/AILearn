import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label


# 这个只匀速浮点调用
def step_func1(x):
    if x > 0:
        return 1
    else:
        return 0

# 支持numpy
def step_func2(x):
    y = x > 0
    return y.astype(int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def step_function(x):
    return np.array(x > 0, dtype=int)

def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
y1 = sigmoid(x)
y2 = relu(x)
plt.plot(x, y1, linestyle = '--', label="sigmoid")
plt.plot(x, y, label="step_function")
plt.plot(x, y2, linestyle = '-.', label="relu")
plt.legend()
plt.ylim(-0.1, 1.1) # 指定 y 轴的范围
plt.show()