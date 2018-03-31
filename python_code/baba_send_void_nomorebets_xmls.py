#!/usr/bin/python
import argparse
import logging
import time
import re
import os
import subprocess as s
import sys


log_level = 10  # TRACE
logger_format = "%(asctime)s %(levelname)s [ %(funcName)s ] %(message)s"
logging.basicConfig(format=logger_format, level=log_level)


def xml_output(msgtype, drawid):
    '''
        To generate two type of xml messages i.e. Void or NoMoreBets for a given Draw Id

        args:
            msgtype: [Void|NoMorebets]
            drawid: [Int|String]
        return:
            string
    '''
    if msgtype in ('NoMoreBets', 'Void'):
        s = """<?xml version="1.0" ?>
<message MessageType="{}" MessageDateTime="2017-03-15T12:00:00-00:00" MessageFormatVersion="1.0" ControllerId="1" TransactionId="2">
<event EventId="{}" EventType="5" EventTime="2016-03-15T12:00:00Z" EventGUID="3858947E-3DBB-4F10-927B-6BD29B8A5253"/>
</message>
""".format(msgtype, drawid)
        return s
    else:
        return None


def write_xml(filename, xml_msg, dryrun=False):
    '''
        To write string into a file

        args:
            filename: output filename
            xml_msg: string

    '''
    if xml_msg and filename:
        if dryrun:
            logging.debug(
                "Writing the below message in {}\n{}".format(filename, xml_msg))
        else:
            logging.info(
                "Writing message in {}".format(filename))
            with open(filename, 'w') as f:
                f.write(xml_msg)


def execute_command(filename, dryrun=False):
    '''
        Checks if the file exists and then tries to curl it to an hard coded URL

        args:
            filename: file to send
    '''
    url = "http://ngpambiltrs01:18080/rgs/b2b/game/rushkeno/feed/"
    cmd = "curl -v -X POST -H \"Accept:application/xml\" -H \"Content-Type:application/xml\" -d@{} {}".format(
        filename, url)
    if dryrun:
        # print("Sending message:\n{}\n".format(cmd))
        logging.debug("Sending message:\n{}\n".format(cmd))
    else:
        if not os.path.isfile(filename):
            logging.debug(
                "file '{}' does not exist, exiting script".format(filename))
            exit(1)
        logging.info("Sending file {} to {}".format(filename, url))
        doit = s.Popen(cmd, shell=True,
                       stdout=s.PIPE, stderr=s.PIPE)
        (stdout, stderr) = doit.communicate()
        # print("stdout:{}\nstderr:{}".format(
        # repr(stdout), stderr))
        if stderr:
            logging.error(
                "There was an error curling the message\n{}".format(stderr))

        # body = 'eventId,eventCode;' + result
        # query_args = { 'sessionToken':'blah', 'tvo':'true' ,'attributes': body}
        # request = urllib2.Request(args.attrAPI)

        # request.add_data(urllib.urlencode(query_args))
        # response = urllib2.urlopen(request).read()
        # if 'error' in response.lower():
        #     log.error (response)


def main():
    dirname = ""
    filename = ""
    draw_list = ""
    draw_id = ""
    dry_run = ""
    msgtype = ""

    parser = argparse.ArgumentParser(
        description='To curl and xml with void or nomorebets to the BABA end point')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--void', action='store', dest='Voidlist',
                       help='The draw list can be comma,space,semi colon delimited')
    group.add_argument('--nomorebets', action='store', dest='NoMoreBetslist',
                       help='The draw list can be comma,space,semi colon delimited')

    parser.add_argument('--dry-run', action='store_true', dest='boolean_switch',
                        default=False, help='Show details without executing')

    # a = ['--nomorebets', '123, 456;589', '--dry-run']
    #a = ['--void', '123']
    if len(sys.argv) <= 1:
        args = parser.parse_args(['-h'])

    args = parser.parse_args()
    if args.boolean_switch:
        dry_run = args.boolean_switch

    if args.Voidlist:
        draw_list = re.split(" |,|;", args.Voidlist)
        msgtype = 'Void'
        filename = msgtype + '.xml'

    if args.NoMoreBetslist:
        draw_list = re.split(" |,|;", args.NoMoreBetslist)
        msgtype = 'NoMoreBets'
        filename = msgtype + '.xml'

    if draw_list:
        logging.info("Draw list total: {}".format(len(draw_list)))
        for draw_id in draw_list:
            logging.info("Handling draw_id={}".format(draw_id))
            msg = xml_output(msgtype, draw_id)
            write_xml(filename, msg, dry_run)
            execute_command(filename, dry_run)
            if not dry_run:
                time.sleep(0.2)


if __name__ == '__main__':
    main()
