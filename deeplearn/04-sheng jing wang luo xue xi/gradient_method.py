# coding: utf-8
import numpy as np
import matplotlib.pylab as plt
from numerical_gradient import numerical_gradient


# learning rate
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    x_history = []

    for i in range(step_num):
        x_history.append( x.copy() )

        grad = numerical_gradient(f, x)

        # 沿着梯度方向，步进lr
        x -= lr * grad

    return x, np.array(x_history)


def function_2(x):
    return x[0]**2 + x[1]**2

# 初始值点
init_x = np.array([-3.0, 4.0])

# 学习率，η
lr = 0.1

# 学习步数
step_num = 20

# x_history，每次学习后的位置
x, x_history = gradient_descent(function_2, init_x, lr=lr, step_num=step_num)

# 画中心两条线
plt.plot( [-5, 5], [0,0], '--b') # -- 和 blue
plt.plot( [0,0], [-5, 5], '--b')

# 点表示每步的位置
plt.plot(x_history[:,0], x_history[:,1], 'o')

plt.xlim(-3.5, 3.5)
plt.ylim(-4.5, 4.5)
plt.xlabel("X0")
plt.ylabel("X1")
plt.show()
