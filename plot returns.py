import yfinance as yf
import datetime as dt
import numpy as np
import pandas
import matplotlib.pyplot as plt


endDate = dt.date.today() # End date and today
startDate = dt.date.today() - dt.timedelta(days=(365*5)) # Start date is 5 years ago

# List of stocks of interest

stocks = ["AAPL","MSFT","GOOGL","AMZN",
          "TSLA","META","NVDA","V","JNJ",   
          "WMT","UNH","MA","DIS"]



data = yf.download(stocks, start = startDate, end = endDate) # Download relevant data from Yahoo Finance
close_prices = data['Close'] # Extract closing price on each day
print(stocks[1])
print(close_prices.iloc[:5,0]) # Check first item in table


# Calculates log returns each day 

logprice = np.log(close_prices/close_prices.shift(1))
cum_logprice = logprice.cumsum()


# Plot the graph for visualisation

cum_logprice.plot(title = "Cumulative Returns", figsize = (10,6))
plt.show()

