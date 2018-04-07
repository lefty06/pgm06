import resource as mem

'''
The syntax is the * and **. The names *args and **kwargs are only by convention but there's no hard requirement to use them.
You would use *args when you're not sure how many arguments might be passed to your function, i.e. it allows you pass an arbitrary number of arguments to your function. For example:
>>> def print_everything(*args):
        for count, thing in enumerate(args):
...         print( '{0}. {1}'.format(count, thing))
...
>>> print_everything('apple', 'banana', 'cabbage')
0. apple
1. banana
2. cabbage

Similarly, **kwargs allows you to handle named arguments that you have not defined in advance:
>>> def table_things(**kwargs):
...     for name, value in kwargs.items():
...         print( '{0} = {1}'.format(name, value))
...
>>> table_things(apple = 'fruit', cabbage = 'vegetable')
cabbage = vegetable
apple = fruit

You can use these along with named arguments too. The explicit arguments get values first and then everything else is passed to *args and **kwargs. The named arguments come first in the list. For example:

def table_things(titlestring, **kwargs)
You can also use both in the same function definition but *args must occur before **kwargs.
You can also use the * and ** syntax when calling a function. For example:
>>> def print_three_things(a, b, c):
...     print( 'a = {0}, b = {1}, c = {2}'.format(a,b,c))
...
>>> mylist = ['aardvark', 'baboon', 'cat']
>>> print_three_things(*mylist)
a = aardvark, b = baboon, c = cat

As you can see in this case it takes the list (or tuple) of items and unpacks it. By this it matches them to the arguments in the function. Of course, you could have a * both in the function definition and in the function call.
'''

def print_keyword_args(**kwargs):
    # You can use **kwargs to let your functions take an arbitrary number of keyword arguments ("kwargs" means "keyword arguments"):
    # kwargs is a dict of the keyword args passed to the function
    # for key, value in kwargs.iteritems():
    #         print "%s = %s" % (key, value)

    # res will be a dictionnary of key,value
    res= kwargs.items() #this is a list of keys,values
    print res
    print res[0] #this this first set key,value
    print res[0][1] #this is first key,value set and it display only its value


def this_func(p1,p2,p3,p4=None):
    #The default argument ie p4=None must always come at the end of the list of mandatory args
    #A function can return more than one result, each of different type.
    #The result returned is a tuple (non modifiable)
    return p1, p2, p3, p4

print('this func:{}'.format( this_func(p2=22,p1='This first value is:',p4='<-This is a pipe sign',p3=' PIPE ')))

#To merge two lists and turn them into a dictionary
#Zip will create a list of tuples associating each element in each list
list_name=['Bruce Wayne','Docteur','Steve Ostin',]
list_hero=['Batman','Hulk','Lhomme qui vallait 1 milliard']
my_dic= { name:hero for name,hero in zip(list_name,list_hero)}
print('\ntype of my_dic: {}\nValue of Docteur in the generate dictionary: {}'.format(type(my_dic), my_dic['Docteur']))

res= [ x*x for x in range(1,20) ]
print res

print '\nMemory used by the script: {}MB'.format(mem.getrusage(mem.RUSAGE_SELF).ru_maxrss/1024)
