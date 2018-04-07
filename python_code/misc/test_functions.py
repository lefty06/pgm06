import collections as c

def test_opt_arg(arg1,arg2=None):
    #The optionnal arguments must always go at the end of the list of args
    return arg1, arg2

def count_args(count_args,required_number_args):
    return True if len(count_args) == required_number_args else False

def print_everything(*args):
    for count, thing in enumerate(args,1): #Add a line number starting from index 1
        print( '{0}. {1}'.format(count, thing))
        # print_everything('apple', 'banana', 'cabbage') #To test in main

def find_dupes_in_list(arg1):
    #collections, https://pymotw.com/2/collections/counter.html
    #collections.Couinter can take a string, a list as an argument and return a dict with the number of times each values repeats in the list
    res_dict={k:v for k,v in c.Counter(arg1).iteritems() if v>1} #retuns the duplicate values and the number of occurences.
    res_list=[k for k,v in c.Counter(arg1).iteritems() if v>1] #returns the duplicate values only.
    return res_dict

def Main():
    event_ids=[123,565,123,586,2556,2155,'123',321]
    print find_dupes_in_list(event_ids)

    astring='this_is_a_random_sentence'
    print find_dupes_in_list(astring)

if __name__ == '__main__':
    Main()
