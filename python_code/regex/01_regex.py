#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import re
import os

# 6/10 http://www.python-course.eu/re.php
# 6/10 http://www.tutorialspoint.com/python/python_reg_expressions.htm
# 6/10 http://apprendre-python.com/page-expressions-regulieres-regular-python
# 4/10 https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
# 8/10 https://docs.python.org/3/library/re.html#search-vs-match

"""
IMPORTANT: Unless an 'r' or 'R' prefix is present, escape sequences in string and bytes literals are interpreted according to rules similar to those used by Standard C.
re.sub(r'\t','[TAB]','this is my\tblabla text'), re.sub(r'\t','[TAB]',r'this is my\tblabla text') #Anything preceeded by r or R special escape characters will not be interpreted e.g.: \t

MATCH checks for a match only at the beginning of the string, while SEARCH checks for a match anywhere in the string
SEARCH WILL only search for one match in the string and return a group object
findall uses search to find all occurences of the pattern in the string and return all results in a list
finditer uses search to find all occurences of the pattern in the string and return a generator

echo "blo\nbli\nbla and bla \nbla" | grep -r "bla" , search cant find bla because it is in line 3
echo "blo\nbli\nbla and bla \nbla" | grep -r "bla" , search and re.M finds and returns the last bla
echo "blo\nbli\nbla and bla \nbla" | grep -r "bla" , findall and re.M finds all occurences on all lines
echo "blo\nbli\nbla and bla \nbla" | grep -r "bla" , finditer and re.M finds all occurences on all lines

re.L	Interprets words according to the current locale. This interpretation affects the alphabetic group (\w and \W), as well as word boundary behavior (\b and \B).
re.M	Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).
re.I Makes the search case insensitive
re.S	Makes a period (dot) match any character, including a newline.
re.U	Interprets letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B.
re.X	Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker.
"""

phone_list = """Allison Neu 555-8396
Bob Newhall 555-4344
C. Montgomery Burns 555-0001
C. Montgomery Burns 555-0113
Canine College 555-7201
Canine Therapy Institute 555-2849
Cathy Neu 555-2362
City of New York Parking Violation Bureau 555-BOOT
Dr. Julius Hibbert 555-3642
Dr. Nick Riviera 555-NICK
Earn Cash For Your Teeth 555-6312
Family Therapy Center 555-HUGS
Homer Jay Simpson (Plow King episode) 555-3223
Homer Jay Simpson (work) 555-7334
Jack Neu 555-7666
Jeb Neu 555-5543
Jennifer Neu 555-3652
Ken Neu 555-8752
Lionel Putz 555-5299
MAD Magazine 555-8628
Marital Street Hotline 555-1680
Marvin Monroe 555-3700
Marvin Monroe's radio therapy show 555-PAIN
Moe Szyslak (phone number spells SMITHERS) 7648-4377
Moe Szyslak 555-0000
Moe's Tavern 555-1239
Mr. Plow 555-3226
NY Metro 555-5680
Ned Flanders 555-8904
New York Parking Violation Bureau 555-2668
ORB 	Dr Nick's "B"argain Medical Services 1-800-DOCT
Original Famous Ray's Pizza 555-PIZA
Otto's "How's my Driving" 555-8821
Plow King 555-4796
Pretzel Wagon 555-3226
Prof John Frink's Lab 555-5782
Radio Psychaiatrist 555-7246
Reverend Timothy Lovejoy 555-6542
Richard Nash 555-9996
Richard Newhall 555-9973
Ruff-form Dog School 555-0078
Santitarium for Dogs 555-9716
Sleep-Eazy Motel 555-1000
Sugar Truck 555-3872
Susan Newhall 555-2362
The Nuclear Powerplant 5554-52467
The Simpsons' residence 5555-87077
The Simpsons, 742 Evergreen Terrace 555-01133
Toby Muntz 555-9972
"""

# EXAMPLE 1

# To turn the above string into a list
list_phones = phone_list.split('\n')


