#!/usr/bin/env python
import signal
import sys
import time

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        # sys.exit(0)


def main2():
    signal.signal(signal.SIGINT, signal_handler)
    print 'bla'
    time.sleep(20)
    print 'blabla'

    # signal.pause()

def main():
    try:
        print "bla"
        time.sleep(10)
        print "bla"
    except KeyboardInterrupt:
        print "ctrl + c pressed"
        sys.exit()

if __name__ == '__main__':
    main2()
