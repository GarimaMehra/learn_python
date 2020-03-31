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


def first_letter(x):
  y=''
  for i in sorted(x):
    a = i[0]#check listPython file code to know how to loop. this is wrong way to loop through a list..ok.
    y= y+ a 
  print(y)

def amplify(x):
  i=1
  a=[]
  while (i <= x):
    j=i 
    if (i%4 == 0):
      j= 10*j
    a = a + [j]
    i=i+1
  print (a)


def filter_num(x):
  a=[]
  i= 0
  while (i < len(x)):
    j= type(x[i]) 
    if j == int:
      a=a+[x[i]]
    i=i+1 
  print (a)   


def find_even_num(x):
  a= []
  i=1
  while (i<=x/2):
    j= 2*i
    a=a+[j]
    i=i+1
  print (a)  

   
def unique_sort(x):
  a = sorted(x)
  print(a)
  y = []
  i=0
  while (i < len(a)-1):
    y = y+ [a[i]]
    if (a[i] == a[i+1]):
      y.remove(a[i+1])   
    i=i+1 
  y=y+[a[i]]  
  print(y)  
  

def unique_sort2(x):
  a = sorted(x)
  print(a)
  y = []
  i=0
  while (i < len(a)-1):
    if (a[i] != a[i+1]):
      y = y+ [a[i]]   
    i=i+1   
  y= y + [a[i]]  
  print(y)


def nth_smallest(list1,x):
  if (x>len(list1)):
    print ("None") # why return is not working here.
  else:
    a = sorted(list1)
    print (a[x-1])


def sum_of_evens(x):
  i = 0
  y = 0
  while (i < len(x)):
    j = 0
    while(j < len(x[i])):
      a=x[i]
      if ((a[j] % 2) == 0):
        y = y + a[j]
      j=j+1  
    i=i+1
  print(y)  



