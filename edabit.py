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



def get_budgets(x):  # learn dictionaries
  i=0
  y=0
  while (i < len(x)):
    a = x[i]
    j = a['budget']
    y = y + j
    i = i + 1 
  print(y)     


def move_to_end(list1,num):
  list1.remove(list1[0])
  list1.append(num)
  print(list1)



def probability(x,num):
  i = 0
  count = 0
  while (i<len(x)):
    if (x[i] >= num):
      count=count+1
    i=i+1
  p = (count*100)/len(x)
  print (p)    


def convert_cartesian(x,y):
  if (len(x) != len(y)):
    print ('Not valid')
  i=0
  z= []
  while (i<len(x)):
    a=[]
    a=a+[x[i]]+[y[i]] 
    z = z + [a]
    i=i+1
  print(z)   


def sort_by_length(x):
  i=0
  c=[]
  while (i < len(x)):
    c = c+[len(x[i])]
    i=i+1
    a= sorted(c)
  print (a)
  j=0
  b=[]
   

    
def greatest_num(x):
  i= 1
  num = x[0]
  while (i < len(x)):
    if (num < x[i]):
      num = x[i]  
    i = i + 1  
  print(num)
  


def circular_shift(lst1,lst2,n):
  i = 0
  while (i < n):
    j = len(lst1)-1
    a = lst1[len(lst1)-1]
    while (j > 0):
      lst1[j] = lst1[j-1]
      j = j-1
    lst1[j]= a  
    i = i + 1
  print(lst1)
  if (lst1 == lst2):
    return True
  else:
    return False

def swap(x,y):
  return y,x


def rearranged_diff(num):
  x = str(num)
  b = sorted(x)
  c = b
  d = ''
  e = ''
  print(c)
  i =0
  while (i < len(c)):
    e = e + c[i]
    i = i + 1
  e = int(e)  
  print(e)
  i = 0
  while (i < len(b)/2):
    b[i], b[-(i+1)] = swap(b[i], b[-(i+1)])
    i = i + 1
  print(b) 
  i = 0
  while (i < len(b)):
    d = d + b[i]
    i = i + 1
  d = int(d)  
  print(d)
  print(d-e) 
    
    
def rearranged_diff_v2(num):
  x = str(num)
  b = sorted(x, reverse = True)
  d = ''
  e = ''
  i = 0
  print(b)
  i=0
  while (i < len(b)):
    d = d + b[i]
    e = e + b[-(i+1)]
    i = i + 1
  d = int(d) 
  e = int(e) 
  print(d)
  print(e)
  print(d-e) 

      
      
def add_str_nums(x,y):#teach exceptions to garima via this todo ankit
  x = int(x)
  y = int(y)
  if (type(x) != int or type(y) != int):
    print('-1')
  else: 
    z = x + y
    print(str(z))


"""
123
+39
___
162   
___
"""


  