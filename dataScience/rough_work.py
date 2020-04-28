import numpy as np
import pandas as pd

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

# aa45

def giveAllIds():
  allIds = []
  for i in lowercase:
    for j in lowercase:
      for k in digits:
        for l in digits:
          #allIds.append( i + j + k + l)
          allIds.append( "{}{}{}{}".format(i, j , k, l) )
  return allIds

def giveAllIdsV2():#list_comprehension used
  return list( "{}{}{}{}".format(i, j , k, l) for i in lowercase for j in lowercase for k in digits for l in digits) 

#print( (lambda : list( (i + j + k + l) for i in lowercase for j in lowercase for k in digits for l in digits))() )

def mergeDfByIndex():
  df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz'],'value': [1, 2, 3]},  index=['a', 'b', 'c'])
  df2 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz'],'value': [1, 2, 3]},  index=['c', 'd', 'e'])
  m1 = pd.merge(df1,df2,how="outer",left_index=True, right_index=True)
  df3 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz'],'value': [1, 2, 3]},  index=['a', 'x', 'e'])
  m2 = pd.merge(m1,df3,how="outer",left_index=True, right_index=True)
  print(m2.head(100))


#mergeDfByIndex()