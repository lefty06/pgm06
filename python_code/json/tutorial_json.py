#!/usr/bin/python
#crtl + shift + b to compile
#crtl + shift + p
#Ctrl+Shift+d	to Duplicate line
#Ctrl+Shift+k	to Delete line
#Ctrl+\	toggle to comment uncomment
#crtl + p
#Anaconda Disable/Enable linting degfault settings file
#Json online validator, http://jsonlint.com/
#Optimize code, https://wiki.python.org/moin/PythonSpeed/PerformanceTips#Overview:_Optimize_what_needs_optimizing
import os
import json
import pprint


#Json is an alternative to XML, it takes a pairs of key:values, the key always being a string and the value that can be anything (string,list, dictionnary, integer, object, etc.... ), json_file={'name':"pat",'age':20,'hobbies':['boobs','tits','jugs']}
#To navigate a json file you need to get familiar with it's structure first!
#Example 1
#Triple quote to comment code blocks

'''data = [ { 'b':(2, 4),'a':'A',  'c':3.0 } ]

data_json = json.dumps(data,sort_keys=True,indent=3)
print 'ENCODED:', data_json

decoded = json.loads(data_json)
print 'DECODED:', decoded

print 'ORIGINAL type:', type(data[0]['b'])
print 'DECODED type:', type(decoded[0]['b'])
'''

# Example 2
# you can create the contents, convert to json(encode/dump) and to print the contents of a json u need to decode/load
'''
json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
json_encoded = json.dumps(json_string,sort_keys=True,indent=3)
parsed_json = json.loads(json_encoded)
print(parsed_json['names']['first_name'])

d = {'first_name': 'Guido','second_name': 'Rossum','titles': ['BDFL', 'Developer']}
print(json.dumps(d,sort_keys=True,indent=5))
'''

#Example 3 Create json from Objects
'''
class User(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password

# o.__dict__ is a simple catch all for user defined objects but we can also add support for others objects. For instance sets will be treated as lists
def jdefault(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__

alice = User('Alice A. Adams', 'secret')
pets = set([u'Tiger', u'Panther', u'Toad'])

print(json.dumps(alice, default=jdefault))
print(json.dumps(pets, default=jdefault))
'''

#Example 4

#chr converts Interger to ASCII
# ds = dict((chr(i), range(i, i+5)) for i in range(65,70))
# print ds
# pprint.pprint (ds)

#json_file_name='/home/pat/Documents/python_scripts/json/servers.json'
# json_file_name='/home/pat/Documents/python_scripts/json/s.json'
#
# with open(json_file_name) as fd:
#  	fs=json.load(fd)
#
# pprint.pprint(fs)
# print '------------------------------'
# print "check type, type(fs): ",type(fs)
# print "check keys,fs.keys(): ",fs.keys()
# print "check type,type(fs['alias']): ",type(fs['alias'])
# print "count keys, len(fs['alias'].keys()): ",len(fs['alias'].keys())
# print "check keys,fs['alias'].keys(): ",fs['alias'].keys()
# print type(fs['alias']['jump'])
# print fs['alias']['jump']


'''
#The count section does not return correct results
count_items=len(fs['features'][0]['name'])
count_items2=len(fs['features'][0]['classifiers'][0])
print "Json total count of name items: ",  count_items
print "Json total count of name items: ",  count_items2

#This works
counties = [item for item in fs["features"]
	if item["name"] == "Los Angeles"]
	#if item["classifiers"][0]["name"] == "Los Angeles"]

print "Number of items found:", len(counties)
pprint.pprint(counties)
'''
