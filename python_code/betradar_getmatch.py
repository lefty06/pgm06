#!/usr/bin/python
# coding=UTF-8
import xml.etree.cElementTree as ET
import argparse


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


def main():

    xmlfile = '/home/pat/Documents/vscode2018/python_code/RationalGroup_ALL_2018-1-21T08-52-42_2018-01-21T08-09-34.XML'
    tree = ET.ElementTree(file=xmlfile)

    parser = argparse.ArgumentParser(
        description='Get bets from a list of IDs or a file with IDs')

    # you can create as many groups as needed
    # cant use -l and -s at the same time
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-l', '--list', action='store', dest='show_tree',
                       choices=['Sport', 'Country', 'Competition'], help='this is it')
    group.add_argument('-s', '--search', dest='ids', nargs='+',
                       help='uma lista de INTs caralho')

    #-f is mandatory
    parser.add_argument('-f', '--file', type=argparse.FileType('r'),
                        dest='fname', help='Absolute path to the Betradar XML', required=True)

    #  Cricket = 21, International = 105, U19 World Cup, Group A = 7664
    # args = parser.parse_args(['-f', xmlfile, '-s', '21', '105', '7664'])
    args = parser.parse_args()
    if args.show_tree:
        show_tree(tree, args.show_tree)
    if args.ids:
        # Need to sort this shit out, its messy or change the function parameters
        show_matches(tree, args.ids[0], args.ids[1])


if __name__ == '__main__':
    main()