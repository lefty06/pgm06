#!/usr/bin/python
import pickle

'''
this data type is used when processing/sorting a lot of data to be re used later.
this data type is optimized for python
'''
data_dict = {
    "volt": [0, 1, 2, 3, 45, 25],
    "current": [1, 2, 56, 74, 87]
}

with open('01_test_pickled_file', 'wb') as pk:
    pickle.dump(data_dict, pk)

with open('01_test_pickled_file', 'rb') as pk:
    new_data = pickle.load(pk)

print type(new_data)
