def types(num):
  response = "" 
  if (num<0):
    response = 'negative'
  elif (1<=num<10):
    response = 'child'
  elif (10<= num <=20):
    response = 'teen age'
  elif (num>20):
    response= "adult"
  return response  


def odd_even(num):
  message = ""
  if num%2 !=0:
    message = "odd number"
  elif num%2 == 0:# redundant here
    message = "even number"  
  print(message)

def odd_even_age(num):
  message = ""
  message1 = ""
  if num%2 !=0:
    message = "odd number"
  else:
    message = "even number"

  if (num<0):
    message1 = 'negative'
  elif (1<=num<10):
    message1 = 'child'
  elif (10<= num <=20):
    message1 = 'teen age'
  elif (num>20):
    message1= "adult" 
     
  print(message) 
  print(message1)   


def quadrant(x,y):
  message = "origin"
  if (x>0) and (y>0):
    message = 'Top right' 
  elif (x<0) and (y>0):
    message = 'Top left'
  elif (x<0) and (y<0):
    message = 'Bottom left'
  elif (x>0) and (y<0):
    message = 'Bottom right' 
  print(message)
  #return message

#print(quadrant(0,0))

def quadrantV2(x,y):
  message = "origin"
  if (x>0):
    if(y>0):
      message = 'Top right'
    else:
      message = 'bottom right'
  else:
    if(y>0):
      message = 'Top left'
    else:
      message = 'bottom left'
  print(message)     

def x_y(x,y):  
  """
  Description:
  x, y, z
  any(x, y) +ve => positive
  both(x, y) -ve=> negative
  baki kuch bhi ho = >"invalid input arguments"
  """
  message = 'invalid'
  if (x<0) and (y<0):
    message = 'negative'
  if (x>0) or (y>0):
    message = 'positive'
  return message 
  
def x_y_z(x,y,z):
  """
  Description:
  x, y, z
  any(x, y) +ve aur z +ve => positive
  both(x, y) -ve ya z -ve => negative
  baki kuch bhi ho => invalid input arguments
  """
  message = 'null'
  if (x>0 or y>0) and z>0:
    message = 'positive'
  if (x<0 and y<0) or z<0:
    message =  'negative'
  return message  



"""
Rough work:
string arguments => 
red => blue
white => black
yellow => green
brown => pink
other string => vibgyor
"""

def color(inputColor):
  message = 'vibgyor'
  if (inputColor == 'red'):
    message = 'blue'
  if (inputColor == 'white'):
    message = 'black'  
  if (inputColor == 'yellow'):
    message = 'green'
  if (inputColor == 'brown'):
    message = 'pink' 
  return message 


def whileloop(x,y):
  while x<y:
    if (x%2 != 0):
      print(x)
    x=x+1



def rev_num(x,y):
  z=x
  while (x<y+1): 
    print(x)
    x=x+1 
  while (z<y+1): 
    print(y)
    y=y-1  

 
  
def rev_num2(x,y):
  i=x
  j=y
  while (x<y+1) or (i<j+1):
    if(x < y + 1):# kagaz mein draw kar ke socho ya woh variables ki values rakh k debug karo
      print(x)
      x = x + 1
    else:
      print(j)
      j = j - 1
    
    
'''
5

1
1 3
1 3 5
1 3 5 7
1 3 5 7 9
'''

def py(x):
  i = 1
  while (i < x+1):
    j = 1
    value = 1
    while( j < i+1 ):
      print( value,  end = " ")
      value += 2
      j += 1
    print("")
    i+=1

"""

4
1,1 1,2 1,3 1,4
2,1 2,2 2,3 2,4
3,1 3,2 3,3 3,4
4,1 4,2 4,3 4,4
"""   


def matrix(x):
  i = 1
  while (i < x+1):
    j = 1
    while( j < x+1 ):
      print( str(i) + "," + str(j),  end = "  ")
      j += 1
    print("")
    i+=1


"""

4, 6
1,1 1,2 1,3 1,4 1,5 1,6
2,1 2,2 2,3 2,4 2,5 2,6
3,1 3,2 3,3 3,4 3,5 3,6
4,1 4,2 4,3 4,4 4,5 4,6
"""
def matrix2(x,y):
  i = 1
  while (i < x+1):
    j = 1
    while( j < y+1 ):
      print( str(i) + "," + str(j),  end = "  ")
      j += 1
    print("")
    i+=1

"""
2,3
0,0 0,1 0,2
1,0 1,1 1,2
"""

def matrix3(x,y):
  i = 0
  while (i< x):
    j = 0
    while( j< y):
      print( str(i) + "," + str(j),  end = "  ")
      j += 1
    print("")
    i+=1


"""
2,3 (sum=2)

0,0 0,1 0,2
1,0 1,1 1,2
inme se jinka sum 2

0,2 1,1

"""

def matrix4(x,y,Sum):
  i=0
  while (i<x):
    j=0
    while (j<y):
      if (i+j == Sum):
        print (str(i) + ","+ str(j), end = " ")
      j=j+1 
    print("")   
    i=i+1


"""
2,2,3

0,0,0  0,0,1  0,0,2
0,1,0  0,1,1  0,1,2

1,0,0  1,0,1  1,0,2
1,1,0  1,1,1  1,1,2
"""

def matrix5(x,y,z):
  i=0
  while (i<x):
    j=0
    while (j<y):
      k=0
      while (k<z):
        print (str(i) + ","+ str(j) + "," + str(k), end = " ")
        k=k+1
      print('')  
      j=j+1 
    print("")   
    i=i+1

def star(x):
  i=1
  while (i<x+1):
    j=1
    while (j<i+1):
      print("*", end = " ")
      j=j+1
    print("")
    i=i+1


def star2(x):
  y=2*x-1
  i=1
  while (i<x+1):
    j=1
    while (j<y+1):
      if(j==x) or ():
       print("*", end = " ")
      j=j+1
    print("")
    i=i+1