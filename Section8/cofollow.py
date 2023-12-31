import os
import time
from functools import wraps


def follow(filename, target):
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)
            else:
                target.send(line)


# Decorator for coroutine to remove None start
def consumer(func):
    @wraps(func)
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)
        return f
    return start


@consumer
def printer():
    while True:
        item = yield
        print(item, end='')


@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)


def receive(expected_type):
    msg = yield
    assert isinstance(msg, expected_type), 'Expected type %s' % (expected_type)
    return msg
