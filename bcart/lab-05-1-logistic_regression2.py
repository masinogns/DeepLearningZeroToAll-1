# Lab 5 Logistic Regression Classifier
from neural_network import NeuralNetwork
from mytype import MyType
import tensorflow as tf


class MVLogisticRegression (NeuralNetwork):
    def init_network(self):
        self.set_placeholder(2, 1)

        output = self.create_layer(self.X, 2, 1, MyType.LOGISTIC, 'Wa', 'ba')
        output = tf.sigmoid(output)

        self.set_hypothesis(output)
        self.set_cost_function(MyType.LOGISTIC)
        self.set_optimizer(MyType.GRADIENTDESCENT, l_rate=0.1)

    def my_log(self, i, x_data, y_data):
        pass

    '''
    [1, 2]
    [2, 3]
    [3, 1]
    [4, 3]
    [5, 3]
    [6, 2]
    ->
    [ 0.00138244]
    [ 0.0577572]
    [ 0.07596549]
    [ 0.92112178]
    [ 0.99383414]
    [ 0.99856013]
    '''

gildong = MVLogisticRegression()

x_data = [[1, 2],
          [2, 3],
          [3, 1],
          [4, 3],
          [5, 3],
          [6, 2]]
y_data = [[0],
          [0],
          [0],
          [1],
          [1],
          [1]]

gildong.learn(x_data, y_data, 5000, 200);
gildong.show_error()
gildong.test_sigmoid(x_data)
gildong.evaluate_sigmoid(x_data, y_data)
