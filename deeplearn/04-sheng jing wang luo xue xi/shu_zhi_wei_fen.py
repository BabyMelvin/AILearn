import numpy as np
import matplotlib.pylab as plt

def function_1(x):
    return 0.01 * x ** 2 + 0.1 * x

def numerical_diff(f, x):
    h = 1e-4 # 0.001
    return (f(x + h) - f(x -h)) / ( 2 * h)


def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    return lambda t: d * t + y

x = np.arange(0.0, 20.0, 0.1) # 以 0.1 为单位，从 0 到 20 的数组 x
y = function_1(x)
plt.xlabel("x")
plt.ylabel("y")

tf = tangent_line(function_1, 5)
y2 = tf(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.show()