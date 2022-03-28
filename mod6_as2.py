# -*- coding: utf-8 -*-
"""mod6_as2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19RkoEwxagotWnSsAuGjnt4E1qiY9Yc8D
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/content/Hurricanes.csv")

x = df["Year"]
y = df["Hurricanes"]

plt.bar(x,y)
plt.xlabel("Year")
plt.ylabel("Hurricanes")
plt.grid()
plt.title("Hurricanes vs Year")

plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right') # Rotate Axis Labels

plt.show()

df_temp = pd.read_csv("/content/CityTemps.csv")
print(df_temp)

x_mosco = df_temp["Moscow"]
x_san_Francisco = df_temp["San Francisco"]

plt.hist(x_mosco, len(x_mosco), facecolor='blue', alpha=0.5)
plt.hist(x_san_Francisco, len(x_san_Francisco), facecolor='red', alpha=0.5)

plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.title("Temperatures of Mosco and San Francisco")

plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right') # Rotate Axis Labels

plt.show()

import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv('/content/Cars2015.csv',delimiter=',')

df = df.drop(['Type','LowPrice','HighPrice','Drive','CityMPG','HwyMPG','FuelCap','Length'], axis=1)

df = df.drop(['Width','Wheelbase','Height','UTurn','Weight','Acc030','Acc060'],axis=1)

df = df.drop(['QtrMile','PageNum','Size'],axis=1)

#based on make count the number of models

df['count'] = df.groupby('Make')['Make'].transform('count')
df.drop_duplicates('Make',inplace=True)

df.sort_values(by='count',ascending=False,inplace=True)

#Based on the count obtain we will plot our graph.

plt.figure(figsize=(50,8))

ax1 = plt.subplot(121, aspect='equal')

df.plot(kind='pie', y = 'count', ax=ax1, autopct='%1.1f%%',startangle=90, shadow=False, labels=df['Make'], legend = False, fontsize=10) 

plt.show()

import pandas as pd
df=pd.read_csv('/content/sample-salesv2.csv')
print(df.head())

print(df['unit price'].describe())

customers = df[['name','net_price','date']]

print(customers)

customer_group = customers.groupby('name')
customer_group.size()

sales_totals = customer_group.sum()
sales_totals.sort_values(by ='net_price').head(10)

my_plot =sales_totals.sort_values(by ='net_price',ascending=False).plot(kind='bar',legend=None,title="Total Sales by Customer")
my_plot.set_xlabel("Customers")
my_plot.set_ylabel("Sales ($)")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

X = [1, 2, 3, 4]
Y = [20, 21, 20.5, 20.8]

# 1. Draw a Simple plot
plt.plot(X, Y)
plt.show()

plt.plot(X, Y)
plt.grid()
plt.show()

plt.setp(plt.gca().get_xticklabels(), rotation=90,
         horizontalalignment='right')

plt.plot(X, Y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

y_error = [0.12, 0.13, 0.2, 0.1]

plt.plot(X, Y, y_error)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.figure(figsize=(3, 4))

plt.rcParams.update({'font.size': 14})

x = np.random.random(50)
y = np.random.random(50)

plt.scatter(x, y)
plt.show()

df = pd.DataFrame({
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
})

plt.scatter(df["preTestScore"], df["postTestScore"],s=df['age'])
plt.xlabel("preTestScore")
plt.ylabel("postTestScore")
plt.title("preTestScore vs postTestScore")
plt.legend(["preTestScore", "postTestScore"])
plt.show()

df = pd.DataFrame({
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    'female': [0, 1, 1, 0, 1],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70]
})

x = df["preTestScore"]
y = df["postTestScore"]
colors = df["female"]

plt.scatter(x, y, alpha=0.5,s=300,c=df.female)
plt.xlabel("preTestScore")
plt.ylabel("postTestScore")
plt.title("preTestScore vs postTestScore")
plt.legend(["preTestScore", "postTestScore"])
plt.show()