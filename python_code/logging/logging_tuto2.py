#!/usr/bin/env python

import logging


#CRITICAL - 50 something failed application must close
#ERROR - 40 some function failed
#WARNING - 30 something unexpected
#INFO - 20 confirmation that things are working as planned
#DEBUG - 10 details info

#To log info on console and log file, you set set up the main logger
#and add handlers
logger=logging.getLogger('example')
logger.setLevel(logging.DEBUG)

#Create logging handlers (as many as you want)
#1. one for the console and one for the file.
fh= logging.FileHandler("logging_tuto_file_handler.log")
ch= logging.StreamHandler()

#2. Create a formatter
this_format= "%(asctime)s %(levelname)s [ %(funcName)s ] %(message)s "
formatter = logging.Formatter(this_format)

#3. Assign a formatter (can be the same or different)
fh.setFormatter(formatter)
ch.setFormatter(formatter)

#4. Assign a logging level (can be the same or different)
# fh.setLevel(20)
# ch.setLevel(10)
fh.setLevel(logging.INFO)
ch.setLevel(logging.DEBUG)

# 5. Add the handlers to the streaming logger
logger.addHandler(fh)
logger.addHandler(ch)


class Item(object):
	"""Base Item class"""

	def __init__(self,name,value):
		self.name=name
		self.value=value
		#logger.debug("Item created: '{}({})'".format(self.name,self.value)) #placeholder syntax python 3.1
		logger.debug("Item created: '%s (%d)'" %(self.name,self.value)) #placeholder syntax python 2 and 3

	def buy(self,quantity=1):
		"""Buy item"""
		logger.debug("Bought item: '{}'".format(self.name))

	def sell(self,quantity=1):
		"""sell item"""
		logger.debug("Sold item: '{}'".format(self.name))


# item_01= Item('sword',150)
# item_01.buy()
# item_01.sell()
# item_01.sell()
# item_01.sell()

"""
logging.logger.setlevel() #Redefine logging level
logging.logger.disabled=true #disable logging
"""

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
