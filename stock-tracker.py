import pandas as pd 
import requests
import numpy as np

ticker = "AAPL"

def getdata(url):
  r = requests.get(url,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
  data = pd.read_html(r.text)
  return data

summary_url = f'https://finance.yahoo.com/quote/{ticker}?p={ticker}'
summary_data = getdata(summary_url)

data = [summary_data[0], summary_data[1]]
data = pd.concat(summary_data)
data.reset_index(drop=True, inplace=True)

df = data.transpose()
df.columns = df.iloc[0]
df = df.drop(0)
df = df.reset_index(drop=True)

historiscal_url= f'https://finance.yahoo.com/quote/{ticker}/history?p={ticker}'
historiscal_data = getdata(historiscal_url)
data = historiscal_data[0]

