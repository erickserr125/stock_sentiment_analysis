"""
retrieve_exchanges_and_stock will give us a list of exchanges and stock information per exchange
-One Stock Information includes:
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

our next goal is to:
1) Retrieve news data about company sources (News API)

"""
import subprocess
import datetime
import json
#import os
#from dotenv import load_dotenv, find_dotenv

#Retrieves stock from a certain length ago (maybe more if needed)
def retrieve_articles(stock_symbol, days_ago, api_key,output_proc = False):
    """
    :param stock_symbol: - Stock to lookup on NEWS API
    :param days_ago: - Number of days to look back for an article (max -30 for developer plan)
    :param api_key: - Local API Key
    :param output_proc: - Output the steps in the process
    Output:
    :return status: retrieve status of lookup. If error, returns error code instead of json.loads(article_data)
    :return json.loads(article_data): - Json/Dict of the individual stock :
    1) Status
    2) totalResults
    3) articles[]
        a) Source {}(id, name)
        b) author
        c) title
        d) description
        e) url
    """
    #TODO: Remove if News API plan is upgraded
    if(days_ago > 30):
        return "Error: days_ago is too large for News API's developer plan."

    if(output_proc):
        print("Collecting article data on ", stock_symbol, "from ", days_ago, " days ago.")

    today = datetime.datetime.now()
    date = today - datetime.timedelta(days = days_ago)
    article_data = subprocess.run(["curl", "https://newsapi.org/v2/everything",
                                   "-G", "-d", "q={}".format(stock_symbol),
                                   "-d", "from={}".format(date),
                                   "-d", "sortBy=popularity","-d",
                                   "apiKey={}".format(api_key)], stdout = subprocess.PIPE).stdout.decode('utf-8')
    #Watchout for unnecessary data
    dict_article = json.loads(article_data)
    if(dict_article["status"] == "error"):
        print("Error:", dict_article["code"])
        print(dict_article["message"])
        return dict_article["status"], dict_article["code"]
    if(output_proc):
        print("Returning json data")
    return dict_article["status"], dict_article

def save_data(file_name, dict_data):
    with open(file_name, 'w') as fp:
        json.dump(dict_data, fp)


#Test
#load_dotenv(find_dotenv()) #Looks for .env file
#news_api_key = os.getenv('NEWS_API_KEY')
#print(news_api_key)
#a = retrieve_articles("AAPL", 30, news_api_key, True)
#print(a)