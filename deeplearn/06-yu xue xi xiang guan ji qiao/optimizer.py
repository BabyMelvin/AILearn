import numpy as np


class Momentum:

    # 变量 v 会保存物体的速度
    def __init__(self, lr = 0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None

    # 调用 update() 时，v 会以字典型变量的形式保存与参数结构相同的数据
    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)

        for key in params.keys():
            self.v[key] =  self.momentum * self.v[key] - self.lr * grads[key]
            params[key] += self.v[key]


class AdaGrad:
    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)

        for key in params.key():
            self.h[key] += grads[key] * grads[key]

            # 加上了微小值1e-7,避免作为除数为0
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)