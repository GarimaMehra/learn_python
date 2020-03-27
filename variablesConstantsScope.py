"""
stdin = standard input
CONSTANT have 3 major type:
integer = 2, 3, 4
float = 3.14, 3.44
string = "ankit", 'computer'

advanced:
array
dictionary
list
"""

2
3
'ankit'
2 + 3
'ank' + "   " + "bis"



"""
VARIABLE
has 2 properties type, value
type example: integer, float, string
value example: 2, 3, 'aaa' 

variables are carrier or alias name of constants. And their properties type and value are based on the constant they store.
"""

ankit = 2
mayank = 2.4
garima = 3
snickers = "4"
ankit + int(snickers)# ankit + snickers is invalid
str(ankit) + snickers
snickers = "world"# ankit + int(snickers) is invalid now as "world" cannot be converted to a integer by calling int() function
snickers = "56"
ankit + int(snickers) 


"""
SCOPE: mean in which files and and which functions given vairiable will exist

2 type of variables:
local 
global
"""
def localScopeExample():
  ankit = 10# i am local
  b = 'hello'# i am local
  c = 2.3 # i am local
  print(ankit, b, c)
  if ( ankit == 10):
    g = 'king'
    print(g)
  print(c, b, ankit)
  print(g)
  



#print(ankit, b, c) # invalid as variable ankit is not in outside scope. It is in scope of function. So, have local scope

#print(g)# invalid as variable g is not in outside scope. It is in scope of function. So, have local scope

# to print ankit, b, c, and g call function localScopeExample() as they are local variable and defined the localScopeExample function. So, only availble in it.

"""
global scope of variable. These variable are available inside a file. They can also be used inside the functions present in the file. But they should be defined before use, other their usage will give an error.

It is best practise to declare all you global variables at the starting of file.

recommneded structure of pyhton file
all import commands
define all variables
then you code
"""
#print(garimaNew) #this will give error as garimaNew varible is not defined till now. but defiend in next line.
garimaNew = "hello world"
ankitNew = "ping pong"
#print(garimaNew) #this will NOT give error as garimaNew varible is NOW defined.

def exampleOfGlobalVariable():
  localVariable = "cricket"
  print(garimaNew)
  print( garimaNew + localVariable)
  print( ankitNew )
  #ankitNew = "not ping pong now"
  print(ankitNew)

#exampleOfGlobalVariable()
# to print garimaNew, ankitNew call function exampleOfGlobalVariable() as they are global variable and avaialable in whole file. So, can be used indie this functionwithout re-defining.

