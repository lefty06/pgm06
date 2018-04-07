#!/usr/bin/env python
import argparse
import subprocess

SQL_event_iseachway = """with event_bets as (
select bet_id from bet_parts where node_id in ( {0} )
),
all_bets as (
select *
from bets
where (bets_id in (select id from event_bets))
or (id in (select id from event_bets) and  bet_type in ('SINGLE','MULTIPLE'))
),
all_eachway as(
select distinct bet_id,'YES' iseachway
from bet_parts
where win_type in ('PLACE')
and bet_id in (select id from all_bets)
)
select b.id,b.bets_id,b.bet_type,b.placed_Time,bp.part_no,b.acco_id,b.account_ref,bp.event,bp.market,bp.win_type,bp.selection,bp.price,bp.stake, e.iseachway
from all_bets b join bet_parts bp on b.id=bp.bet_id left join all_eachway e on b.id=e.bet_id
where bp.node_id in ( {0} )
order by bp.event,b.id,bp.part_no;
"""

SQL_bets_iseachway = """with all_bets as (
select *
from bets
where (bets_id in ({0}))
or (id in ({0}) and  bet_type in ('SINGLE','MULTIPLE'))
),
all_eachway as(
select distinct bet_id,'YES' iseachway
from bet_parts
where win_type in ('PLACE')
and bet_id in (select id from all_bets)
)
select b.id,b.bets_id,b.bet_type,b.placed_Time,bp.part_no,b.acco_id,b.account_ref,bp.event,bp.market,bp.win_type,bp.selection,bp.price,bp.stake, e.iseachway
from all_bets b join bet_parts bp on b.id=bp.bet_id left join all_eachway e on b.id=e.bet_id
order by bp.event,b.id,bp.part_no;
"""

def search_iseachway_bets(sql,idlist):
    CMD='echo "{0}"|psql ats_pokerstarsbetcatch '.format(sql.format(idlist))
    return CMD

def exec_command(CMD):
    str_subprocess_out=subprocess.Popen(CMD, stdout=subprocess.PIPE, shell=True).communicate()
    print str_subprocess_out[0]

def main():

    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-b','--betlist',help='List of bets IDs comma separated')
    group.add_argument('-n','--nodes',help='List of event IDs comma separated')

    args = parser.parse_args()

    if args.betlist:
        CMD=search_iseachway_bets(SQL_bets_iseachway,args.betlist)
        print '{0}'.format(CMD)
        # exec_command(CMD)
    if args.nodes:
        CMD=search_iseachway_bets(SQL_event_iseachway,args.nodes)
        print '{0}'.format(CMD)
        # exec_command(CMD)

    print 'args:{}'.format(args) #Displays everything, good for debugging

if __name__ == '__main__':
    main()
