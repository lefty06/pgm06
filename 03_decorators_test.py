#!/usr/bin/python
from time import time


def timer(func):
    def f(*args, **kw):
        before = time()
        result = func(*args, **kw)
        after = time()
        print("function: {}, execution time: {}".format(
            func.__name__, after-before))
        return result
    return f

# This is a decorator which executes the following function and includes an extra piece of code without having to add that piece of code in each function
# This decorator will take any function with number of arguments.


@timer
def add(x, y):
    return x+y


print "{}".format(add(1, 2))

# Example with no decorator where that extra piece would need to be added for every function to display the execution time


def sub(x, y):
    before = time()
    result = x-y
    after = time()
    print("function: {}, execution time: {}".format(sub.__name__, after-before))
    return result


print "{}".format(sub(10, 2))