def search_string(string_pattern, string_search=None, string_list=None, file_name=None):
    '''This function searches in either a string, a list or a file and returns a list of results.
    args:
        string_pattern: String to search
        string_search: String to search into
        string_list: List to search into
        file_name: file to search into [file name|absolute file name]

    return:
        sresults: List of results

    Import Note: Major downside is that you need to use names parameters for clarity .e.g: search_string('blabla'file_name='ats.log')
    '''

    sresults = []

    if string_search:
        res = re.search(string_pattern, string_search, re.M | re.I)
        sresults.append(res.group())
        return sresults

    if string_list:
        for line in string_list:
            res = re.search(string_pattern, str(line), re.M | re.I)
            if res:
                sresults.append(res.group())
        return sresults

    if file_name:
        if os.path.isfile(file_name):
            with open(file_name, "r") as plist:
                for line in plist:
                    res = re.search(string_pattern, line, re.M | re.I)
                    if res:
                        # print res.group()
                        sresults.append(res.group())

                return sresults
        else:
            print('This file does not exist')
            return sresults


def example2():
    res = re.search(r"Python\.$", "I like Python.")
    if res:
        print("\ntype: {}, results: {}".format(
            type(res), res.group()))

    # Search the starting position of the first occurence found
    res = re.search(
        "Python", "I like Python but sometimes hate Python.").start()
    print("\ntype: {}, Starting position: {}".format(type(res), res))

    # Search the finishing position of the first occurence found
    res = re.search(r"Python\.$", "I like Python.").end()
    print("\ntype: {}, Finishing position: {}".format(type(res), res))

    res = re.search(r"Python\.$", "I like Python.").span()
    if res:
        print("\ntype: {}, Starting and Ending position: {}".format(type(res), res))

    res = re.search(
        r".*Python.*", "I like Python.\nSome prefer Java or Perl....and Python.")
    if res:
        print("\ntype: {}, res: {}".format(type(res), res.group()))

    # This is to demonstrate re.M or r.MULTILINE.
    # Search for first occurence of Python ignoring line breaks
    res = re.search(
        r"Python.*", "I like Perl.\nSome prefer Java or Python.", re.M)
    if res:
        print ("\ntype: {}, res: {}".format(type(res), res.group()))

    string_ladies = "Anabelle ana catarina melodie Ana"

    # Search any name=ana
    res = re.search("ana", string_ladies, re.I)
    if res:
        print ("\ntype: {}, res: {}".format(type(res), res.group()))

    # Search any name starting by ana
    res = re.search("ana[a-z]*", string_ladies, re.I)
    if res:
        print ("\ntype: {}, res: {}".format(type(res), res.group()))

    # Search all names starting by ana (list)
    res = re.findall("ana[a-z]*", string_ladies, re.I)
    if res:
        print ("\ntype: {}, res: {}".format(type(res), res))

    # Search all names starting by ana (generator)
    res = re.finditer("ana[a-z]*", string_ladies, re.I)
    print ("\ntype: {}".format(type(res)))
    if res:
        a = [i.group() for i in res]
        print ("\ntype: {}, res: {}".format(type(a), a))

    # Search for the starting and ending position of all ocurrences of names starting by ana in the string
    res = re.finditer(r"ana[a-z]*", string_ladies, re.I)
    if res:
        indices = [m.span() for m in res]
        print ("\ntype: {}, res: {}".format(type(indices), indices))


def example3():
    # To extract tag name and it's value
    fname = '/home/pat/Documents/vscode2018/python_code/ice-checks/python_scripts/regex/01_tags.xml'
    with open(fname, "r") as plist:
        for i in plist:
            # #To display all tag names and their text
            # res = re.search(r"<([a-z]+)>(.*)</\1>",i,re.I|re.M)
            # if res:
                # print("tag name: {}, text: {}".format(res.group(1),res.group(2)))

            res = re.search(r"<(comment)>(.*)</\1>", i, re.I | re.M)
            if res:
                print("tag name: {}, text: {}".format(
                    res.group(1), res.group(2)))


def example4():

    l = ["555-8396 Neu, Allison",
         "Burns, C. Montgomery",
         "555-5299 Putz, Lionel",
         "555-7334 Simpson, Homer Jay"]

    print("Original List:\n{} \n\nResults:".format("\n".join(l)))

    for i in l:
        # To display the list Surname, Name, Phone number
        res = re.search(r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)", i)
        print("{}, {}, {}".format(res.group(3), res.group(2), res.group(1)))


