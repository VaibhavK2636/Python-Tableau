# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 22:46:34 2022

@author: vaibh
"""

import pandas as pd
data=pd.read_csv('transaction.csv')
data=pd.read_csv('transaction.csv',sep=';')
data.info()

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemPurchased = 6  

ProfitPerItem =21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTranscation = NumberofItemPurchased*ProfitPerItem
CostPerTransasction = NumberofItemPurchased*CostPerItem
SellingPricePerTranscation = NumberofItemPurchased*SellingPricePerItem

#CostPerTransactionColumn Calculation

CostPerItem = data["CostPerItem"]
NumberofItemPurchased = data['NumberOfItemsPurchased']
CostPerTransasction= CostPerItem * NumberofItemPurchased 

#Adding a new Column to dataframe

data['CostPerTransaction'] = data['CostPerItem']* data['NumberOfItemsPurchased']

#Sales Per Transaction 

data['SalesPerTransaction']= data['SellingPricePerItem']* data['NumberOfItemsPurchased']

#Profit Calculation= Sales - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup= (sales-cost)/cost

data['Markup'] =( data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction'] 

#Rounding MArkup

roundmarkup = round(data['Markup'],2)
data['Markup'] = roundmarkup

#combining data field of mnth year day

my_date = 'Day'+'-'+'Month'+'-'+'Year'

#changing columns type of day

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day + '-' + data['Month'] + '-' + year

#adding to dataframe

data['Date']= my_date

data.iloc[0]
data.head(10)
data.info()

#Splitting clientkeyword column using split function

split_col = data['ClientKeywords'].str.split(',', expand=True)

#Creating new column for clienteyboard

data['ClientAgeType']= split_col[0]
data['ClientType']= split_col[1]
data['LengthofContract']= split_col[2]

#using replace function remove square brackets in ClientType and LEngth of Contract

data['ClientAgeType'] = data['ClientAgeType'].str.replace('[','')

data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

#Changing itemDEscription to lowercase using lower function

data['ItemDescription'] = data['ItemDescription'].str.lower()

#bringing in a new dataset

seasons= pd.read_csv('value_inc_seasons.csv',sep=';')

#merging two dataframws 

data = pd.merge(data, seasons, on='Month')

#dropping unneccessary columns

data = data.drop('ClientKeywords',axis = 1)
data = data.drop(['Year','Day','Month'],axis=1)

#Export into csv

data.to_csv('ValueincCleaned.csv',index= False)














