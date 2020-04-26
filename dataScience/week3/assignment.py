import pandas as pd
import numpy as np

energy = pd.read_excel('dataScience/week3/Energy Indicators.xls')
energy = energy[17: 245]
print(energy.shape)
energy.drop(energy.columns[[0,1]], axis = 1, inplace = True) 
energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
print (energy.head())
energy['Energy Supply'] = energy['Energy Supply']*1000000
print (energy['Energy Supply'])
energy['Country'] = energy['Country'].str.replace('\d+', '')
energy['Country'] = energy['Country'].str.replace(r"\s*\([^()]*\)","").str.strip()
#print(energy.iloc[197])
#print(energy.iloc[11])
#print(energy.iloc[24])

energy['Country'] = energy['Country'].replace({"Republic of Korea": "South Korea", "United States of America": "United States", "United Kingdom of Great Britain and Northern Ireland": "United Kingdom", "China, Hong Kong Special Administrative Region": "Hong Kong"})

print(energy['Country'])
print(energy.iloc[43]['Country'])

GDP = pd.read_csv('dataScience/week3/world_bank.csv', skiprows = 4)

print(GDP.head())
print(GDP.shape)
GDP['Country Name'] = GDP['Country Name'].replace({'Korea, Rep.': 'South Korea', 'Iran, Islamic Rep.':'Iran', 'Hong Kong SAR, China': 'Hong Kong'})
print(GDP.head())
print(GDP.iloc[124])
print(GDP.iloc[94])

Scimen = pd.read_excel('dataScience/week3/scimagojr-3.xlsx')
print(Scimen.head())
print(Scimen.shape)

energy=energy.set_index('Country')
print(energy.head())

GDP = GDP.set_index('Country Name')
GDP = GDP.loc[:, '2006':'2015'] 
print(GDP.head())

Scimen = Scimen.set_index('Country')
print(Scimen.head())

df1 = pd.merge(Scimen, energy, how = 'inner', left_index = True, right_index =True)
print(df1.head())
print(df1.shape)
df2 = pd.merge(df1, GDP, how ='inner',left_index = True, right_index = True)
df3 = df2[:15]
print(df3)
print(df3.shape)

def answer_two():
  missing_entries = len(df2)-len(df3)
  print(missing_entries)



def answer_three():
  df = df3.loc[:, '2006':'2015']
  df['avgGDP'] = df.mean(axis =1, skipna = True) 
  print(df['avgGDP'])
  print(type(df['avgGDP']))



def answer_four():
  df = df3.loc[:, '2006':'2015']
  df['avgGDP'] = df.mean(axis =1, skipna = True)
  df = df.sort_values(by=['avgGDP'], ascending=False)
  c = df.index[5]
  print(c)
  d = (df['2015'].iloc[5])-(df['2006'].iloc[5])
  print(d)

def answer_five():
  mean_energy_supply = df3['Energy Supply per Capita'].mean(axis=0, skipna = True)
  print(mean_energy_supply)


def answer_six():
  df = df3['% Renewable']
  a = df.max()
  print(a)
  b = df3[df3['% Renewable']== df3['% Renewable'].max()]
  response = b.index[0]
  print(response)
  c = (a, response)
  print(c)
# Unable to use idxmax in this question.  


def answer_seven():
  df = df3.copy()
  df['Ratio'] = df['Self-citations']/df['Citations']
  c = (df['Ratio'].idxmax(),df['Ratio'].max())
  print(c)
  

def answer_eight():
  df = df3.copy()
  df['Population'] = df['Energy Supply']/df['Energy Supply per Capita']
  df = df.sort_values(by=['Population'], ascending=False)
  print(df.index[2])
# Unable to use nlargest in this question.



def answer_nine():
  df = df3.copy()
  df['Population'] = df['Energy Supply']/df['Energy Supply per Capita']
  df['Citable Documents per Capita'] = df['Citable documents']/df['Population']
  df['Citable Documents per Capita']=df['Citable Documents per Capita']
  data = df[['Citable Documents per Capita','Energy Supply per Capita']].corr()
  print(data)


def answer_ten():
  df = df3.copy()
  df = df.sort_values(by=['% Renewable'])
  print(df['% Renewable'])
  median = df['% Renewable'].iloc[7]
  print(median)
  a = [] 
  for item in df['% Renewable']:
    if item < median:
      med = 0
    if item >= median:
      med = 1  
    a = a + [med]
  df['Median'] = a  
  df = df.sort_values(by=['Rank'])
  print(df['Median'])     

ContinentDict  = {'China':'Asia', 'United States':'North America', 'Japan':'Asia', 'United Kingdom':'Europe', 'Russian Federation':'Europe', 'Canada':'North America', 'Germany':'Europe','India':'Asia','France':'Europe', 'South Korea':'Asia', 'Italy':'Europe', 'Spain':'Europe', 'Iran':'Asia', 'Australia':'Australia', 'Brazil':'South America'}


def answer_eleven():


answer_ten()









