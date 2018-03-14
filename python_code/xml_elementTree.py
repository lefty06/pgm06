#!/usr/bin/python
# coding=UTF-8
import xml.etree.cElementTree as ET

# Good overall XML tutorial: https://pymotw.com/2/xml/etree/ElementTree/parse.html
# This is to OPEN XMLs
# https://docs.python.org/3.6/library/xml.etree.elementtree.html
# <data> Root name of the XML
#     <tag_name attribute_name1="attribute_value1" attribute_name2="attribute_value2">The text value</tag_name>
#     <movie name="Heat">
#         <yeah>year element text</year>
#     </movie>
# <data>

xmlfile = '/home/pat/Documents/vscode2018/python_code/simple_test.xml'
tree = ET.ElementTree(file=xmlfile)

# To fetch the root element and is necessary for the rest of the code
root = tree.getroot()

# To return the root (top) address and tree name
# print ("tree.getroot(): {}, tree.getroot().tag: {}".format(root, root.tag))

# To check whether this is the root element ie no values
# print ('{}, {}'.format(root.tag, root.attrib))

# # To display all root child nodes ie 1 level and their respective values (dictionary)
# for child_of_root in root:
#     print('tag: {}, attrib:{}, # of key per attrib:{}'.format(
#         child_of_root.tag, child_of_root.attrib, len(child_of_root.keys())))

# Not working
# print ("{} {}".format(root[0].tag, root[0].txt))

# print()
# # To navigate the entire tree i.e. all levels
# for elem in tree.iter():
#     print (elem.tag, elem.attrib)

# It will find all tag names and only return the data for it not for the child nodes/tags
# for elem in tree.iterfind('country'):
#     print ('elem.tag: {}\nelem.attrib: {}, type(elem.attrib):{}\nelem.text: {},type(elem.text): {}\n-----'.format(
#         elem.tag,
#         elem.attrib, type(elem.attrib),
#         elem.text, type(elem.text)
#     ))


# No idea what it returns?
# print ('len(root[0])={}'.format(len(root[0])))

'''
for elem in tree.findall('country'):
    print ('{}, {},{}'.format(elem.tag, elem.attrib, elem.text))
    # this one way to access tags attributes and text under country
    print ('root[0][1].tag={}, root[0].attrib= {}, root[0][1].text)= {}'.format(root[0][1].tag,
                                                                            root[0].attrib, root[0][1].text))
    # This returns the attribute value ie <tag_name attrib_name="value"....
    country_name = elem.get('name')
    # This searches and returns the first occurence
    country_year = elem.find('rank/current-rank')
    print ("{} {}".format(country_name, country_year))
'''

'''
<XML>
<person sex='Male'>
    <Name>Joe<Name>
    <child>
        <Name>JJunior<Name>
    <child>
    <country>Thaiti<country>
</person>
<person sex='Male>
    <Name>Alan<Name>
    <country>Mongolia<country>
</person>
</XML>

Element.iter() To navigate the tree, this is a generator
Element.iterfind('tagname/tagname') Returns a generator with all elements found at any level
Element.findall("person[@sex='Male']") returns 2 elements = person
Element.find("person[@sex='Male']) finds the first match and returns first level elements ie name, child
Element.get() accesses the element’s attributes
Element.findtext('tagname') Returns the FIRST sub element having text

if you use methods find or findall you count the number of elements returned
    print ("{},{}".format(
                    len(Element.find('tagname')),
                    len(Element.findall('tagname'))
            )
'''

# for country in root.findall('country'):
#     name = country.get('name')
#     rank = country.find('rank').text
#     print( name,rank)

# #To find and display all current-rank tag names, tag attributes and tag text
# for ranking in root.findall('country/rank/current-rank'):
#     tag_name=ranking.tag
#     tag_attrib=ranking.attrib
#     tag_text=ranking.text
#     print('tag_name:{}, tag_attributes:{}, tag_text:{}'.format(tag_name,tag_attrib,tag_text))

###########################################

# Example
# xmlfile2 = '/home/pat/Documents/vscode2018/python_code/RationalGroup_ALL_2018-1-21T08-52-42_2018-01-21T08-09-34.XML'
# tree2 = ET.ElementTree(file=xmlfile2)
# root2 = tree2.getroot()

# for child_of_root in root2:
#     print('tag: {}, attrib:{}, # of key per attrib:{}'.format(
#         child_of_root.tag, child_of_root.attrib, len(child_of_root.keys())))

# That will probably be the way to navigate the XML
# for elem in tree2.iter():  # To navigate the entire tree i.e. all levels
#     print (elem.tag, elem.attrib)

# The root tag doesnt count you need to search from the follow level down
# for elem in tree2.findall('Sports/Sport'):
#     print ('{}, {}, {}'.format(elem.tag, elem.attrib, type(elem.attrib)))
#     sport_id = elem.attrib
#     sport_text = elem.findall('Texts/Text/Value')
#     if sport_text == 'Soccer':
#         print ("{}, {}".format(sport_id['BetradarSportID'], sport_text))


# Example
# xmlfile2 = '/home/pat/Documents/python_code/simple_test.xml'
# tree2 = ET.ElementTree(file=xmlfile2)
# for elem in tree2.findall('data/country/rank'):
#     print ('{}, {}, {}'.format(elem.tag, elem.attrib, type(elem.attrib)))

###############################################################

