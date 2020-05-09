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
  df = df.drop(['StateName'], axis = 1)
  a = []
  for item in df['RegionName']:
    if item[-6:] == '[edit]':
      x = item.split('[edit]')[0]
      a = a + [x] 
    else:
      a = a + [x] 
  df['RegionName'] = df['RegionName'].str.split('(').str[0]
  df['State'] = a
  df = df[['State','RegionName']]
  return df  

#print(get_list_of_university_towns())    
 
 
def get_recession_start():
  df = pd.read_excel('dataScience/week4/gdplev.xls', skiprows = 219) 
  df = df.iloc[:,4:7]
  df.columns=['Quarter', 'GDP(current_dollars)', 'GDP(chained_2009)']
  df=df.set_index('Quarter')
  i = 0
  while i < (len(df['GDP(chained_2009)'])-2):
    if df['GDP(chained_2009)'][i] > df['GDP(chained_2009)'][i+1]> df['GDP(chained_2009)'][i+2]:
      value = df['GDP(chained_2009)'][i]
      answer = df[ df['GDP(chained_2009)'] == value].index[0]
    i = i+1
  return answer 

#print(get_recession_start())

def get_recession_end():
  df = pd.read_excel('dataScience/week4/gdplev.xls', skiprows = 219) 
  df = df.iloc[:,4:7]
  df.columns=['Quarter', 'GDP(current_dollars)', 'GDP(chained_2009)']
  df=df.set_index('Quarter')
  i = 0
  while i < (len(df['GDP(chained_2009)'])-3):
    if df['GDP(chained_2009)'][i] > df['GDP(chained_2009)'][i+1]< df['GDP(chained_2009)'][i+2] < df['GDP(chained_2009)'][i+3]:
      value = df['GDP(chained_2009)'][i+3]
      #answer = (df.loc[df['GDP(chained_2009_dollars)'] == value, 'Quarter'])
      answer = df[ df['GDP(chained_2009)'] == value].index[0]
    i = i+1 

  return answer
#print(get_recession_end())



def get_recession_bottom():
  df = pd.read_excel('dataScience/week4/gdplev.xls', skiprows = 219) 
  df = df.iloc[:,4:7]
  df.columns=['Quarter', 'GDP(current_dollars)', 'GDP(chained_2009)']
  df=df.set_index('Quarter')
  i = 0
  while i < (len(df['GDP(chained_2009)'])-3):
    if df['GDP(chained_2009)'][i] > df['GDP(chained_2009)'][i+1]< df['GDP(chained_2009)'][i+2] < df['GDP(chained_2009)'][i+3]:
      value = df['GDP(chained_2009)'][i+1]
      answer = df[ df['GDP(chained_2009)'] == value].index[0]
    i = i+1 
  return answer
#print(get_recession_bottom())    


def convert_housing_data_to_quarters():
  df = pd.read_csv('dataScience/week4/City_Zhvi_AllHomes.csv')

  df = df.drop(df.loc[:, '1996-04':'1999-12'].columns, axis = 1)
  
  df['State'] = df['State'].replace({'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'})
  i = 2000
  while i <= 2016:
    df[str(i)+'q1'] = (df[str(i)+'-01']+ df[str(i)+'-02'] + df[str(i)+'-03'])/3
    df[str(i)+'q2'] = (df[str(i)+'-04']+ df[str(i)+'-05'] + df[str(i)+'-06'])/3
    if i == 2016:
      df[str(i)+'q3'] = (df[str(i)+'-07']+ df[str(i)+'-08'])/2
      break
    else:  
      df[str(i)+'q3'] = (df[str(i)+'-07']+ df[str(i)+'-08'] + df[str(i)+'-09'])/3
      df[str(i)+'q4'] = (df[str(i)+'-10']+ df[str(i)+'-11'] + df[str(i)+'-12'])/3
    i = i+1
  df = df.set_index(['State', 'RegionName'])  
  df = df.iloc[:,-67:] 
  return df

  
   
  

print(convert_housing_data_to_quarters())
