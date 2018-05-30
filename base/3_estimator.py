import tensorflow as tf

"""
    simplify the mechanics of machine learn:
        run training loop
        run evaluation loop
        manage data sets
"""
# simpler the linear regression program
# Numpy is often used to load,manipulate and pre_process data
import numpy as np

# declare list of features.we only have one numeric feature
# there are many other types of columns that are more complicated and useful
feature_columns = [tf.feature_column.numeric_column("x", shape=[1])]

# a estimator is the front end to invoke training(fitting) and evaluation(inference)
# there are many pre_defined types like linear regression,linear classification ,and many neural network classifiers and regressors
# linear regression
estimator = tf.estimator.LinearRegressor(feature_columns=feature_columns)

# TensorFlow provides many helper method to read and set up data sets.
# here we use two data sets:one for training and one for evaluation
# we have to tell the 07-function how many batched of data(num_epochs多少次) and how big data batch (每次多长)should be
x_train = np.array([1., 2., 3., 4.])
y_train = np.array([0., -1., -2., -3.])
x_eval = np.array([2., 5., 8., 1.])
y_eval = np.array([-1.01, -4.1, -7, 0.])

input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_train}, y_train, batch_size=4, num_epochs=None, shuffle=True
)
train_input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_train}, y_train, batch_size=4, num_epochs=1000, shuffle=False
)
eval_input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_eval}, y_eval, batch_size=4, num_epochs=1000, shuffle=False
)

# we can invoke 1000 training step by invoking the method and passing the training data set
estimator.train(input_fn=input_fn, steps=1000)

# here we evaluate how well our module did
train_metrics = estimator.evaluate(input_fn=train_input_fn)
eval_metrics = estimator.evaluate(input_fn=eval_input_fn)
print("train metrics:%r" % train_metrics)
print("eval metrics:%r" % eval_metrics)
