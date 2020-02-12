import requests
import json

APP_NAME = ''
APP_KEY = ''
APP_KEY_DELAY = ''

#LOGIN
def bf_login(username='', password=''):
    
    header = { 'X-Application' : APP_KEY, 'Accept' : 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' }

    up = 'username=' + username + '&password=' + password
    url = 'https://identitysso.betfair.it/api/login'
    response = requests.post(url, data=up, headers=header)
    print json.dumps(json.loads(response.text), indent=3)
    
    return response.json()['token']

# KEEPALIVE
def bf_keepalive(token):
    url = 'https://identitysso.betfair.it/api/keepAlive'
    header = { 'X-Application' : APP_KEY, 'X-Authentication' : token,'Accept' : 'application/json' }
    response = requests.post(url, headers=header)
    print json.dumps(json.loads(response.text), indent=3)    
    return response.status_code

# LOGOUT
def bf_logout(token):
    url = 'https://identitysso.betfair.it/api/logout'
    header = { 'X-Application' : APP_KEY, 'X-Authentication' : token,'Accept' : 'application/json' }
    response = requests.post(url, headers=header)
    print json.dumps(json.loads(response.text), indent=3)    
    return response.status_code

#DO_SMTHING
def bf_do(api, token, params={"filter":{ }}):
    endpoint = "https://api.betfair.com/exchange/betting/rest/v1.0/"
    header = { 'X-Application' : APP_KEY, 'X-Authentication' : token ,'content-type' : 'application/json' }
    url = endpoint + api + "/"
    response = requests.post(url, data=json.dumps(params), headers=header)
    print json.dumps(json.loads(response.text), indent=3)
    return response.status_code

def bf_list_mkt(token, event_id, text_query=None):
    if text_query is not None:
        params = {
                "filter": {
                           #"eventTypeIds": ["2"],
                           #"inPlayOnly": True,
                           "textQuery": text_query,
                           "eventIds": [event_id]
                },
                "maxResults": "200",
                "marketProjection": [
                    "COMPETITION",
                    "EVENT",
                    "EVENT_TYPE",
                    "RUNNER_DESCRIPTION",
                    "RUNNER_METADATA",
                    "MARKET_START_TIME"
                    ]
                  }
    else:
        params = {
                "filter": {
                           #"eventTypeIds": ["2"],
                           #"inPlayOnly": True,
                           "eventIds": [event_id]
                },
                "maxResults": "200",
                "marketProjection": [
                    "COMPETITION",
                    "EVENT",
                    "EVENT_TYPE",
                    "RUNNER_DESCRIPTION",
                    "RUNNER_METADATA",
                    "MARKET_START_TIME"
                    ]
                  }        
    return bf_do('listMarketCatalogue', token=token, params=params)
    
def bf_get_mkt_prices(token, mkt_id):
    params = {
              "marketIds": [mkt_id],
              #"orderProjection": "EXECUTABLE",
              "priceProjection": {
                            #"priceData" : ["EX_ALL_OFFERS"],
                            "priceData" : ["EX_BEST_OFFERS"],
                            "exBestOffersOverrides": {
                                                      "bestPricesDepth": 3
                                                      }
                            }
              }
    return bf_do('listMarketBook', token=token, params=params)


def bf_place_bet(token, mkt_id, selection_id, side, size, price):
    '''
    param:selection_id   id del risultato puntato
    param:side "BACK" (punta) "LAY" (banca)
    param:size e.g. "2" euro
    '''
    params = {
            "marketId": mkt_id,
            "instructions": [
                {
                    "selectionId": selection_id,
                    "handicap": "0",
                    "side": side,
                    "orderType": "LIMIT",
                    "limitOrder": {
                        "size": size,
                        "price": price,
                        "persistenceType": "LAPSE"
                    }
                }
            ]
        }
    return bf_do('placeOrders', token=token, params=params)
    


