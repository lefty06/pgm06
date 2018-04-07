#!/usr/bin/python
# crtl + shift + b to compile
#crtl + shift + p
#crtl + p
# Anaconda Disable/Enable linting degfault settings file
# All over the place file for testing.
# http://www.python-course.eu/sys_module.php
# http://www.bogotobogo.com/python/python_subprocess_module.php

import os
import json
import sys
import commands
import subprocess

"""
os.system('pwd') #the easiest way to execute a cmd

This is basically just like the Popen class and takes all of the same arguments, but it simply wait until the command completes and gives us the return code.

IMPORTANT Note: call and check_call cannot be assigned to a variable, the ouput cannot be captured in a variable. check_output can to this
    *call* just calls the program.
    *check_call* calls the program and throws an exception if it fails.
    *check_output* calls the program, throws an exception if it fails, and returns the output of the program.
On Unix with shell=True, the shell defaults to /bin/sh.
Note Do not use stdout=PIPE or stderr=PIPE with this function as that can deadlock based on the child process output volume.

More advanced use cases can be handled by subprocess.Popen objects.
When Popen is used it needs to either communicate or be closed and do not use shell=true!
Popen will return stdout, stderr or both (array) but not stdin.


To investigate proc.poll() which returns return code or None
proc.terminate()  = proc.kill()
"""


def example1():
    """
    the call function will return everything (stdout and stderr) including errors returned by the shell
    """
    # subprocess.call(['ls -l teost*', '-1'], shell=True)
    subprocess.call(['ls -l testo*', '-1'], shell=True)


def example2():
    """
    the check_call function works like call expect that stderr is checked and CalledProcessError exception is raised if an error code is detected. Not sure what is the point of capturing it???
    """
    try:
        res = subprocess.check_call(['pwd'], shell=True)
        return res
    except subprocess.CalledProcessError:
        print 'Captured subprocess.CalledProcessError, what do we do now?'

    # Quirky test, watch out the value returned is 0 because of pwd
    #subprocess.check_call(['ls -l teost*;pwd'], shell=True)


def example3():
    """
    check_output can be captured and will also raise an exception is there's an error exit code returned by the shell
    """
    sout = subprocess.check_output(['ls -l test*'], shell=True)
    print sout


def example4():
    """
    using PIPE to capture stdout
    """
    # subprocess.Popen() executes a child program in a new process.

    # Method 1 deprecated
    str_os_out = os.popen("echo 'os execute'").read()
    print "str_os_out:\n", str_os_out

    print '-------------------------'

    # Method 2
    str_subprocess_out = subprocess.Popen(
        "echo subprocess execute", stdout=subprocess.PIPE, shell=True).stdout.read()
    print 'str_subprocess_out:\n', str_subprocess_out

    print '-------------------------'

    # Method 3
    str_subprocess_out2 = subprocess.Popen(
        "ls subprocess execute", stdout=subprocess.PIPE, shell=True)
    str_subprocess_out3 = str_subprocess_out2.communicate()
    print "str_subprocess_out3:\n", str_subprocess_out3[0]


def example5():
    """
    Using PIPE to capture stdout stderror and return code
    """
    # will return an array using space a separator
    #CMD = shlex.split('grep -l HORSE /home/pat/Documents/python_scripts/misc/1.xml')
    # CMD='ls "Hello world!"'.split(' ')

    # Note that both stdout and stderr are captured indepandentely ie >stdout 2>stderr
    proc = subprocess.Popen(['ls', '"Hello world!"'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = proc.communicate()
    print 'stdoutdata:\n', stdoutdata
    print 'stderrdata:\n', stderrdata
    print 'return code:\n', proc.returncode


def example6():
    """
    Redirect stderr in stdout
    """
    # Note that both stderr is redirected to stdout ie 2>&1
    proc = subprocess.Popen(['ls', '"Hello world!"'],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (stdoutdata, stderrdata) = proc.communicate()
    print 'stdoutdata:\n', stdoutdata
    print 'stderrdata:\n', stderrdata
    print 'return code:\n', proc.returncode


def example7():
    """
    Using PIPE and stdin to simulate user input
    this simulated s user input, check bash script
    """
    proc = subprocess.Popen(
        ['/bin/bash', '/home/pat/Documents/python_scripts/subprocess/subprocess_example7.bash'],  stdin=subprocess.PIPE)
    print proc.communicate(' Hello?')
    print 'return code: ', proc.returncode


def example8():
    """
    Using PIPE and stdin to simulate user input
    this simulated s user input (check bash script) and then captures stdout and stderror
    """

    # NOT WORKING?
    proc = subprocess.Popen(['/bin/bash', '/home/pat/Documents/vscode2018/python_code/subprocess/subprocess_example7.bash'],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = proc.communicate('testing this script')
    print 'stdoutdata:\n ', stdoutdata
    print 'stderrdata:\n ', stderrdata
    print 'return code:\n', proc.returncode


def example9():
    """
    this one hurts, dont really know what's the use case for it
    The p1.stdout.close() call after starting the p2 is important in order for p1 to receive a SIGPIPE if p2 exits before p1.
    """
    p1 = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', '-A1', 'system'], stdin=p1.stdout,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits
    p = p2.communicate()
    print 'stdoutdata: \n', p[0]
    print 'stderrdata: \n', p[1]
    print 'return code:\n', p2.returncode  # for some reason cannot get p.returncode

# Note: reference to example 8 where a script is being called but a function could not have been because the subprocess module is for spawning processes and doing things with their input/output - not for running functions.
# from multiprocessing import Process, Queue
#
# def my_function(q, x):
#     q.put(x + 100)
#
    # queue = Queue()
    # p = Process(target=my_function, args=(queue, 1))
    # p.start()
    # p.join() # this blocks until the process terminates
    # result = queue.get()
    # print result


if __name__ == '__main__':
    example8()
