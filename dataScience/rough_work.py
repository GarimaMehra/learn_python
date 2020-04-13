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