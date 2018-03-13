#!/usr/bin/python
from time import sleep

# To get the results the user will have to wait until the entire data is processed eventhough he only wants to process some of the first values and discard the rest. This will consume time and a lot of memory. The alternative is to use a generator which will iterate to the next value on demande instead of storing them all


def compute():
    '''
    this is to return a list of digits
        '''
    rv = []
    for i in range(10):
        sleep(.5)
        rv.append(i)
    return rv


def compute2():
    for i in range(10):
        sleep(.5)
        yield i


for val in compute2():
    print(val)
