import matplotlib.pyplot as plt
import numpy as np
import sys, os


sys.path.append(os.pardir)

from dataset.mnist import load_mnist

from TwoLayerNet import TwoLayerNet

if __name__ == '__main__':
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize= True, one_hot_label = True)
    train_loss_list = []
    train_acc_list = []
    test_acc_list = []

    train_size = x_train.shape[0]
    batch_size = 100

    # 平均每个epoch的重复次数
    iter_per_epoch = max(train_size/batch_size, 1)

    # 超参数
    iters_num = 10000
    train_size = x_train.shape[0]
    batch_size = 100

    learning_rate = 0.1

    network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

    for i in range(iters_num):
        # 获取mini-batch
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]

        # 计算梯度
        grad = network.numerical_gradient(x_batch, t_batch)

        # 更新参数
        for key in ('W1', 'b1', 'W2', 'b2'):
            network.params[key] -= learning_rate * grad[key]

        #记录学习过程
        loss = network.loss(x_batch, t_batch)
        train_loss_list.append(loss)

        # 计算每个 epoch 的识别精度
        if i % iter_per_epoch == 0:
            train_acc = network.accuracy(x_train, t_train)
            test_acc = network.accuracy(x_test, t_test)
            train_acc_list.append(train_acc)
            test_acc_list.append(test_acc)
            print("train acc, test acc | " + str(train_acc) + ", " + str(test_acc))

    # 画图
    markers = {'train': '0', 'test': 's'}
    x = np.arange(len(train_acc_list))
    plt.plot(x, train_acc_list, label = 'train acc')
    plt.plot(x, test_acc_list, label = 'test acc', linestyle='--')
    plt.xlabel('epochs')
    plt.ylabel('accuracy')
    plt.ylim(0, 1.0)
    plt.legend(loc='lower right')
    plt.show()