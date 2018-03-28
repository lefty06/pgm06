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

    print('\n-------------------\n')

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
    for elem in tree2.iter():
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

    # show_tree(tree2, what='Competition')
    show_matches(tree2, 21, 105, 7664)


def show_matches(etree, sport=None, country=None, competition=None):
    '''
    '''
    mid = ""
    mdate = ""
    cid = ""
    cname = ""
    res = ""
    path = ""
    count_match = 0

    if sport and country and competition:
        path = ".//Sport[@BetradarSportID=\"" + str(sport) \
            + "\"]/Category[@BetradarCategoryID=\"" + \
            str(country) + \
            "\"]/Tournament[@BetradarTournamentID=\"" + \
            str(competition) + "\"]/Match"
    elif sport and country:
        path = ".//Sport[@BetradarSportID=\"" + \
            str(sport) + "\"]/Category[@BetradarCategoryID=\"" + \
            str(country)+"\"]/Tournament/Match"
    elif sport:
        path = ".//Sport[@BetradarSportID=\"" + \
            str(sport) + "\"]/Category/Tournament/Match"
    else:
        pass

    print('Arguments:\n\tBetradarSportID={} (Sport)\n\t\t|_BetradarCategoryID={} (Country)\n\t\t\t|_BetradarTournamentID={} (Competition)\n'.format(
        sport, country, competition))
    for m in etree.iterfind(path):
        mid = m.attrib['BetradarMatchID']
        res = mid
        count_match += 1

        for m2 in m.findall('.//Fixture/Competitors/Texts'):
            for m3 in m2.iter():
                if any('SUPERID' in s for s in m3.attrib.keys()):
                    cid = m3.attrib["SUPERID"]
                    res = res+", ("+cid+")"
                if any('Language' in s for s in m3.attrib.keys()):
                    if m3.attrib['Language'] == 'en':
                        cname = m3.findtext('.//Value')
                        res = res+cname
        mdate = m.findtext('.//DateInfo/MatchDate')
        res = res+", "+mdate
        print res
        res = ""

    if count_match == 0:
        print('No Matches/Events Found\n')
        print("ElemTree Path="+path)
    else:
        print('\nMatch Count:' + str(count_match))


def show_tree(elem, what='Sport'):
    '''
        This will display the Betradar XML up to three levels down(Sport > Category > Tournament))
    '''
    user_choice = ['Sport', 'Country', 'Competition']
    sport = ""
    sport_id = ""
    category = ""
    category_id = ""
    tournament = ""
    tournament_id = ""

    if type(elem).__name__ in ('ElementTree'):

        if what in user_choice:
            # Find all sports
            for sp in elem.iterfind('.//Sport'):
                sport = sp.findtext('.//Texts/Text[@Language="en"]/Value')
                sport_id = sp.attrib.values()[0]
                if what in user_choice[0]:
                    print("{}={}".format(sport, sport_id))

                # Only if user wants to see L2 and L3 the below is executed
                if what in user_choice[1:]:
                    # Find all sports and category (country)
                    for c in sp.iterfind('.//Category'):
                        category = c.findtext(
                            './/Texts/Text[@Language="en"]/Value')
                        category_id = c.attrib.values()[0]
                        if what in user_choice[1]:
                            print(" {}={}, {}={}".format(sport, sport_id,
                                                         category, category_id))

                        # Only if user wants to see L3 the below is executed
                        if what in user_choice[2]:
                            # Find all sports and category (country) and tournament (competition)
                            for t in c.iterfind('.//Tournament'):
                                tournament = t.findtext(
                                    './/Texts/Text[@Language="en"]/Value')
                                tournament_id = t.attrib.values()[0]
                                print(" {}={}, {}={}, {}={}".format(sport, sport_id,
                                                                    category, category_id, tournament, tournament_id))
        else:
            print('Wrong Choice "{}", choose from :{}'.format(what, user_choice))
    else:
        print("{} is not an element but it a {}".format(elem, type(elem)))
        if type(e).__name__ == 'list':
            for n in elem:
                for n2 in n.iter():
                    print("tag:{}, attributes:{}, text:{}".format(
                        n2.tag, n2.attrib, n2.text))


def show_text(e):
    res = {}
    if type(e).__name__ == 'Element':
        if e.tag in ('Sport', 'Category', 'Tournament'):
            en_text = e.findtext('Texts/Text[@Language="en"]/Value')
            id_attrib = e.attrib.values()[0]
            print("{},{},{}".format(id_attrib, e.tag, en_text))
            res[en_text] = id_attrib

    return res


def main():
    example_07()


if __name__ == "__main__":
    main()
