#!/usr/local/env python

import logging

logger=logging.getLogger('example')

#CRITICAL - 50 something failed application must close
#ERROR - 40 some function failed
#WARNING - 30 something unexpected
#INFO - 20 confirmation that things are working as planned
#DEBUG - 10 details info

#To only display to the console
#logging.basicConfig(level=logging.DEBUG) #or level=10

#To log into a file
#logging.basicConfig(filename='logtest.log',level=10)

#this_format= "%(asctime)s [%(levelname)s] %(message)s "
this_format= "%(asctime)s %(levelname)s [ %(funcName)s ] %(message)s "
#logging.basicConfig(filename="test.log",format=this_format,level=30)
logging.basicConfig(format=this_format,level=30)

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
		logger.warn("Sold item: '{}'".format(self.name))


item_01= Item('sword',150)
item_01.buy()
item_01.sell()

"""
logging.logger.setlevel() #Redefine logging level
logging.logger.disabled=true #disable logging



"""
