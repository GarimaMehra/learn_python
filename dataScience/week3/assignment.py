import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)



def answer_one():
  energy = pd.read_excel('dataScience/week3/Energy Indicators.xls')
  energy = energy[17: 244]
  energy.drop(energy.columns[[0,1]], axis = 1, inplace = True)
  energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
  energy = energy.replace('...',np.NaN)
  energy['Energy Supply'] = energy['Energy Supply']*1000000
  energy['Country'] = energy['Country'].str.replace('\d+', '')
  energy['Country'] = energy['Country'].str.replace(r"\s*\([^()]*\)","").str.strip()
  energy['Country'] = energy['Country'].replace({"Republic of Korea": "South Korea", "United States of America": "United States", "United Kingdom of Great Britain and Northern Ireland": "United Kingdom", "China, Hong Kong Special Administrative Region": "Hong Kong"})
  energy=energy.set_index('Country')

  GDP = pd.read_csv('dataScience/week3/world_bank.csv', skiprows = 4)
  GDP['Country Name'] = GDP['Country Name'].replace({'Korea, Rep.': 'South Korea', 'Iran, Islamic Rep.':'Iran', 'Hong Kong SAR, China': 'Hong Kong'})
  GDP= GDP.rename(columns={'Country Name': 'Country'})
  GDP = GDP.set_index('Country')
  GDP = GDP.loc[:, '2006':'2015']


  ScimEn = pd.read_excel('dataScience/week3/scimagojr-3.xlsx')
  ScimEn = ScimEn.set_index('Country')

  df1 = pd.merge(ScimEn, energy, how = 'inner', left_index = True, right_index =True)
  df2 = pd.merge(df1, GDP, how ='inner',left_index = True, right_index = True)
  response = df2[:15]
  return response

def answer_two():
  energy = pd.read_excel('dataScience/week3/Energy Indicators.xls')
  energy = energy[17: 244]
  energy.drop(energy.columns[[0,1]], axis = 1, inplace = True)
  energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
  energy['Energy Supply'] = energy['Energy Supply']*1000000
  energy.replace('...',np.NaN)
  energy['Country'] = energy['Country'].str.replace('\d+', '')
  energy['Country'] = energy['Country'].str.replace(r"\s*\([^()]*\)","").str.strip()
  energy['Country'] = energy['Country'].replace({"Republic of Korea": "South Korea", "United States of America": "United States", "United Kingdom of Great Britain and Northern Ireland": "United Kingdom", "China, Hong Kong Special Administrative Region": "Hong Kong"})
  energy=energy.set_index('Country')
  
  GDP = pd.read_csv('dataScience/week3/world_bank.csv', skiprows = 4)
  GDP['Country Name'] = GDP['Country Name'].replace({'Korea, Rep.': 'South Korea', 'Iran, Islamic Rep.':'Iran', 'Hong Kong SAR, China': 'Hong Kong'})
  GDP= GDP.rename(columns={'Country Name': 'Country'})
  GDP = GDP.set_index('Country')
  GDP = GDP.loc[:, '2006':'2015']


  ScimEn = pd.read_excel('dataScience/week3/scimagojr-3.xlsx')
  ScimEn = ScimEn.set_index('Country')


  df1 = pd.merge(ScimEn, energy, how = 'inner', left_index = True, right_index =True)
  df2 = pd.merge(df1, GDP, how ='inner',left_index = True, right_index = True)
  
  
  df3 = pd.merge(ScimEn, energy, how = 'outer', left_index = True, right_index =True)
  df4 = pd.merge(df3, GDP, how ='outer',left_index = True, right_index = True)
  response = len(df4)-len(df2)
  return response

def answer_three():
  Top15 = answer_one()
  df = Top15.loc[:, '2006':'2015']
  df['avgGDP'] = df.mean(axis =1, skipna = True) 
  df = df.sort_values(by=['avgGDP'], ascending=False)
  return df['avgGDP']


