#!/usr/bin/env python
"""
    Executes a sql file and will prompt the user for variables declared in the code
"""
import sys
import commands
import logging
import argparse
import re
import os

#BEGIN: Set the logger for file and console with different VERBOSE levels
logging.basicConfig(
     filename=(__file__).replace ('.py', '.log'),
     level=logging.DEBUG,
     format= '%(asctime)s, line %(lineno)d, %(levelname)s: %(message)s',
     #datefmt='%H:%M:%S'
 )
# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s, line %(lineno)d, %(levelname)s: %(message)s')
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
log = logging.getLogger(__name__)
#END: Set the logger

# try:
#     import psycopg2 as pgdriver
# except Exception, ex:
#     log.error ("ERROR: Failed to get a suitable postgres driver")
#     log.error ("You can install pycopg2 with: \tsudo apt-get install python-psycopg2")
#     log.error ("Or you can use bpgsql from the amelco svn repository")
#     exit (1)

#Error codes
ERR_UNKNOWN_ARG = 1

class Report(object):
    argsParser  = argparse.ArgumentParser()
    code        = None
    variables   = None

    def __init__(self, filename, variableList):
        log.info ("Opening file '%s' in read only mode" %filename)
        self.code = (open(filename, 'r')).read()

        #Find unique variables in the report in the format
        #  ${a-Z}
        # and build a argsparser for them
        reportVars = []
        log.debug ("Looking for variables...")
        for v in self.__findVariables():
            reportVars.append(v)

        reportVars = list(set(reportVars))
        log.info ("Found variables: '%s'" %reportVars)

        #Create a parser for these variables
        for v in reportVars:
            #Strip the
            v1 = self.__strip(v)
            self.argsParser.add_argument ('--'+v1,required=True, dest=v1)

        self.variables, not_found = self.argsParser.parse_known_args(variableList)

        log.debug ("Report variable list: '%s'" %self.variables)
        if len (not_found ) >=1:
            log.error ("Unknown arguments '%s'" %notfound)
            exit (ERR_UNKNOWN_ARG)

        self.__replaceVariables ()
    def __strip(self,variable):
        #
        return variable.replace ('${','').replace('}','')
    def __replaceVariables(self):
        if self.code is None:
            log.error ("report code is empty!")
        else:
            argsDict = vars(self.variables)
            for v in argsDict:
                self.code = self.code.replace ("${%s}" %v, argsDict[v])
            log.debug ("Final code is \n%s\n" %self.code)
    def __findVariables(self):
        if self.code is None:
            log.error ("report code is empty!")
        else:
            pattern = re.compile (r'(\$\{[a-zA-Z0-9_]+\})')
            for r in re.findall(pattern, self.code):
                yield r
    def __parseHeader(self):

        pass
    def getVariables(self):

        return self.variables
    def getCode(self):
        #
        return self.code

def parseArgs(args):
  import argparse
  args = args[1:] #remove the application name

  parser = argparse.ArgumentParser()
  parser.add_argument('filename', help='Path with filename to execute')
  #parser.add_argument ("-e","--env" , required=True , dest='env'     , help='environment NAME')
  parser.add_argument ("--verbose" , required=False , dest='verbose' , help='set verbosity to debug', action='store_true', default=False)

  found, not_found = parser.parse_known_args(sys.argv[1:])

  return found, not_found

if __name__ =='__main__':
    args, notfound = parseArgs(sys.argv)

    if args.verbose is True:
        console.setLevel(logging.DEBUG)
    else:
        console.setLevel(logging.ERROR)

    r = Report (args.filename, notfound)

    #Remove unused variables
    del notfound

    #os.system ('bash -c "source /usr/local/bin/setenv && setenv %s"' %args.env)
    #os.environ.update(env)
    #os.environ['DEBUSSY'] = '1'

    print r.getCode()
