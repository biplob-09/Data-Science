# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:47:07 2022

@author: sayan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("HollywoodMovies.csv")
print(df.head())

print(df.describe())

print(df.columns)

df.drop("TheatersOpenWeek",axis=1,inplace=True)
df.drop("OpeningWeekend",axis=1,inplace=True)
df.drop("BOAvgOpenWeekend",axis=1,inplace=True)
df.drop("DomesticGross",axis=1,inplace=True)
df.drop("ForeignGross",axis=1,inplace=True)
df.drop("WorldGross",axis=1,inplace=True)
df.drop("LeadStudio",axis=1,inplace=True)

highest_rate = df[df["Story"] == "Quest"]["RottenTomatoes"].max()
highest_rate_movie=df[df['RottenTomatoes']==highest_rate]
highest_rate_movie.dropna(axis=0,how='any',inplace=True) # dropping the rows with NAN in quest.

genre_group=df.groupby("Genre").count()

max_movie_release=genre_group.index[genre_group["Movie"]==genre_group["Movie"].max()].tolist()
print("The maximun no of movie released unded Genre is :",max_movie_release)

sorted_df = df.sort_values("Budget", ascending=False)

sorted_df = sorted_df[sorted_df["Budget"] > 0]  # removing nan values

print(sorted_df.head(5))


plt.scatter(df["RottenTomatoes"], df["AudienceScore"])
plt.title("Audiece acceptance vs crtics ")
plt.xlabel("RottenTomatoes")
plt.ylabel("AudienceScore")
plt.show()

# Is there any correspondence between the critics’ evaluation of a movie and itsacceptance by the public?
# Yes there is a relation between them... Critics evaluation and public reponse is direcly propotional
# to each other.

# Graph between RottenTomatoes vs Profitability
plt.scatter(df["RottenTomatoes"], df["Profitability"])
plt.title("Profitalibility vs crtics Evaluation ")
plt.xlabel("RottenTomatoes")
plt.ylabel("Profitalibility")
plt.show()


#5 quest

dic={'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
     'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
     'age': [42, 52, 36, 24, 73], 
     'preTestScore': [4, 24, 31, ".", "."],
     'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df=pd.DataFrame(dic)
df.to_csv('example.csv')
df_1=pd.read_csv("example.csv")
print(df_1)
df_1=pd.read_csv("example.csv",header=None)
print(df_1)
df_with_index = pd.read_csv("example.csv", index_col=["first_name", "last_name"])

#Print  the  data  frame  in  a  Boolean  form  as  True  or  False.  True  for  Null/  NaN values and false for non-nullvalues
boolean_df = df.isnull().any()
print(boolean_df)

#Read the dataframe by skipping first 3 rows and print the data frame
df_skip=df[3:]
print(df_skip)

data=pd.read_csv("example.csv", thousands=",")


data=pd.Series(["Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat"])
#a
print(data.str.lower())
#b
print(data.str.upper())
#c
print(data.str.len())


#6.2
series_=pd.Series([' Atul', 'John ', ' jack ', 'Sam'])
#a
print(series_.str.strip())
#b
print(series_.str.lstrip())
#c
print(series_.str.rstrip())


#6.3
pseries=pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])

#a
list_splited = [str(ele).split("_") for ele in pseries]
print(list_splited)

#b
flatten_list = []

# b) Access the individual element of a list
for sublist in list_splited:
    for l in sublist:
        flatten_list.append(l)
        print(l)

# c) Expand the elements so that all individual elements get splitted by ‘_’ and insted of list returns individual elements
print(flatten_list)

#6.4
ser6=pd.Series(['A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'])
ser6.str.replace('X',"XX-XX").replace('dog',"XX-XX")

#6.5
ser7=pd.Series(['12', '-$10', '$10,000'])
series_remov_dollar_sign=[str(ele).replace("$", "") for ele in ser7]
print(series_remov_dollar_sign)

#6.6
ser7=pd.Series(['india 1998', 'big country', np.nan])
print(ser7[::-1])
#rev_=[str(ele)[::-1] for ele in ser7]
print(rev_)

#6.7
series_7 = pd.Series(['1', '2', '1a', '2b', '2003c'])
print(series_7)

series_aplha_check = [str(ele).isalnum() for ele in series_7]
print(series_aplha_check)

#6.8
series8=pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'])
valueA=['A' in ele for ele in series8]
print(valueA)

#6.9
import regex as re
series9=pd.Series(['a', 'a|b', np.nan, 'a|c'])
series_a_b_c_exists = [1 if re.match(
    "[abc]", str(ele)) else 0 for ele in series9]
print(series_a_b_c_exists)

#6.10
df1 = pd.DataFrame({'key': ['One', 'Two'], 'ltable': [1, 2]})
df2 = pd.DataFrame({'key': ['One', 'Two'], 'rtable': [4, 5]})

print(df1)
print(df2)

df_merge = pd.merge(df1, df2, sort=True)
print(df_merge)