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
# Here variables are used to store temporary results
parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='filename', type=str, required=True)
args = parser.parse_args(
    "-f /home/pat/Documents/python_scripts/regex/02_parse_exercice.xml".split())

inputfilename = args.filename
outputfilename = str.replace(inputfilename, '.xml', '.log')

# sys.exit()

with open(inputfilename, mode="r") as fd:  # Read input file
    with open(outputfilename, "w") as fd2:  # Write results in csv outputfile

        # Initializing variables
        inParent = False  # boolean tracking the Opening Parent tag
        lineNo = 0  # line counter
        timestamp, authIdentifier, indexType, indexName, sandwich = None, None, None, None, None
        # csv header
        fd2.write("timestamp,authIdentifier,indexType,indexName,sandwich\n")

        for line in fd:
            lineNo += 1

            # if this is a top level tag
            if '<Parent' in line:

                # Twice in a row, return warning
                if inParent is True:
                    print "Opening parent for 2nd time, in line %s" % lineNo
                    exit(1)
                else:
                    # Resetting variables to go to the next Parent data set
                    inParent = True
                    timestamp, authIdentifier, indexType, indexName, sandwich = None, None, None, None, None

            # if this is a closing top level tag
            if '</Parent>' in line:
                # Twice in a row, return warning
                if inParent is False:
                    print "Error: unclosed parent at line %s" % lineNo
                else:
                    # Check and alert if there are any empty variables, can be a sign that the file or precessing went wrong
                    fd2.write("%s,%s,%s,%s,%s\n" % (
                        timestamp, authIdentifier, indexType, indexName, sandwich))

                    # Close the parent section
                    inParent = False

            # Extracting data using regex
            m = re.search(r'<Timestamp>(.*)</Timestamp>', line)
            if m:
                timestamp = m.group(1)

            m = re.search(r'authIdentifier="(.*)"', line)
            if m:
                authIdentifier = m.group(1)

            m = re.search(r'indexType="(.*)"', line)
            if m:
                indexType = m.group(1)

            m = re.search(r'<IndexName>(.*)<', line)
            if m:
                indexName = m.group(1)

            m = re.search(r'sandwich="(.*)"', line)
            if m:
                sandwich = m.group(1)

print "Results in: %s" % outputfilename