def example5():
    # Display only the name of the largest cities in Germany (file1) and their post code(file2)
    # This is very clever because no duplicates will be added due to how dictionnary works ie keys are unique
    PLZ = {}
    fname = "/home/pat/Documents/vscode2018/python_code/ice-checks/python_scripts/regex/01_post_codes_germany.txt"
    with open(fname) as fh_post_codes:
        for line in fh_post_codes:
            # Takes , as delimiter and returns a list with 3 valuies (0,1,2)
            (post_code, city, rest_unused) = line.split(",", 2)
            PLZ[city.strip("\"")] = post_code  # Removes all " characters"

    # Printing list of cities ordered by name
    for k, v in sorted(PLZ.iteritems(), key=lambda (k, v): (k, v)):
        print "{}:{}".format(k, v)

    # Test to search for a city name and return None if Not
    search_city = "ZweibrAcken"
    if PLZ.get(search_city, None):
        print("\ncity: {}, post code: {}".format(
            search_city, PLZ[search_city]))

    # Test to print the second value in the dictionary bearing in mind the dic is not necessarily sorted
    print("Second key in the dictionnary and its value {}:{}".format(
        PLZ.keys()[2], PLZ[PLZ.keys()[2]]))


def example6():
    PLZ = {}
    fname = "/home/pat/Documents/vscode2018/python_code/ice-checks/python_scripts/regex/01_post_codes_germany.txt"
    with open(fname) as fh_post_codes:
        for line in fh_post_codes:
            # Takes , as delimiter and returns a list with 3 valuies (0,1,2)
            (post_code, city, rest_unused) = line.split(",", 2)
            PLZ[city.strip("\"")] = post_code  # Removes all " characters"

    # Create a dic with city:post_code from 01_post_codes_germany.txt
    # Loop through 01_largest_cities_germany.tx and extract the city name and search for its post code in the dictionnary
    # My version works too
    fname = "/home/pat/Documents/vscode2018/python_code/ice-checks/python_scripts/regex/01_largest_cities_germany.txt"
    with open(fname) as fh_largest_cities:
        print 'city:post_code'
        for line in fh_largest_cities:
            res = re.search(r'^[0-9]{1,2}\.\s+([a-z]+)\s+[0-9].*', line, re.I)
            if res:
                print '{}:{}'.format(res.group(1), PLZ[res.group(1)])
            break

    # Org solution
    fname = "/home/pat/Documents/vscode2018/python_code/ice-checks/python_scripts/regex/01_largest_cities_germany.txt"
    with open(fname) as fh_largest_cities:
        print 'city:post_code'
        for line in fh_largest_cities:
            re_obj = re.search(
                r"^[0-9]{1,2}\.\s+([\wÃ„Ã–ÃœÃ¤Ã¶Ã¼ÃŸ\s]+\w)\s+[0-9]", line)
            city = re_obj.group(1)
            print city, PLZ[city]
            break


def test_search_string():
    """
    Execute to test function search_string
    """

    # Search in file
    print ('\nSearch in file:')
    res = search_string(
        '.*Simpson.*', file_name='/home/pat/Documents/vscode2018/python_code/ice-checks/python_scripts/regex/01_phone_list.txt')
    print "Results: {}\n{}\n".format(len(res), ", ".join(res))

    # Search in string
    print('\nSearch in string:')
    str_test = "The sims was an terrible game...."
    res = search_string('.*sim.*', string_search=str_test)
    print "Results: {}\n{}\n".format(len(res), ", ".join(res))

    # Search in list of values
    print('\nSearch in list of values:')
    res = search_string('.*o.*', string_list=['one two three', 1, 2, 'Hello'])
    print "Results: {}\n{}\n".format(len(res), ", ".join(res))

    # To search for any line starting with s
    print('\nTo search for any line starting with s:')
    res = search_string(r'^s.*', string_list=list_phones)
    print "Results: {}\n{}\n".format(len(res), ", ".join(res))

    # Search all lines containing neu and return anything that preceeds it
    print('\nSearch all lines containing neu and return anything that preceeds it:')
    res = search_string(r'j.*neu', string_list=list_phones)
    print "Results: {}\n{}\n".format(len(res), ", ".join(res))

    # Seach all and return all lines with a number starting with 1 or 2 and preceeded with -
    print('\nSeach all and return all lines with a number starting with 1 or 2 and preceeded with -:')
    res = search_string(r'.*-([1-2]+).*', string_list=list_phones)
    print "Results: {}\n{}\n".format(len(res), ", ".join(res))

    # Seach for two  4 digit numbers at least and separated by -
    print('\nSeach for two  4 digit numbers at least and separated by -:')
    res = search_string(r'([0-9]{4,})-([0-9]{4,})', string_list=list_phones)
    print "Results: {}\n{}\n".format(len(res), ", ".join(res))


def main():
    # test_search_string()
    example6()


if __name__ == '__main__':
    main()
