"""
Variables save data.
Functions and classes save logic

you need return from a fucntion to assign a value to a varible
example:
aVariable = returnFunc('king')

now aVariable wil have 'king' string as value
but 

bVariable = printFunc('king')
bVariable will not have 'king' value assigned as printFunc function does not returns any value
"""

def returnFunc(a):
  return a


def printFunc(a):
  print(a)


"""
scope a function is same as scope of global variable
"""

"""
A function can be called from another function. If second function a return value than that value will be used as argument for the function calling the second funtion

addition( callee(), callee1())

is same as

i = callee()
j = callee1()
addition( i,j)

example: print( addition( callee(), callee1() ) )
"""
def callee():
  return 2

def callee1():
  return 3


def addition(a, b):
  return a + b


"""
you can chain function calls
function A can call function B which can call Function C and so on
example: print(A())
will print 'Hello World'
For chaining all functions should have return.
example: print( ADash()) will not print anything cause BDash function do not have a retrun

"""





def D():
  return "Hello World"


def C():
  return D()


def B():
  return C()


def A():
  return B()


def BDash():
  C()# no return of value from here


def ADash():
  return BDash()

"""
write a function which prints "divisible by 7" if it is divisible by 7 else if it has odd number of factors it prints "odd" else if it has even number of factors it prints "even"
"""

def func7(y):
  i=1
  if(y%7 == 0):
    print('divisible by 7')  
  a= even_odd_factor(y)
  #if ( even_odd_factor(y) == True ):
  if (a== True):
    print('even')
  else:
    print('odd')  
        
        
def even_odd_factor(x):
  hasEvenFactors = True
  i=1
  while (i<=x/2):
    if (i*i == x):
      hasEvenFactors= False
      break
    i=i+1 
  return hasEvenFactors 



