import pandas as nd 
import math
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
import statistics

yf.pdr_override()
stock_standard_devs="Stock Portfolio"
addstock=input("Add stock to portfolio Y or N: ")
startyear=2010
startmonth=5
startday=18

start=dt.datetime(startyear,startmonth,startday)

now=dt.datetime.now()

index = nd.date_range(start,now)
columns = ['Stock Portfolio']

df_std = nd.DataFrame(index=index, columns=columns)
stockweight=[]

while (addstock=="Y"):
	stock=input("Enter a stock ticker symbol: ")
	stock_weight=input("Enter the stocks weight in the portfolio as a percentage: ")
	print(stock)
	print(stock_weight + "%")
	df=pdr.get_data_yahoo(stock,start,now)

	dailyreturnString="Daily_return"
	df[dailyreturnString]=((df.iloc[:,4]-df.iloc[:,4].shift(1))/df.iloc[:,4].shift(1))*100

	print("Annualized Return is " + str(sum(df.iloc[1:,6])/(len(df.index)/252)))

	print("Standard Deviation of the stock is % s " 
       		       	% (math.sqrt(252)*statistics.stdev(df.iloc[1:,6])))

	stock_standard_devs+= "\n Stock: "+ stock +" Standard Deviation: " + str(math.sqrt(252)*statistics.stdev(df.iloc[1:,6])) + " Annualized Return: " + str(sum(df.iloc[1:,6])/(len(df.index)/252))

	addstock=input("Add stock to portfolio Y or N: ")

	df_std[stock] = df.iloc[:,6]
	stockweight.append(stock_weight)


print(df_std.cov())	
print(stock_standard_devs)
print(stockweight)
