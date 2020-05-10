import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def get_list_of_university_towns():
  df = pd.read_fwf('dataScience/week4/university_towns.txt')
  df= df.append({'Alabama[edit]': 'Fake data<to be removed>'}, ignore_index = True)
  df['Alabama[edit]'] = df['Alabama[edit]'].shift(1)
  df.iloc[0] = 'Alabama[edit]'
  df.columns = ['RegionName']
  a = []
  for item in df['RegionName']:
    if item[-6:] == '[edit]':
      x = item.split('[edit]')[0]
      a = a + [x] 
    else:
      a = a + [x] 
  df['RegionName'] = df['RegionName'].str.split('(').str[0]
  df['RegionName'] = df['RegionName'].str.split('[').str[0]
  df['RegionName'] = df['RegionName'].str.rstrip()
  df['State'] = a
  df = df[df['State']!= df['RegionName']]
  df = df[['State', 'RegionName']]
  df = df.reset_index(drop=True)
  return df    

 
def get_recession_start():
  df = pd.read_excel('dataScience/week4/gdplev.xls', skiprows = 219) 
  df = df.iloc[:,4:7]
  df.columns=['Quarter', 'GDP(current_dollars)', 'GDP(chained_2009)']
  i = 0
  gdpColName = 'GDP(chained_2009)'
  for i in range (0, (len(df[gdpColName])-2)):
    if df[gdpColName][i] > df[gdpColName][i+1] > df[gdpColName][i+2]:
      answer = df.iloc[i]['Quarter']
      return answer

def get_recession_end():
  df = pd.read_excel('dataScience/week4/gdplev.xls', skiprows = 219) 
  df = df.iloc[:,4:7]
  df.columns=['Quarter', 'GDP(current_dollars)', 'GDP(chained_2009)']
  start = get_recession_start()
  start_index = df[df['Quarter'] == start].index.tolist()[0]
  df = df.iloc[start_index:]
  df = df.reset_index(drop=True)
  gdpColName = 'GDP(chained_2009)'
  for i in range (0, len(df[gdpColName])-2):
    if df[gdpColName][i]< df[gdpColName][i+1] < df[gdpColName][i+2]:
      answer = df.iloc[i+2]['Quarter']
      return answer


def get_recession_bottom():
  df = pd.read_excel('dataScience/week4/gdplev.xls', skiprows = 219) 
  df = df.iloc[:,4:7]
  df.columns=['Quarter', 'GDP(current_dollars)', 'GDP(chained_2009)']
  start = get_recession_start()
  start_index = df[df['Quarter'] == start].index.tolist()[0]
  end = get_recession_end()
  end_index = df[df['Quarter'] == end].index.tolist()[0]
  df = df.iloc[start_index:end_index + 1]
  gdpColName = 'GDP(chained_2009)'
  answer = df.loc[df[gdpColName].idxmin()]['Quarter']
  return answer

def convert_housing_data_to_quarters():
  df = pd.read_csv('dataScience/week4/City_Zhvi_AllHomes.csv')

  df = df.drop(df.loc[:, '1996-04':'1999-12'].columns, axis = 1)
  
  df['State'] = df['State'].replace({'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'})
  i = 2000
  while i <= 2016:
    df[str(i)+'q1'] = df[[ str(i)+'-01', str(i)+'-02', str(i)+'-03']].mean(axis=1)
    df[str(i)+'q2'] = df[[ str(i)+'-04', str(i)+'-05', str(i)+'-06']].mean(axis=1)
    if i == 2016:
      df[str(i)+'q3'] = df[[ str(i)+'-07', str(i)+'-08']].mean(axis=1)
    else:  
      df[str(i)+'q3'] = df[[ str(i)+'-07', str(i)+'-08', str(i)+'-09']].mean(axis=1)
      df[str(i)+'q4'] = df[[ str(i)+'-10', str(i)+'-11', str(i)+'-12']].mean(axis=1)
    i = i+1
  df = df.set_index(['State', 'RegionName'])  
  df = df.iloc[:,-67:] 
  return df

def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    recessionStartQuarter = get_recession_start()
    recessionBottomQuarter = get_recession_bottom()
    housingData = convert_housing_data_to_quarters()
    df = housingData
    columnsDf = df.columns.to_frame(index=False)
    index = columnsDf[ columnsDf[0] == recessionStartQuarter].index.tolist()[0]
    quarterBeforeRecessionStart = columnsDf.iloc[index-1][0]
    df['price_ratio'] = df[quarterBeforeRecessionStart]/df[recessionBottomQuarter]
    df = df[['price_ratio']]
    allUnivTown = get_list_of_university_towns()
    df1 = allUnivTown
    df1 = df1.set_index(['State', 'RegionName']) 
    univTownHouseData = df1.merge(df, how = 'inner',left_index= True, right_index=True) 
    nonUnivTownHouseData = df1.merge(df, how = 'right',left_index= True, right_index=True)
    stat, pVal = ttest_ind(univTownHouseData['price_ratio'].dropna(), nonUnivTownHouseData['price_ratio'].dropna())
    if pVal<0.01:
      different = True
    else:
      different = False
    if univTownHouseData['price_ratio'].mean() < nonUnivTownHouseData['price_ratio'].mean():
      better = "university town"
    else:
      better = "non-university town"
    return (different, pVal, better)