def example_05():
    sxml = """
    <encspot>
    <file number="1"><Name>some filename.mp3<Subname>This is the alternate text</Subname></Name>
        <Encoder>Gogo (after 3.0)</Encoder>
        <Bitrate>131</Bitrate>
    </file>
    <file number="2"><Name>Prodigy.mp3</Name>
        <Encoder>Youtube</Encoder>
        <Bitrate>256</Bitrate>
    </file>
    <file number="1"><Name>another filename.mp3</Name>
        <Encoder>iTunes</Encoder>
        <Bitrate>128</Bitrate>
    </file>
    </encspot>
    """
    tree = ET.fromstring(sxml)

    # Given the results you need to pay close attention to what find and findall do

    print("This searches only the first matching element with attribute number=1 and returns all first level sub                elements.\nIt returns all results not an iterator, count elements: {}".format(
        len(tree.find("file[@number='1']"))))
    for el in tree.find("file[@number='1']"):
        print ("el.tag={}, e.attrib={}, el.text={}".format(
            el.tag, el.attrib, el.text))

    print ('\n-------------------\n')

    print("This searches (all levels) for all elements with attribute number=1\nIt returns all results not an iterator, count elements:{}".format(
        len(tree.findall("file[@number='1']"))))
    for el in tree.findall("file[@number='1']"):
        print ("el.tag={:>5}, e.attrib={}, el.text={}".format(
            el.tag, el.attrib, el.text))

    print ('\n-------------------\n')

    print "\nAn alternate way:"
    # using xpath This searches at all levels even sub level tags have the same name
    el = tree.findall('.//Subname')
    print ("type:{}, count result:{}, {}".format(type(el), len(el), el))

    print ('\n-------------------\n')

    # To generate a tuples list with a comprehensive expression which all first level tags under file tag
    tuple_of_tag_text = [(ch.tag, ch.text)
                         for e in tree.findall('file') for ch in e.getchildren()]

    print("The list:{}\ne.g.:list elem #2, 2nd elem in tuple: {}".format(tuple_of_tag_text,
                                                                         tuple_of_tag_text[1][1]))


def example_06():
    # Using a generator, this will navigate the entire tree
    xmlfile2 = '/home/pat/Documents/vscode2018/python_code/simple_test.xml'
    tree2 = ET.ElementTree(file=xmlfile2)
    for elem in tree.iter():
        print ("tagname:{},attrib:{},text:'{}'".format(
            elem.tag, elem.attrib, elem.text))


def example_07():
    '''
    The below navigates the XML for all Soccer then Premier league match info
    Category(sport) > Tournament > Match
    When listing all categories the result returned is an iterable elem object which can be searched
    You can nest iterfinds which list all child tags FIRST level only
    '''
    xmlfile2 = '/home/pat/Documents/vscode2018/python_code/simple_test.xml'
    xmlfile2 = '/home/pat/Documents/vscode2018/python_code/RationalGroup_ALL_2018-1-21T08-52-42_2018-01-21T08-09-34.XML'
    tree2 = ET.ElementTree(file=xmlfile2)

    '''
    Category(sport)
        Texts
            Text
        Tournament(competition)
            Texts
                Text
            Match(event)
                Texts
                    text
    '''
    sport = tree2.find('.//Sport[@BetradarSportID="1"]')
    if sport:
        print("{}\n".format(len(sport)))
    sport2 = tree2.find(
        './/Sport[@BetradarSportID="1"]/Texts/Text[@Language="en"]')  # Returns the first element matching
    # tree2.findtext('.//Sport[@BetradarSportID="1"]/Texts/Text[@Language="en"]/Value') #Returns a string

    if sport2:
        print("sport="+sport2.find('Value').text)
        # for n in sport2.iter():
        #     print(n.tag, n.attrib, n.text)
        # print('++++++++++++')

    else:
        print('nada')

    # It will find all tag names and only return the data for it not for the child nodes/tags
    # for cat in tree2.iterfind('Sports/Sport/Category'):
    #     BetradarCategoryID = cat.attrib['BetradarCategoryID']
    #     # Cat=1 Soccer

    #     # cname = get_text(cat, 'BET')
    #     if BetradarCategoryID == '1':
    #         # Listing all tournament IDs

    #         for tournament in cat.iterfind('Tournament'):

    #             # Get tournament ID, TourId=1 Premier league
    #             BetradarTournamentID = tournament.attrib['BetradarTournamentID']

    #             tname = get_text(tournament, 'BET')
    #             if BetradarTournamentID == "1":

    #                 # Get tournament name
    #                 # for t_text in tournament.iterfind('Texts/Text'):
    #                 #     # print("{}, {}".format(t_text.tag, t_text.attrib))
    #                 #     if t_text.attrib['Language'] == 'en':
    #                 #         print("{}, {}".format(
    #                 #             count(t_text.items()), t_text[0].text))
    #                 # print ('cname:'+cname)
    #                 print ('tname:'+tname)

    #                 # List all match IDs
    #                 # for Match in tournament.iterfind('Match'):
    #                 #     print ('Match.tag: {}\n Match.attrib: {},\n Match(Match.attrib):{}\n Match.text: "{}"\n type(Match.text): {}\n-----'.format(
    #                 #         Match.tag,
    #                 #         Match.attrib, type(Match.attrib),
    #                 #         Match.text, type(Match.text)
    #                 #     ))


def get_text(elem, language):
    '''
    texts can contain several tags called <text> which have 1 attrib and no text
    text tags can contain only one tag called <value> which have no attrib and text value
    tagname
        texts
            text1
                value
            text2
                value
    '''

    restext = ""
    for lang in elem.findall('Texts/Text'):
        # print('{},{},{}'.format(lang.tag, lang.attrib, lang.text))
        if lang.attrib['Language'] == language:
            return (lang[0].text)
            # for t in lang.findall('Value'):
            #     # print('\t{},{},{}\n'.format(t.tag, t.attrib, t.text))
            #     return t.text
    return restext


def main():
    example_07()


if __name__ == "__main__":
    main()
