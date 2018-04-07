#!/usr/bin/python

import sys
import re
import os
import argparse
import base64
# import sdscripts
# from collections import Counter
# from socket import gethostname
# from sysadmin.servicedesk.utils import appLoader
# from commands import getstatusoutput

return_code = 0


def get_managed_event_count(ms):
        status, output = ms.run_jmx('ats.betting.trading.algo:name=AlgoService -a NumberOfEvents')
        return output


def print_managed_event_count(ms):
        ms_event_count = get_managed_event_count(ms)
        print('{}: {}'.format(ms.print_host(), ms_event_count))


def get_all_market_servers():
        apps = appLoader.get_app('marketServer')
        return apps.instances


def get_commands(search_date, prod_path, prod_sport, script_pid):
    odir="{}_{}_coral_stats".format(search_date, prod_sport)
    remote_cmd="""
        #!/bin/bash

        cd /home/amelco/{1}/sysadmin/servicedesk
        ./newAdvancedSearch.bash -d {0} "^<\!DOCTYPE oxiFeedRequest" --ignore-zero > /tmp/{2}-mergedoutbound-oxiFeedRequests-{0}-{3}.txt
        ./newAdvancedSearch.bash -d {0} "CoralRetail.*oxiFeedRequest" --ignore-zero > /tmp/{2}-CoralRetail-oxiFeedRequest-{0}-{3}.txt
        ./newAdvancedSearch.bash -d {0} "CoralOnline.*oxiFeedRequest" --ignore-zero > /tmp/{2}-CoralOnline-oxiFeedRequest-{0}-{3}.txt
        ./newAdvancedSearch.bash -d {0} "LadbrokesOnline.*oxiFeedRequest" --ignore-zero > /tmp/{2}-LadbrokesOnline-oxiFeedRequest-{0}-{3}.txt
        ./newAdvancedSearch.bash -d {0} "HTTP latency of" -z --ignore-zero > /tmp/{2}-HTTP-Latencies-{0}-{3}.txt
        mkdir -p /tmp/{4}
        mv /tmp/{2}*{0}-{3}.txt /tmp/{4}/.
        tar  -C /tmp -cfz "{4}.tar.gz" "{4}"
        """.format(search_date,prod_path,prod_sport,script_pid,odir)
    print remote_cmd
    remote_cmd_sudo='sudo su - amelco -c "{} | base64 -d | bash "'.format(base64.b64encode(remote_cmd))
    return  remote_cmd_sudo

def main():

    print         get_commands('2017-05-05','prod-tennis','Tennis','PID123')


        # parser = argparse.ArgumentParser()
        # parser.add_argument('marketServer', nargs='?')
        # args = parser.parse_args()
        # all_market_servers = get_all_market_servers()
        # if args.marketServer:
        #         ms_filter = args.marketServer.split(',')
        #         check_servers = [ms for ms in all_market_servers if ms.host[1] in ms_filter]
        # else:
        #         check_servers = get_all_market_servers()
        # if not check_servers:
        #         if args.marketServer:
        #                 print('No Market servers were found with argument: {}'.format(args.marketServer))
        #         else:
        #                 print('No market servers were found.')
        # for market_server in check_servers:
        #         print_managed_event_count(market_server)
        # sys.exit(return_code)


if __name__ == '__main__':
        main()
