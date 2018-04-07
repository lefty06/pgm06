# # m h  dom mon dow   command
# 0    3    *    *    *    /home/chris.billing/report_error_calling_feeds.py --email "miguel.rebollo@ladbrokescoral.com,cbilling@amelco.co.uk,servicedesk@amelco.co.uk" >>/home/chris.billing/report_error_calling_feeds.log 2>&1
#

#!/usr/bin/env python

import argparse
import base64
import commands
from datetime import datetime as dt, timedelta as td
import json
import logging

LOGGING_FORMAT = '%(asctime)-15s %(levelname)s %(name)s [%(process)d] %(message)s'
logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)

logger = logging.getLogger('FeedErrorReporter')





SEARCH_CMD = """sudo su - amelco -c 'cd /home/amelco/$(cat ~/.default_env)/sysadmin/servicedesk; svn update; /home/amelco/$(cat ~/.default_env)/sysadmin/servicedesk/test_advanced_search.bash -z -d $(date -d "-1 day" +"%Y-%m-%d") --json-output /tmp/{}-feed-search.json --suppress-file-name --commands " -A1 -E -h" "Error calling /feeds/ats/"'"""
SCP_CMD = """scp {0}:/tmp/{0}-feed-search.json /tmp/{0}-feed-search.json"""

ALL_SERVERS = [
    ("wkse13p1xamfoot01", "CORAL PRODUCTION FOOTBALL"),
    ("wkse13p1xamten01", "CORAL PRODUCTION TENNIS"),
    ("wkse13p1xamhrgh01", "CORAL PRODUCTION RACING"),
    ("wkse13p1xamother01", "CORAL PRODUCTION OTHER"),
]

SPORT={
    "Football":{
        "Host":"wkse13p1xamfoot01",
        "env_name":"prod-football"
    },
    "Tennis":{
        "Host":"wkse13p1xamfoot01",
        "env_name":"prod-tennis"
    }
}

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
    # print remote_cmd
    remote_cmd_sudo='sudo su - amelco -c "{} | base64 -d | bash "'.format(base64.b64encode(remote_cmd))
    return  remote_cmd_sudo


def run_grep_on_server(server):
    logger.info('Running grep on {}'.format(server))
    search_cmd = SEARCH_CMD.format(server)
    status, output = commands.getstatusoutput('ssh {} "echo {} | base64 -d | bash"'.format(server, base64.b64encode(search_cmd)))
    status, output = commands.getstatusoutput(SCP_CMD.format(server))


def run_grep_on_all_servers():
    for server, server_name in ALL_SERVERS:
        run_grep_on_server(server)


def summarise_json_output(server):
    server_report_output = []
    logger.info('Summerising {}'.format(server))
    json_file = '/tmp/{}-feed-search.json'.format(server)
    with open(json_file, 'r') as f:
        json_output = json.loads(f.read())
        json_results = json_output['results']
        for app in json_results:
            if app['output'] and 'No such file or directory' not in app['output']:
                server_report_output.append(('{}:\n{}'.format(app['instance'], app['output'])))
            else:
                server_report_output.append(('{}: No Socket Exceptions'.format(app['instance'])))
    return '\n'.join(server_report_output)


def summarise_all_json_files():
    total_output = []
    for server, server_name in ALL_SERVERS:
        total_output.append('{}({}):'.format(server_name, server))
        total_output.append(summarise_json_output(server))
        total_output.append('')
    return total_output


def report_feed_errors(email=None):
    run_grep_on_all_servers()
    report_output = []
    date_yesterday = (dt.now() - td(days=1)).strftime('%Y-%m-%d')
    report_output.append('Report Date: {}\n'.format(date_yesterday))
    report_output.extend(summarise_all_json_files())
    print('')
    print('\n'.join(report_output))
    if email:
        send_email(email, '\n'.join(report_output), 'Feed Error Report - {}'.format(date_yesterday))


def send_email(to, body, subject):
    status, output = commands.getstatusoutput('echo {} | base64 -d | mailx -s "{}" {}'.format(base64.b64encode(body), subject, to))


def main2():
    parser = argparse.ArgumentParser()
    parser.add_argument('--email')
    args = parser.parse_args()
    report_feed_errors(args.email)


def main():
    sport=""
    host=""
    env_name=""

    sport_choice="football".capitalize()

    if sport_choice in SPORT.keys():
        sport=sport_choice
        host=SPORT['Football']['Host']
        env_name=SPORT['Football']['env_name']

        print "{} {} {}".format(sport, host, env_name)

if __name__ == '__main__':
    main()
