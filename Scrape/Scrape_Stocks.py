import json
import http.client

conn = http.client.HTTPSConnection("alpha-vantage.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "1bbb117181msh365e8a8b90b27b2p1fa8acjsn45f2505b6b3b",
    'X-RapidAPI-Host': "alpha-vantage.p.rapidapi.com"
    }

symbols_file = json.load(open("./data/stock_tickers.json","r"))

months = [f"month{month}" for month in range(1,13)]
intervals = [f"year{year}{month}" for month in months for year in range(1,3)]

for symbol in symbols_file["symbols"]:
     break # run when ready, this will break development time for a while
     for interval in intervals:
          conn.request("GET", f"/query?interval=1min&function=function=TIME_SERIES_INTRADAY_EXTENDED&symbol={symbol}&slice={interval}&datatype=json&output_size=full", headers=headers)
          res = conn.getresponse()
          data = res.read()
          try:
               with open(f"./data/stocks/{symbol}","w") as f:
                    f.write(data.decode("utf-8"))
          except FileNotFoundError:
               import os
               os.mkdir("./data/stocks")
               with open(f"./data/stocks/{symbol}_{interval}","w") as f:
                    f.write(data.decode("utf-8"))


