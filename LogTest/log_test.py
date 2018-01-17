import logging


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


num_1 = 10
num_2 = 5


add_result = add(num_1, num_2)
logging.warning('add: {}+{}={}'.format(num_1,num_2,add_result))
