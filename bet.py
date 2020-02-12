'''
Created on 26/ago/2015

@author: crisimo
'''
import utils

username='sruffinoit'
password=''

if __name__ == '__main__':
    
    token = utils.bf_login(username=username, password=password)
    
    # status = utils.bf_keepalive(token)
    
    # status = utils.bf_logout(token)
        
    # all events types
    status = utils.bf_do('listEventTypes', token=token)
    
    #list competitions- soccer only
    status = utils.bf_do('listCompetitions', token=token, params={"filter": {"eventTypeIds": ["1"]}})
    
    #list competitions which have live events
    status = utils.bf_do('listCompetitions', token=token, params={"filter": {"inPlayOnly": True}})

    #list competitions which have live events and are Soccer
    status = utils.bf_do('listCompetitions', token=token, params={"filter": {"inPlayOnly": True, "eventTypeIds": ["1"]}})
    
    #list live events, soccer
    status = utils.bf_do('listEvents', token=token, params={"filter":{"inPlayOnly": True, "eventTypeIds": ["1"]}})
    
    #list live events, UEFA CL
    status = utils.bf_do('listEvents', token=token, params={"filter":{"inPlayOnly": True, "competitionIds": ["228"]}})
    
    # filters one live event (e.g. UEFA CL soccer game)
    status = utils.bf_do('listEvents', token=token, params={"filter":{"inPlayOnly": True, "eventIds": ["27515964"]}})
    
    # list markets associated w/ one event, e.g. MATCH_ODDS, OVER_UNDER_15 on a UEFA CL game
    status = utils.bf_do('listMarketTypes', token=token, params={"filter":{"inPlayOnly": True, "eventIds": ["27515964"]}})
    
    # markets details for one event  ('listMarketTypes')
    status = utils.bf_list_mkt(token, '27516487')
    status = utils.bf_list_mkt(token, '27516487', text_query='match*')
    
    # get market prices for one market (listMarketBook)
    status = utils.bf_get_mkt_prices(token, '1.120158817')
    
    #place bet on one specific result (selection, e.g. draw, 0-0, U1.5)
    mkt_id = '1.120158817'
    selection_id = '58805'
    side = 'LAY'
    size = '2'  # $
    price = '1.67' # @this price
    status = utils.bf_place_bet(token, mkt_id, selection_id, side, size, price)
    
    # check orders on one mkt
    status = utils.bf_do('listCurrentOrders', token=token, params={"marketIds":["1.120158817"],"orderProjection":"ALL","dateRange":{}})
    
    # check closed (settled) bets
    status = utils.bf_do('listClearedOrders', token=token, params={"betStatus":"SETTLED"})
    
    
    
    
    
    
    
    
    
    
    
    
    
