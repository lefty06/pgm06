#!/usr/bin/python
from bs4 import BeautifulSoup


'''
This is not a Python standard lib, it needs to be installed
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#parsing-only-part-of-a-document
'''


def example_01():
    # xmlfile2='/home/pat/.PyCharmCE2017.3/config/scratches/RationalGroup_ALL_2018-1-21T08-52-42_2018-01-21T08-09-34.XML'
    xmlfile2 = '/home/pat/.PyCharmCE2017.3/config/scratches/simple_test.xml'
    infile = open(xmlfile2, "r")
    contents = infile.read().decode('utf-8', 'ignore')
    # soup = BeautifulSoup(contents,'xml')
    soup = BeautifulSoup(contents, 'xml')
    titles = soup.find_all('country')

    # for title in soup.find_all('country'):
    for title in soup.find_all(['country', 'year']):
        print("{}".format(title.get_text()))
        print("{}".format(type(title.get_text())))


def example_02():
    '''
    it much longer to init than element API but more intuite to navigate the xml tree
    '''
    xmlfile2 = '/home/pat/Documents/python_code/simple_test.xml'
    infile = open(xmlfile2, "r")
    contents = infile.read().decode('utf-8', 'ignore')
    soup = BeautifulSoup(contents, 'xml')

    country = soup.find('country', {'name': 'Liechtenstein'})

    children = country.findChildren()

    for child in children:
        print child


def example_03():
    '''
    it much longer to init than element API but more intuite to navigate the xml tree
    '''

    xmlfile2 = '/home/pat/Documents/python_code/simple_test.xml'
    xmlfile2 = '/home/pat/.PyCharmCE2017.3/config/scratches/RationalGroup_ALL_2018-1-21T08-52-42_2018-01-21T08-09-34.XML'
    infile = open(xmlfile2, "r")
    contents = infile.read().decode('utf-8', 'ignore')
    soup = BeautifulSoup(contents, 'xml')

    country = soup.findAll('Sport', 'BetradarSportID')

    for c in country:
        print c

    # country = soup.find('Sport', {'BetradarSportID': '1'})

    # children = country.findChildren()
    # for child in children:
    #     # if child == 'BetradarTournamentID'
    #     print child


def example_04():
    '''
    In this example, we will try and find a link (a tag) in a webpage
    We will use the soup.findAll method to search through the soup object to match fortext and html tags within the page.
    That will print out all the elements in python.org with an "a" tag.
    (The "a" tag defines a hyperlink, which is used to link from one page to another.)
    '''
    from BeautifulSoup import BeautifulSoup
    import urllib2

    url = urllib2.urlopen("http://www.python.org")
    content = url.read()
    soup = BeautifulSoup(content)
    links = soup.findAll("a")


def example_05():
    '''
    In this example, we will try and find a link (a tag) in a webpage
    We will use the soup.findAll method to search through the soup object to match fortext and html tags within the page.
    That will print out all the elements in python.org with an "a" tag and we can specify the URL's we want to return. 
    (The "a" tag defines a hyperlink, which is used to link from one page to another.)
        <a>title="blablal" href="https://blabla.com"</a>
    (The img tag defines an image and its attribute being called src)
        <img>class="image-size-full" src="https://blabla.jpg"</img>
    '''

    from BeautifulSoup import BeautifulSoup
    import urllib2
    import re

    url = urllib2.urlopen(
        "https://www.boredpanda.com/funny-fortune-cookie-messages/?page_numb=1")
    content = url.read()
    soup = BeautifulSoup(content)
    for img in soup.findAll('img', src=True):
        if re.findall('funny.*fortune.*jpg', img['src']):
            print "Found the image URL:", img['src']


def main():
    example_05()


if __name__ == '__main__':
    main()
