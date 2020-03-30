 
"""
Boolean or Bool is a type a constants( e.g integer, float).
it has only 2 values. True with captial T. And, False with capital F.
"""
def booleanUse(x):#call like booleanUse(False)
  y = True# example of varible assingment by boolean
  print(y)

  if x:# example of using boolean DIRECTLY as condition. Same as x == True condition below
    print('true string')
  else:
    print('false string')

  if x == True:# example of using boolean INDIRECTLY as condition
    print('true string again')
  else:
    print('false string again')

"""
string is a type of constant in python
defined inside single or double quotes
stringVariable = 'Hello world'
string is created using individual characters like above string has first character as 'H'
"""

def stringOperations(x):
  #prints all character of string
  for i in x:
    print(i)
  
  #length of string
  print(len(x))

  #accessing a character in string using square brackets [], string is a array of characters and its first character is at 0 and last at length - 1
  print(x[0])#first character
  print(x[ len(x) - 1])#last character

  #square brackets can also be used to print all characters in string as following
  #"IndexError: string index out of range" if you access a charcter a location more than string length
  j = 0
  while j < len(x):
    print(x[j])
    j+=1
  
  # concatenation two or more strings using + operator
  print( x + " garima")
  print( x + " garima" +" mehra")

  # more operations on sting can be found at https://www.w3schools.com/python/python_strings.asp



def char_k(x,y):
  if (x[y-1] == 'k'):
    return True
  else:
    return False  


def start_end(x,y):
  if (x[y-1] == x[-y]):
    return True
  else:
    return False  


def rev_string(x):
  i = 0
  while (i < len(x)):
    print(x[-(i+1)])
    i=i+1


def rev_string2(x):
    i = 0
    for i in len(x):
      return (x[-(i+1)])


def palindrome(x):
  response ='False'
  i=0
  count=0
  while (i < len(x)/2):
    if (x[i] == x[-(i+1)]):
      count=count+1
    i=i+1
  if ( (len(x)%2 == 0) and (count == len(x)/2) ) or ( (len(x)%2!= 0) and (count== (len(x)+1)/2) ):
    response ='True'
  print(response)  


def palindrome_v2(x):
  response = 'True'
  i=0
  while (i < len(x)/2):
    if(x[i] != x[-(i+1)]):
      response = 'False' 
      break 
    i=i+1
  print(response)   


def palindrome_v3(x):
  i=0
  response= 'True'
  while (i < len(x)):
    if x[i] != rev_string(x[i]):
      response = 'False'
    i=i+1  
  print(response)      


  




      
