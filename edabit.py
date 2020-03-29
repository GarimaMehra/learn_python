def eof(x):
  i=1
  response = 'even'
  while(i<= x/2):
    if(i*i == x):
      response = 'odd'
      break
    i=i+1
  print (response) 


def eof2(x):
  i=1
  count=0
  while(i <= x):
    if( x % i == 0):
      count = count+1
    i=i+1

  if (count%2 != 0):
    print('odd')
  else:
    print('even')


def reverse(arg):
  response = 'boolean expected'
  if (arg == 'true'):
	  response = 'false'
  if (arg == 'false'):
	  response = 'true'
  print (response)  


def sum(x):
  i=1
  j=0
  while (i<=x):
    j= j+i
    i= i+1
  print(j)  


def a_b_c(a,b,c):
  i=1
  j=a
  while(i<=b):
    j = j*2
    i=i+1
  if (j%c == 0):
    print ('true')
  else:
    print ('false')  



def evennum(x):
  i=1
  j=1
  while (i <= x/2):
    j=i*2
    print (j)
    i=i+1



     

'''  
'''