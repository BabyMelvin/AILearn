# coding: utf-8
from time import sleep

import numpy as np
from keras.src.backend.jax.nn import sigmoid
from torch.onnx.symbolic_opset18 import col2im

from util import im2col

class Relu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx
class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = sigmoid(x)
        self.out = out

        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out

        return dx

class Convolution:

    # 滤波器（权重）、偏置、步幅、填充作为参数
    def __init__(self, W, b, stride=1, pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad

        # backward使用
        self.x = None
        self.col = None
        self.col_w = None

        self.dW = None
        self.db = None

    def forward(self, x):
        # 滤波器是(FN, C, FH, FW) 的 4 维 形 状
        # FN、C、FH、FW 分别是Filter Number（滤波器数量）、Channel、Filter Height、Filter Width 的缩写。
        FN, C, FH, FW = self.W.shape
        N, C, H, W = x.shape

        out_h = int(1 + (H + 2 * self.pad - FH) / self.stride)
        out_w = int(1 + (W + 2 * self.pad - FW) / self.stride)

        col = im2col(x, FH, FW, self.stride, self.pad)

        # reshape 将滤波器展开为 2 维数组
        # 通过在 reshape 时指定为-1，reshape 函数会自 动计算-1 维度上的元素个数，
        # 以使多维数组的元素个数前后一致
        col_W = self.W.reshape(FN, -1).T  # 滤波器展开
        out = np.dot(col, col_W) + self.b

        # transpose 会更改多维数组的轴的顺序
        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)
        return  out

    def backward(self, dout):
        FN, C, FH, FW = self.W.reshape
        dout = dout.transpose(0, 2, 3, 1).reshape(-1, FN)

        self.db = np.sum(dout, axis=0)
        self.dW = np.dot(self.col.T, dout)
        self.dW = self.dW.transpose(1, 0).reshape(FN, C, FH, FW)

        dcol = np.dot(dout, self.col_w.T)
        dx = col2im(dcol, self.x.shape, FH, FW, self.stride, self.pad)

        return dx

class Pooling:
    def __init__(self, pool_h, pool_w, stride=2, pad=0):
        self.pool_h = pool_h
        self.pool_w = pool_w
        self.stride = stride
        self.pad = pad

        self.x = None
        self.arg_max = None

    def forward(self, x):
        N, C, H, W = x.shape
        out_h = int(1 + (H - self.pool_h) / self.stride)
        out_w = int(1 + (W - self.pool_w) / self.stride)

        col = im2col(x, self.pool_h, self.pool_w, self.stride, self.pad)
        col = col.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)
        arg_max = np.argmax(col, axis=1)

        out = np.argmax(col, axis=1)
        out = out.reshape(N, out_h, out_w, C).transpose(0, 3, 1, 2)

        self.x = x
        self.arg_max = arg_max
        return out

    def backward(self, dout):
        dout = dout.transpose(0, 2, 3, 1)

        pool_size = self.pool_w * self.pool_h
        dmax = np.zeros((dout.size, pool_size))
        dmax[np.arange(self.arg_max.size), self.arg_max.flatten(())] = dout.flatten()

        dcol = dmax.reshape(dmax.shape[0] * dmax.shape[1] * dmax.shape[2], -1)
        dx = col2im(dcol, self.x.shape, self.pool_h, self.pool_w, self.stride, self.pad)

        return dx