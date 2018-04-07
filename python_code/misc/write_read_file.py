import os
from os import path
import pickle

#This is to store the values of a list very quicly in a file and read it very quckly too using pickle
#pickle stores values in a non humane reable format but the access will be very fast.


def write_pickle_list(thelist,outputfile):
    with open(outputfile, 'wb') as f:
        pickle.dump(thelist, f)

def read_pickle_list(outputfile):
    myslist=[]
    if path.isfile(outputfile):
        with open(outputfile, 'rb') as f:
            my_list = pickle.load(f)
        return my_list
    return my_list

def Main():
    l=['1',2,3,5]
    ofile='/home/pat/Documents/python_scripts/misc/alist.pickle'
    write_pickle_list(l,ofile)
    res=read_pickle_list(ofile)

    # print '{}'.format('\n'.join(res)) #This will return an error because join can only be used with a list of strings, map can cast values to string
    print '{}'.format('\n'.join(map(str,res)))

if __name__ == '__main__':
    Main()
