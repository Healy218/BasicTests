import nltk
import requests
import re
import cvxpy as cvx
import numpy as np
import pandas as pd
import time
from pandas_datareader import data
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from alpha_vantage.techindicators import TechIndicators
from bs4 import BeautifulSoup


#ti = TechIndicators(key='11XRM636J0MM8T38', output_format='pandas')
#ts = TimeSeries(key='11XRM636J0MM8T38', output_format='pandas')
#data, meta_data = ts.get_weekly('TLRY')
#pprint(data.head(15))
#data['4. close'].plot()
#plt.title('Weekly Tilray Graph')
#plt.show()
#data2, met_data2 = ti.get_bbands(symbol='TLRY', interval='60min', time_period=60)
#data2.plot()
#plt.show()

r = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(r.text, "html5lib")
regex = re.compile(r' a')
matches = regex.finditer(r)
for match in matches:
    print(match)
#print(soup.get_text())

