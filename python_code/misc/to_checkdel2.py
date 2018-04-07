#!/usr/bin/python

import sdscripts

import argparse
import json
import os
import sys

from sysadmin.servicedesk.python import jmx_check_workers
from sysadmin.servicedesk.utils.commonUtils import color_string
from sysadmin.servicedesk.utils.appShortcutHandler import AppConfig, AppNotFoundException
from sysadmin.servicedesk.utils import appLoader
from sysadmin.servicedesk import config as servicedesk_config

appLoader.set_throw_exceptions()


def check_all_workers_for_all_servers(ms_servers, servers, config):
    print(color_string('Checking market server workers for: {}\n'.format(', '.join([s.cfg_name for s in servers])), 'BOLD'))
    all_results = []
    for server in servers:
        print(color_string('Checking {}'.format(server.print_hosts_pretty()), 'HEADER'))
        result = check_workers_for_server(ms_servers, server, config)
        all_results.append(result)
        if result:
            print(color_string('OK', 'GREEN'))
        else:
            print(color_string('BAD!!', 'RED'))
        print('')
    return all_results



def check_workers_for_server(ms_servers, server, config):
    if not server.instances:
        print('No {}s are configured to run'.format(server.name))
        return False
    print('Checking worker status for {} - {}'.format(server, server.instances))
    if server.cfg_name == 'marketServer':
        bean_prefix = 'ats.ms.stub:name='
        bean_name = 'AtsGroupStub'
    else:
        bean_prefix = 'ats.ms.feed.proxy:name='
        bean_name = config[server.cfg_name]
    return jmx_check_workers.get_all_workers_status(ms_servers, bean_prefix=bean_prefix, bean_name=bean_name, bean_attribute='WorkerMemberNames')


def get_market_server_worker_config():
    config_dir = os.path.dirname(servicedesk_config.__file__)
    config_file = os.path.join(config_dir, 'check_market_server_workers.json')
    if os.path.isfile(config_file):
        with open(config_file, 'r') as f:
            return json.loads(f.read())
    else:
        raise ValueError('No sysadmin/servicedesk/config/check_market_server_workers.json config found')


def get_servers_list(server_names, filter_config):
    app_config = AppConfig()
   if server_names == 'all':
        return [app for app in appLoader.all_apps.values() if app.instances and app.cfg_name in filter_config]
    else:
        all_servers = []
        for server_name in server_names.replace(' ', '').split(','):
            try:
                servers = app_config.get_app_var(server_name)
                if servers.cfg_name in filter_config:
                    all_servers.append(servers)
                else:
                    print("The application '{}' has not been defined in the config.".format(server_name))
            except AppNotFoundException:
                print("The application '{}' does not exist.".format(server_name))
        return all_servers


def get_ms_servers():
    return appLoader.get_app('marketServer')


def main():
    parser = argparse.ArgumentParser('A JGroups checker which inspects the market server workers')
    parser.add_argument('servers', help='A comma-delimited list of servers to check against')
    args = parser.parse_args()
    market_server_worker_config = get_market_server_worker_config()
    server_list = get_servers_list(args.servers, market_server_worker_config)
    ms_servers = get_ms_servers()
    print(ms_servers)

    if all(check_all_workers_for_all_servers(ms_servers, server_list, market_server_worker_config)):
        print(color_string('Workers are OK', 'GREEN'))
        return 0
    else:
        print(color_string('Workers are not OK!!!', 'RED'))
        return 1


if __name__ == '__main__':
    sys.exit(main())