def answer_four():
  Top15 = answer_one()
  df = Top15.loc[:, '2006':'2015']
  df['avgGDP'] = df.mean(axis =1, skipna = True)
  df = df.sort_values(by=['avgGDP'], ascending=False)
  value = (df['2015'].iloc[5])-(df['2006'].iloc[5])
  return float(value)


def answer_five():
  Top15 = answer_one()
  mean_energy_supply = Top15['Energy Supply per Capita'].mean(axis = 0)
  return float(mean_energy_supply)


def answer_six():
  Top15 = answer_one()
  df = Top15['% Renewable']
  Max_renew = df.max()
  response = Top15[Top15['% Renewable']== Top15['% Renewable'].max()]
  Max_country = response.index[0]
  return (Max_country, float(Max_renew))
  

def answer_seven():
  Top15 = answer_one()
  Top15['Ratio'] = Top15['Self-citations']/Top15['Citations']
  response = (str(Top15['Ratio'].idxmax()),float(Top15['Ratio'].max()))
  return response


def answer_eight():
  Top15 = answer_one()
  Top15['Population'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
  Top15 = Top15.sort_values(by=['Population'], ascending=False)
  response = Top15.index[2]
  return response


def answer_nine():
  Top15 = answer_one()
  Top15['Population'] = pd.to_numeric(Top15['Energy Supply']/Top15['Energy Supply per Capita'])
  Top15['Citable Documents per Capita'] = pd.to_numeric(Top15['Citable documents']/Top15['Population'])
  data = Top15[['Citable Documents per Capita','Energy Supply per Capita']]
  data = data.astype({'Energy Supply per Capita': 'float'}, copy = False)
  #print(data.dtypes)
  data = data['Citable Documents per Capita'].corr(data['Energy Supply per Capita'])
  return float(data)

def answer_ten():
  Top15 = answer_one()
  median = Top15['% Renewable'].median()
  a = [] 
  for item in Top15['% Renewable']:
    if item < median:
      med = 0
    if item >= median:
      med = 1  
    a = a + [med]
  Top15['HighRenew'] = a  
  return Top15['HighRenew'] 


def answer_eleven():
  Top15 = answer_one()
  Top15['Continent'] = pd.Series({'China':'Asia', 'United States':'North America', 'Japan':'Asia', 'United Kingdom':'Europe', 'Russian Federation':'Europe', 'Canada':'North America', 'Germany':'Europe','India':'Asia','France':'Europe', 'South Korea':'Asia', 'Italy':'Europe', 'Spain':'Europe', 'Iran':'Asia', 'Australia':'Australia', 'Brazil':'South America'})
  Top15 = Top15.reset_index()
  Top15['Population'] = pd.to_numeric (Top15['Energy Supply']/Top15['Energy Supply per Capita'])
  response = Top15.set_index('Continent').groupby(level=0)['Population'].agg([np.size, np.sum, np.mean, np.std])
  return response
  

def answer_twelve():
  Top15 = answer_one()
  Top15['Continent'] = pd.Series({'China':'Asia', 'United States':'North America', 'Japan':'Asia', 'United Kingdom':'Europe', 'Russian Federation':'Europe', 'Canada':'North America', 'Germany':'Europe','India':'Asia','France':'Europe', 'South Korea':'Asia', 'Italy':'Europe', 'Spain':'Europe', 'Iran':'Asia', 'Australia':'Australia', 'Brazil':'South America'})
  Top15['Bins'] = pd.cut(Top15['% Renewable'],5)
  response = Top15.groupby(['Continent','Bins']).size()
  response = response[response > 0].dropna().astype('int64')
  return response

    

def answer_thirteen():
  Top15 = answer_one()
  Top15['Population'] = pd.to_numeric (Top15['Energy Supply']/Top15['Energy Supply per Capita'])
  Top15['PopEst'] = Top15['Population'].apply('{:,}'.format)
  return Top15['PopEst']



