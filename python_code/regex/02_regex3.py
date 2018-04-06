#/usr/bin/env python

import sys
import re
import argparse

'''
<?xml version="1.0" encoding="UTF-8"?>
<Parent version="1.0">
	<Request authIdentifier="010508F3-33CF-44AC-BCA2-AD34549C321A">
	<Bacon sandwich="yummy">
	<IndexID indexType="test">
<IndexName>681910</IndexName>
<Timestamp>Mon Jan 12 13:13:22 2015</Timestamp>
	</IndexID>
</Parent>
'''

# The exercice is to extract data from certain tags and return an error if the xml is malformed.
# Here a dictionnary is used to store temporary results
parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='filename', type=str, required=True)
args = parser.parse_args(
    "-f /home/pat/Documents/python_scripts/regex/02_parse_exercice.xml".split())

inputfilename = args.filename
outputfilename = str.replace(inputfilename, '.xml', '.log')

# print outputfilename
# sys.exit()

# Marginally slower and using dictionnary to store results.
tags = {"timestamp": "", "authIdentifier": "",
        "indexType": "", "indexName": "", "sandwich": ""}

with open(inputfilename, mode="r") as fd:  # Read input file
    with open(outputfilename, "w") as fd2:  # Write results in csv outputfile
        # Initializing variables
        inParent = False  # boolean tracking the Opening Parent tag
        lineNo = 0  # line counter

        fd2.write("{}\n".format(",".join(tags.keys())))  # csv header

        for line in fd:
            lineNo += 1

            # if this is a top level tag
            if '<Parent' in line:

                # Twice in a row, return warning
                if inParent is True:
                    print "Opening parent for 2nd time, in line {}".format(
                        lineNo)
                    exit(1)
                else:
                    # Resetting variables to go to the next Parent data set
                    inParent = True
                    tags = {k: "" for k in tags.keys()}  # Empty dictionary

            # if this is a closing top level tag
            if '</Parent>' in line:
                # Twice in a row, return warning
                if inParent is False:
                    print "Error: unclosed parent at line {}".format(lineNo)
                else:
                    # Check and alert if there are any empty variables, can be a sign that the file or precessing went wrong
                    fd2.write("{}\n".format(",".join(tags.values())))

                    # Close the parent section
                    inParent = False

            # Extracting data using regex
            m = re.search(r'<(timestamp)>(.*)</\1.>*', line, re.I | re.M)
            if m:
                tags['timestamp'] = m.group(2)

            m = re.search(r'<.*authIdentifier="(.*)".*', line, re.I | re.M)
            if m:
                tags['authIdentifier'] = m.group(1)

            m = re.search(r'<.*indexType="(.*)".*', line, re.I | re.M)
            if m:
                tags['indexType'] = m.group(1)

            m = re.search(r'<(indexName)>(.*)</\1.>*', line, re.I | re.M)
            if m:
                tags['indexName'] = m.group(2)

            m = re.search(r'<.*sandwich="(.*)".*', line, re.I | re.M)
            if m:
                tags['sandwich'] = m.group(1)

print "Results in: %s" % outputfilename
