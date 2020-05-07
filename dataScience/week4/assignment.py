import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)

def get_list_of_university_towns():
  df = pd.read_fwf('dataScience/week4/university_towns.txt')
  s2 = pd.Series(['ABC'])

  df= df.append(s2, ignore_index = True)
  df['Alabama[edit]'] = df['Alabama[edit]'].shift(1)
  df.iloc[0] = 'Alabama[edit]'
  df.columns = ['RegionName','StateName']
  print(df.head())
  df = df.drop(['StateName'], axis = 1)
  a = []

  for item in df['RegionName']:
    if item[-6:] == '[edit]':
      x = item.split('[edit]')[0]
      a = a + [x] 
    else:
      a = a + [x] 
  df['RegionName'] = df['RegionName'].str.replace(r" \(.*\)","").str.replace(r"\[.*\]","")
  df['State'] = a
  df = df[['State','RegionName']]

  print(df)  

get_list_of_university_towns()    
 
 
  
 




