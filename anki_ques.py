
def max_min_no(x):
  i = 0
  while (i < len(x)-1):
    j = 1
    while (j < len(x)-i):
      y = []
      if ((x[i] < x[i+j]) == True):
        y = y + [x[i]]
      else:
        y = y + [x[i+j]]  
      if (x[i] > y[0]):
        a = x[i]
        x[i] = x[i+j]
        x[i+j] = a  
      j = j + 1            
    i = i + 1  
  print(x)  
     


def swapp(x):
  a = [x[0], x[len(x)-1]]
  x[0] = a[1]
  x[len(x)-1] = a[0]
  print(x)

def swap(x,y):
  return y,x
  

def swapp2(x):
  x[0], x[len(x)-1] = swap(x[0], x[len(x)-1])
  print(x)

"""new problem
A function takes list x as an argument and returns a list y such that y is same as list x except first element of list y is sum of first and last element of list x
However, use below function named sumCustom in implementing this function. Do not modify sumCustom function. This function adds two number.

example [ 1, 2, 3, 5] => [ 6, 2, 3, 5]

"""

def sumCustom( a, b):
  return a + b

def add_first_num(x):
    x[0] = sumCustom(x[0], x[len(x)-1]) 
    print(x)


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
  