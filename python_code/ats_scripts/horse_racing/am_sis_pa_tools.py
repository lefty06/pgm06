import os
from os import path
import sys
import argparse
import re
import subprocess
from datetime import datetime as dt, timedelta as td
import logging

'''
os.path.isfile('/etc')  # False, it only checks if the file exists
os.path.isfile('/etc/filename.txt')  # False, it only checks if the file exists
os.path.exists("/etc/password.txt")  # True, checks if the file or dir exists
os.path.exists("/etc/password.txt")  # True, checks if the file or dir exists
'''

logger=logging.getLogger('example')
this_format= "%(asctime)s %(levelname)s [ %(funcName)s ] %(message)s "
logging.basicConfig(format=this_format,level=logging.CRITICAL)

global script_name
script_name=__file__

def subprocess_cmd(command):
    logger.debug('executing: {}'.format(command))
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()

def isCompressed(str_file):
    logger.debug('checking file: {}'.format(str_file))
    res=str_file.lower().endswith(('.tar.gz', '.tar.bz2', '.tgz','.tz2','.gz','.bz2'))
    return res

def grep_string(seach_pattern,file):
    logger.debug('seach_pattern:{}, file: {}'.format(seach_pattern,file))
    with open(file) as f:
        for l in f:
            # print l
            if re.search(seach_pattern,l,re.M|re.I):
                return True
        return False

def search_dir_date(feed=None,number_of_days=0,abspath=None):
    logger.debug('feed: {}, Num of days: {}, abspath: {}'.format(feed,number_of_days,abspath))
    #this is how you can declare optional arguments
    dir_dates=[]

    if abspath <> None:
        dir_dates.append(abspath)
        return dir_dates

    for i in xrange(number_of_days+1):
        d=(dt.now() - td(days=i)).strftime('%Y-%m-%d')
        # dir_dates.append('/home/amelco/http-{0}/{1}'.format(feed,d))
        dir_dates.append('/home/pat/Documents/python_scripts/misc/{1}'.format(feed,d))
    return dir_dates

def search_xmls(feed,ldir=[]):
    logger.debug('feed:{}, number of dirs to check:{}'.format(feed,len(ldir)))
    # print(os.path.isdir("/home/el"))
    # print(os.path.exists("/home/el/myfile.txt"))
    search_res=[]
    search_err=[]
    search_files=[]

    for p in ldir:
        if os.path.isdir(p):
            for i in os.listdir(p):
                # fullpathfile='{0}/{1}'.format(p,i)
                fullpathfile=os.path.join(p,i) #This is a better way to construct the full path ie path+fileame because os path takes into account the OS / or \
                if i.endswith('.xml') and path.isfile(fullpathfile) and not isCompressed(fullpathfile):
                    if feed.lower() == 'sis' :
                        str_sis='MasterDoc'
                        if grep_string(str_sis,fullpathfile):
                            search_files.append(fullpathfile)
                    if feed.lower() == 'pa':
                        str_pa='HorseRacingCard'
                        if grep_string(str_pa,fullpathfile):
                            search_files.append(fullpathfile)
        else:
            # print 'cannot access:{}'.format(p)
            search_err.append(p)
            # files = [x for x in os.listdir(p) if path.isfile(p+os.sep+x)]
            # files+= [file for file in os.listdir(p) if f.endswith('.xml')]
    search_res=[search_err, search_files]
    return search_res

def copy_files(list_files,output_dir):
    logger.debug('copying {} in output_dir:{}'.format( len(list_files),output_dir))
    res=[]
    #Empty output dir
    if os.path.isdir(output_dir):
        CMD='rm {}/* 2>/dev/null'.format(output_dir)
        subprocess_cmd(CMD)

        CMD='cp {} {}'.format(' '.join(list_files),output_dir)
        subprocess_cmd(CMD)

        res.append('All files copied in {}'.format(output_dir))
    else:
        res.append('Cannot find ouput directory {}, files haven\'t been copied.'.format(output_dir))
    return res

def gather_and_copy(feed, days=2):

    list_of_dirs=search_dir_date(feed,days)
    res_search=search_xmls(feed,list_of_dirs)

    if len(res_search[1]) > 0 :
        # print "\nList of {} creation xmls ({}):\n{}".format(feed,len(res_search[1]),'\n'.join(res_search[1]))
        print '\n{} XMLs found: {}'.format(feed.upper(),len(res_search[1]))
        cpfiles=copy_files(res_search[1],'/tmp/temp_res')
        print ''.join(cpfiles)

        if len(res_search[0]) > 0:
            print '\nCannot access directory:\n{}'.format('\n'.join(sorted(res_search[0],reverse=True)))
    else:
        print 'No XMLs found'

        if len(res_search[0]) > 0:
            print '\nCannot access directory:\n{}'.format('\n'.join(sorted(res_search[0],reverse=True)))

def print_help(s=script_name):
    str_help='Usage: python {0} [pa|sis] {{number_of_days}}\n\
    -[pa|sis]             :To gather pa or sis XMLs\n\
    -[INT number_of_days] :To gather Xmls for the last X days (Optional argument, Default value=2 days)\n\
    \ne.g.:\n\
    python {0} pa   #To gather PA XMLs in the past 2 days\n\
    python {0} pa 5 #To gather PA XMLs in the past 5 days\n'.format(script_name)
    return str_help

def Main():
    parser = argparse.ArgumentParser()
    #Takes 0 or more arguments and will store them in a list called fargs
    parser.add_argument('-f','--feed',dest='fargs',nargs='*',help='Choose feed sis|pa',default=None)
    args = parser.parse_args()

    if not args.fargs  :
        print "{}".format(print_help())
        sys.exit("Not enough args\n")
    elif len(args.fargs) == 1 and args.fargs[0].lower() in ('pa','sis'):
        gather_and_copy(args.fargs[0])
    elif args.fargs[0].lower() in ('pa','sis') and len(args.fargs) > 1 and args.fargs[1].isdigit() == True:
        gather_and_copy(args.fargs[0], int(args.fargs[1]))
    else:
        # print '{}'.format(args.fargs)
        print "{}".format(print_help())
        sys.exit("\n")


if __name__ == '__main__':
    Main()
