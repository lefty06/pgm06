#!/usr/bin/python
import commands
import os
import subprocess
import sys
import readline
from datetime import datetime
import logging


"""
Modules:
Logging level to debug app
get current and absolute path
execute os commands
execute os commands and get status output

"""


logger=logging.getLogger('example')
this_format= "%(asctime)s %(levelname)s [ %(funcName)s ] %(lineno)s - %(message)s "
logging.basicConfig(format=this_format,level=20)



def getAppPath():
    #app_path = os.path.abspath(app_path)
    app_path = os.getcwd()
    logger.debug("app_path: {} ".format(app_path) )
    return app_path

def getHomeDir():
	logger.debug("home dir: {} ".format(os.path.expanduser('~')) )
	return os.path.expanduser('~')


if __name__ == '__main__':
	logger.info("Main start" )
	l= getAppPath()
	# logger.info("current path: " +  l) #better using the below syntax to concat strings
	logger.info("current path: {0}".format(l))

	#To return the current directory
	l=os.path.dirname(os.path.abspath('/home/toto/file.py'))
	logger.info( "extract dirname: {0}".format(l))
	l=os.getcwd()
	logger.info( "extract dirname: {0}".format(l))


	#To return the current filename
	l=os.path.basename(__file__)
	logger.info( "current file name: {0}".format(l))
	l=os.path.split(os.path.abspath('/home/toto/file.py'))
	logger.info( "list of dirname and file: {0}".format(l))

	#Execute a command in the shell and returns a list with status code and output
	cmd="date"
	lst=commands.getstatusoutput('pwd')
	logger.info( "list of error code and cmd output: {0}".format(l))
