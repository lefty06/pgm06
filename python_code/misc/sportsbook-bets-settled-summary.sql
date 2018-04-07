SET work_mem = '4GB';
COPY (

  SELECT  b.status
         ,b.bet_type
         ,b.free_bet
         ,case when b.setl_type_id = 0 then 'Resulting'
               when b.setl_type_id = 1 then 'Cashout'
               when b.setl_type_id = 2 then 'Manual'
               else b.setl_type_id::text end          AS cashout
         ,upper('${source_currency}')                 AS currency
         ,sum (b.bonus_stake)                         AS bonus_stake
         ,ROUND(SUM(payout * (1 / e.rate)),2)         AS total_payout
         ,ROUND(SUM(b.total_stake * (1 / e.rate)),2)  AS total_stake
         ,COUNT(*)
     FROM bets b
     LEFT JOIN exchange_rate e ON LOWER(b.currency) = e.currency2 and e.date::date = placed_time::date and currency1 = lower('${source_currency}')

     WHERE b.settlement_time BETWEEN '${startdate}'::timestamp and '${enddate}'::timestamp
     AND   b.bet_type    in ('SINGLE','MULTIPLE')
     AND   b.acco_id not in (${exclude_acco_ids})

     GROUP BY 1,2,3,4,5
     ORDER BY 1,2,3,4

) to stdout csv header;
