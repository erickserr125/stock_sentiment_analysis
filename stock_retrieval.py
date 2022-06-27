#!/usr/bin/env python
"""
List of Exchanges using Finnhub Excel sheet
TODO: Consider automating search for list of exchanges
Current list (https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing):

AS,AT,AX
BA,BC,BD,BE,BK,BO,BR
CA,CN,CO,CR,
DB,DE,DU
F
HE,HK,HM
IC,IR,IS
JK,JO
KL,KQ,KS
L,LN,LS
MC,ME,MI,MU,MX
NE,NL,NS,NZ
OL
PA,PM,PR
QA
RG
SA,SG,SI,SN,SR,SS,ST,SW,SZ
T,TA,TL,TO,TW,TWO
US
V,VI,VN,VS
WA,HA,SX,TG,SC
"""

import finnhub
import time

def retrieve_exchanges_and_stock(exchanges,api_key, output_proc = False):
    """
    :param Exchanges: List(Str) - Global Stock Exchanges
    :param api_key: Str - Finnhub API Key
    :param output_proc: Bool - Output progress of the code

    :return exchange_dict: dict of dicts, stocks per exchange. Stock dicts contain:
         a) Currency (currency)
         b) Description (description)
         c) Display Symbol (displaySymbol)
         d) FIGI Identifier (figi)
         e) isin -- NOT USED
         f) mPrimary Exchange's MIC (mic)
         g)Share Class FIGI (shareClassFIGI)
         h)Stock Ticker (symbol)
         i)Alternative Ticker (symbol2)
         j)Security Type (type)


    REMOVE TRY/EXCEPT IF API LIMIT IS REMOVED
    Free Plan Limit: 30 calls/minute
    Will send 429 error if limit reached
    """
    if(output_proc):
        print("Beginning Stock Exchange/Stock Retrieval...")

    #Logging into finnhub
    finnhub_client = finnhub.Client(api_key = "{}".format(api_key))
    exchange_dict = {}
    if(output_proc):
        print("Collected finnhub api-key")
        print("Beginning stock information collection")

    start_time = time.time()
    for exchange_name in exchanges:
        #Two possible errors:
        #1) Call limit reached or
        #2) exchange is no longer valid
        #The following code DOES NOT account for the latter error
        try:
            data = finnhub_client.stock_symbols(exchange_name)
        except:
            print("Delaying calls by ",time.time()-start_time)
            time.sleep(time.time()-start_time)
            print("Resuming calls")
            start_time = time.time()#Reset start_time
            data = finnhub_client.stock_symbols(exchange_name)
        if (not (exchange_name in exchange_dict)):
            exchange_dict[exchange_name] = data

    if(output_proc):
        print("Returning list of exchanges and exchange_data...")

    return exchange_dict