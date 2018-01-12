import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

"""
    MNIST is the machine learning "hello world"
    MNIST:Mixed National Institute of Standards and Technology database
            数据库，存储各个国家地区，不同标准手写数字
"""

"""
    MNIST data split three parts:
        1.mnist.train:55000 data points of train
        2.mnist.test :10000 points of test
        3.mnist.validation: 5000 points fo validation data
   MNIST data points two parts:
        1.an image of a handwritten digit 
        2.a corresponding label
    the train set and test set contain images and their corresponding labels
"""
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
