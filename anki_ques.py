
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

def swap(x,y,z) #y,z are elements of x
  i = 0
  while (i < len(x)):
    a = [y,z]
    if (x[i] == y)
    
    x[i] 
  a = [y,z]
  y = a[1]
  z = a[0]
  return x


def swapp2(x):
  return swap(x, x[0], x[len(x)-1])
