#!/usr/bin/python

import sys
import re
import os
import argparse
import sdscripts
from collections import Counter
from socket import gethostname
from sysadmin.servicedesk.utils import appLoader
from commands import getstatusoutput

return_code = 0
zabbix_bool = False
email_bool = False
email_string = []


def zprint(print_string):
        if not zabbix_bool:
                print(print_string)
        email_string.append(print_string)


def get_ms_managed_events(ms):
        ms.get_managed_events()
        ms_events = ms.managed_events
        zprint('{}: {}'.format(ms.print_host(), len(ms_events)))
        return ms_events


def get_all_managed_events():
        apps = appLoader.get_app('marketServer')
        all_events = []
        for appInst in apps.instances:
                all_events += get_ms_managed_events(appInst)
        return all_events, apps


def run_check():
        all_events, apps = get_all_managed_events()
        dupes = [x for x, y in Counter(all_events).iteritems() if y > 1]
        zprint('')
        if dupes:
                global return_code
                return_code = 1
                zprint('{} Duplicate(s) were found...'.format(len(dupes)))
                for dupe in dupes:
                        ms_list = []
                        for app in apps.instances:
                                if dupe in app.managed_events:
                                        ms_list.append(app)
                        zprint('{0}: {1}'.format(dupe, ', '.join(x.print_host() for x in ms_list)))
        else:
                zprint('No dupes were found.')


def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('--email', action='store_true')
        parser.add_argument('--zabbix', action='store_true')
        args = parser.parse_args()
        global email_bool
        global zabbix_bool
        if args.email:
                email_bool = True
        if args.zabbix:
                zabbix_bool = True
        run_check()
        if return_code > 0 and args.email:
                if 'ATS_INSTANCE_NAME' in os.environ:
                        env_long_name = os.environ['ATS_INSTANCE_NAME']
                else:
                        env_long_name = gethostname()
                status, output = getstatusoutput('echo "{0}" | mailx -s "{1} - Duplicate events managed" "{2}"'.format('\n'.join(email_string), env_long_name, 'servicedesk@amelco.co.uk'))
        if args.zabbix:
                print return_code
