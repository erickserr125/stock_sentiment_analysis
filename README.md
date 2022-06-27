# stock_sentiment_analysis
Using the FinnhubAPI, NEWS API, and the roBERTa pre-trained sentiment analyzer, I measure the average sentiment of stocks in the US Stock market. 

## Limitations

This code is limited by the free plans listed by the Finnhub and News APIs. Finnhub limits calls to 30 calls/sec,
and News limits calls to 100 per day. In addition to some extra filtering, that leaves us with less than 100 stocks to analyze per day. 
Some possible fixes could include upgrading the payment plan, searching for articles manually, or using a different API.

## Results

The code successfully measured the average positivity, negativity, and neutrality of several stocks.
`sentiment_analyzer.py` contains the results and barplots. 
