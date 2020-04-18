import pandas as pd
import numpy as np
#print(None == None)
#print(np.nan == np.nan)

df = pd.read_csv('dataScience/week2/olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
#print(df.head())

def answer_one():
  response = -1
  dfl = df
  dfl = dfl[ dfl['Gold'] == dfl['Gold'].max()]
  print(dfl.head())
  response = dfl.index[0]
  return response


def answer1():
  df2 = df
  df2['country'] = df2.index
  df2=df2.set_index('Gold')
  a = df2.loc[df2.index.max()]['country']
  return a


def answer1v2():
  df2 = df.Gold#same as df['Gold']
  return df2.idxmax()

def answer_twov2():
  return (df['Gold'] - df['Gold.1']).abs().argmax()
  
def answer_two():
  df2 = df
  df2['Difference']= abs(df2['Gold']-df2['Gold.1'])
  df2 = df2[df2['Difference']== df2['Difference'].max()]
  response = df2.index[0]
  return response


def answer2():
  df2 = df
  df2['Difference'] = abs( df2['Gold']- df2['Gold.1'])
  df2['country'] = df2.index
  df2 = df2.set_index('Difference')
  a = df2.loc[df2.index.max()]['country']
  return a
  
def answer_three():
  df2 = df.copy()
  df2= df2[(df2['Gold']>0) & df2['Gold.1']>0]  
  df2['Rel_diff'] = abs(df2['Gold'] - df2['Gold.1'])/df2['Gold.2']
  df2 = df2[df2['Rel_diff']== df2['Rel_diff'].max()]
  response = df2.index[0]
  return response




def answer3():
  df2 = df.copy()
  df2= df2[(df2['Gold']>0) & df2['Gold.1']>0]
  print(df2.head())
  df2['total'] = df2['Gold'] + df2['Gold.1']
  print(type(df2['total']))
  print(type(df2['Gold.2']))
  k = df2['total'].equals(df2['Gold.2'])
  print(df2.head())
  df2['Rel_diff'] = abs(df2['Gold'] - df2['Gold.1'])/df2['total']
  print(df2.head())
  a = df2['Rel_diff'].max()
  print(a)
  df2 = df2[df2['Rel_diff']== df2['Rel_diff'].max()]
  response = df2.index[0]
  return response


def answer4():
  df2 = df.copy()
  df2['Points'] = df2['Gold.2']*3 + df2['Silver.2']*2 + df2['Bronze.2']
  return df2['Points']

census_df= pd.read_csv('dataScience/week2/census.csv')

def answer5():
  df2 = census_df
  dfGrpBy = df2.groupby('STNAME')
  dfGrpBySeries = dfGrpBy.size()
  #print(df2.groupby('STNAME').size().idxmax())
  return dfGrpBySeries.idxmax()

#answer5()

#group by pandas.Dataframe https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm and https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/
  
  


  
  
  











