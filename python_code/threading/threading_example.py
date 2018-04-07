#!/usr/bin/env python

import time
import threading
from threading import Thread

# http://www.python-course.eu/threads.php
# https://pymotw.com/2/threading/
# http://effbot.org/zone/thread-synchronization.htm

"""
#Example 1
#No need to declare a threading class to use threading
class MyThread(threading.Thread):
	def run(self):
		print ("About to sleep")
		time.sleep(5)
		print ("Finished sleeping")

m=MyThread();
m.start()

time.sleep(1)
print ("I'm still running")

"""

"""
#Example 2
def print_t(name,delay):
	while 1:
		time.sleep(delay)
		print name

	thread.start_new_thread(print_t, ("First thread",1))
	thread.start_new_thread(print_t, ("Second thread",2))

time.sleep(4)
print "Hello"

#Strangely, print hello will stop the infinite loop???
#but the below loop will ensure it does not???
while 1:
	pass
"""

#Example 3
def timer(name,delay,repeat):
	print "Timer " + name + " Started"
	while repeat > 0:
		time.sleep(delay)
		print name + ": " + str(time.ctime(time.time()))
		repeat -= 1
	print "Timer: " + name + " Completed"

def Main():
	t1 = Thread(target=timer, args=("Timer1",1,3))
	t2 = Thread(target=timer, args=("Timer2",2,5))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	#print str(t1.isAlive())
	print "*********** Main complete **************"


if __name__ == '__main__':
	Main()



"""
#giving a threadname is optionnal
threadname.start()
threadname.run() #no need its is included in start()
threadname.join() #will wait for the previous thread to finish
"""

# There are two modules which support the usage of threads in Python, thread and threading, the thread module has been considered as "deprecated" for quite a long time.


# without join:
# +---+---+------------------                     main-thread
#     |   |
#     |   +...........                            child-thread(short)
#     +..................................         child-thread(long)

# When using start, threads and main instructions that might follow the threads will all be executed in parallel whichever finishes first

# with join
# +---+---+------------------***********+###      main-thread
#     |   |                             |
#     |   +...........join()            |         child-thread(short)
#     +......................join()......         child-thread(long)

# with join and demon thread
# +-+--+---+------------------***********+###     parent-thread
#   |  |   |                             |
#   |  |   +...........join()            |        child-thread(short)
#   |  +......................join()......        child-thread(long)
#   +,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,     child-thread(long+demonized)

# '-' main-thread/parent-thread/main-program execution
# '.' child-thread execution
# '#' optional parent-thread execution after join()-blocked parent-thread could
#     continue
# '*' main-thread 'sleeping' in join-method, waiting for child-thread to finish
# ',' demonized thread - 'ignores' lifetime of other threads;
#     terminates when main-programs exits; is normally meant for
#     join-independent tasks

# so the reason you don't see any changes is because you main-thread does nothing after your join. You could say join is (only) relevant for the execution-flow of the main-thread.

# If you for example want to concurrently download a bunch of pages to concatenate them into a single large page you may start concurrently downloads using threads, but need to wait until the last page/thread is finished before you start assembling a single page out of many. That's when you use join().
