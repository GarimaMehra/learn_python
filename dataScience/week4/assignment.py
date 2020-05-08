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

#get_list_of_university_towns()    
 
 
def get_recession_start():
  df = pd.read_excel('dataScience/week4/gdplev.xls', skiprows = 7) 

  df = df.iloc[:,4:7]

  df.columns=['Quarter', 'GDP(current_dollars)', 'GDP(chained_2009_dollars)']
  print(df.head())

  print(type(df.iloc[4]['GDP(current_dollars)']))

  a = df['GDP(current_dollars)'] 
  i = 0
  for item in df['GDP(current_dollars)']:

    if a[i] > a[i+1]> a[i+2]:
      print(item)
      print(df.loc[df['GDP(current_dollars)'] == item, 'Quarter'])
      break
    else:
      i = i+1  
  

#get_recession_start()


def get_recession_end():
  df = pd.read_excel('dataScience/week4/gdplev.xls', skiprows = 7) 

  df = df.iloc[:,4:7]

  df.columns=['Quarter', 'GDP(current_dollars)', 'GDP(chained_2009_dollars)']

  a = df['GDP(current_dollars)'] 
  i = 0
  for item in df['GDP(current_dollars)']:

    if a[i] > a[i+1]> a[i+2] < a[i+3] < a[i+4]:
      value = a[i+2]
      print(value)
      print(df.loc[df['GDP(current_dollars)'] == value, 'Quarter'])
    
    else:
      i = i+1 


get_recession_end()



def get_recession_bottom():
  df = pd.read_excel('dataScience/week4/gdplev.xls', skiprows = 7) 

  df = df.iloc[:,4:7]

  df.columns=['Quarter', 'GDP(current_dollars)', 'GDP(chained_2009_dollars)']

  a = df['GDP(current_dollars)'] 
  i = 0
  for item in df['GDP(current_dollars)']:

    if a[i] > a[i+1]> a[i+2] < a[i+3] < a[i+4]:
      value = a[i+2]
      print(value)
      print(df.loc[df['GDP(current_dollars)'] == value, 'Quarter'])
      break
    else:
      i = i+1 