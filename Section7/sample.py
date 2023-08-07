from logcall import *
from validate import *


@validated
def add(x: Integer, y: Integer):
    """
    Add Two
    :param x:
    :param y:
    :return:
    """
    return x + y


@logged
def sub(x, y):
    return x-y


@log_format('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
    return x*y
