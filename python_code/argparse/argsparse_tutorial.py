#!/usr/bin/python
# -*- coding: utf-8 -*-
#to avoid error: syntaxError: Non-ASCII character '\xc2' in file
import argparse

'''

parser.add_argument('-s','--serie',help='Store a simple value',required=True)
By default all argument are optional except if you mention required=True
-s or --serie can be used and must be followed an value ie -s value_of_arg

parser.add_argument('-s','--serie', action='store', dest='simple_value',default=333,help='Store a simple value',type=int,required=True)
default will be the default value of simple_value is -s|--serie is not used
dest='simple_value' will determine the name of variable where the argument is stored ie args.simple_value
type=int is the type of the variable simple_value

parser.add_argument('-e',dest='desp',nargs='+')
-e must have 1 or more values that will be stored in a list called desp. the default=whatever will be ignored

parser.add_argument('-p',dest='desp2',nargs='*',default='Hello') or default=['Hello']
-P can have 0 or more values that will be stored in a list called desp. the default=whatever can be used

--------------------

dest: You will access the value of option with this variable
help: This text gets displayed whey someone uses --help.
default: If the command line argument was not specified, it will get this default value.
action: Actions tell optparse what to do when it encounters an option on the command line. action defaults to store.
These actions are available:
    store: take the next argument (or the remainder of the current argument), ensure that it is of the correct type, and store it to your chosen destination dest.
    store_true: store True in dest if this flag was set.
    store_false: store False in dest if this flag was set.
    store_const: store a constant value
    append: append this option’s argument to a list
    thecount: increment a counter by one
    callback: call a specified function
nargs: ArgumentParser objects usually associate a single command-line argument with a single action to be taken. The nargs keyword argument associates a different number of command-line arguments with a single action.
required: Mark a command line argument as non-optional (required).
choices: Some command-line arguments should be selected from a restricted set of values. These can be handled by passing a container object as the choices keyword argument to add_argument(). When the command line is parsed, argument values will be checked, and an error message will be displayed if the argument was not one of the acceptable values.
type: Use this command, if the argument is of another type (e.g. int or float).
'''



def Main(): #simple argpase example
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', action='store', dest='simple_value',
                        help='Store a simple value')

    parser.add_argument('-c', action='store_const', dest='constant_value',
                        const='value-to-store',
                        help='Store a constant value')

    parser.add_argument('-t', action='store_true', default=False,
                        dest='boolean_switch',
                        help='Set a switch to true')
    parser.add_argument('-f', action='store_false', default=False,
                        dest='boolean_switch',
                        help='Set a switch to false')

    parser.add_argument('-a', action='append', dest='collection',
                        default=[],
                        help='Add repeated values to a list',
                        )

    parser.add_argument('-A', action='append_const', dest='const_collection',
                        const='value-1-to-append',
                        default=[],
                        help='Add different values to list')
    parser.add_argument('-B', action='append_const', dest='const_collection',
                        const='value-2-to-append',
                        help='Add different values to list') #Clever, it adds a constant to an existing array ie const_collection

    parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')

    #to test from terminal with input
    # results = parser.parse_args()
    # print 'simple_value     =', results.simple_value
    # print 'constant_value   =', results.constant_value
    # print 'boolean_switch   =', results.boolean_switch
    # print 'collection       =', results.collection
    # print 'const_collection =', results.const_collection

    #to test from script parsing the arguments
    print parser.parse_args(['-sbla']) #there's different ways to parse args for testing, no need to use terminal
    print parser.parse_args(['-s','bli']) #there's different ways to parse args for testing, no need to use terminal
    print parser.parse_args(['-s=blo']) #there's different ways to parse args for testing, no need to use terminal
    print parser.parse_args(['-s=blo','-c']) #there's different ways to parse args for testing, no need to use terminal
    print parser.parse_args(['-s=blo','-c','-t']) #there's different ways to parse args for testing, no need to use terminal
    print parser.parse_args(['-s=blo','-c','-t','-aHello','-a',' Its me']) #there's different ways to parse args for testing, no need to use terminal
    print parser.parse_args(['-s=blo','-c','-t','-aHello','-a',' Its me','-A','-B']) #there's different ways to parse args for testing, no need to use terminal
    print parser.parse_args(['-s=blo','-c','-t','-aHello','-a',' Its me','-A','-B']) #there's different ways to parse args for testing, no need to use terminal
    print parser.parse_args(['-s=blo','-c','-t','-aHello','-a',' Its me','-A','-B','-A']) #there's different ways to parse args for testing, no need to use terminal
    print parser.parse_args(['-v']) #there's different ways to parse args for testing, no need to use terminal

def fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        return a

def Main2(): #simple argpase example
#python script -f 8 -d 'blabla'
    parser = argparse.ArgumentParser()
    # parser.add_argument('--fibo') #the argument will be a string by default if not specified
    parser.add_argument('-d','--disclaimer')
    parser.add_argument('-f','--fibo',type=int)
    args = parser.parse_args()

    # print parser.parse_args(['-f','8','-d','bla']) #to parse values equivalent of executing the script python script -f 8 -d bla

    print 'disclaimer: {}'.format(args.disclaimer)
    print 'Fib: {}'.format(fib(args.fibo))
    print 'args:{}'.format(args) #Displays everything, good for debugging


def Main3():
#python script -f 8 -v
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v','--verbose',action="store_true")
    group.add_argument('-q','--quiet',action="store_true")

    # parser.add_argument('num',help="Calculates Fibonacci number",type=int)
    parser.add_argument('-n','--num',help="Calculates Fibonacci number",type=int)
    parser.add_argument('-e','--email')
    args = parser.parse_args()

    res=fib(args.num)

    if args.verbose:
        print 'The finbonacci suite of {} is {}'.format(args.num,res)
    elif args.quiet:
        print '{}'.format(res)
    else:
        print '{}:{}'.format(args.num,res)

    if args.email:
        print args.email

    print 'args:{}'.format(args)


def Main4():
    parser = argparse.ArgumentParser()
    # parser.add_argument('-e',action='store',dest='desp',default=333,type=int)
    parser.add_argument('-e',dest='desp',nargs='+',type=int) #nargs +: 1 or more args
    parser.add_argument('-p',dest='desp2',nargs='*',default=['Hello']) #nargs *: 0 or more args
    args = parser.parse_args()

    if args.desp:
        print 'desp'
        print '{}'.format(args.desp)

    if args.desp2:
        print 'desp2'
        print '{}'.format(args.desp2)

def PD_Main():
    parser = argparse.ArgumentParser(description='Get bets from a list of IDs or a file with IDs')

    #you can create as many groups as needed
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f','--file',type=argparse.FileType('r'),help='Um fecheiro caralho')
    group.add_argument('-l','--list',nargs='+',type=int,help='uma lista de INTs caralho')

    parser.add_argument('-b','--bets',action="store_true",required=True)

    #to test from terminal: python -b -f abspath/file
    args=parser.parse_args()
    if args.file:
        print args.file.readlines()
    if args.list:
        print args.list

    #TO TEST ARGPARSE from atom crtl+shift+b
    # print parser.parse_args(['-h']) #correct
    # print parser.parse_args(['-b']) #correct
    # print parser.parse_args(['-b','-l=12']) #correct
    # print parser.parse_args(['-b','--file=/home/pat/Documents/python_scripts/argparse/f.txt']) #correct
    # print parser.parse_args(['-b','-l=2','--file=/home/pat/Documents/python_scripts/argparse/f.txt']) #FDS

if __name__ == '__main__':
    PD_Main()
