import conditionsAndLoops as c
import github_ex as g
import variablesConstantsScope as v1
import edabit as e
import functionsAndTheirScope as f
import BooleansAndString as b
import NoneInPython as n
import ListPython as l
import dictionary_example as d
import anki_ques as a
import todo as t
import classesAndGarbageCollection as cl
#import dataScience.week1.csv as dsc
#from dataScience.week1 import lambda_examples as dsl, numpy_examples as dsn
#import dataScience.week1.list_comprehensions as dslc
#from dataScience import rough_work as dsr
from dataScience.week2 import pandas_examples as ds2p

ankitNew = "different variable"

#red = 'red'


#start = 3
#end = 5

#def Print_num():
    #for x in range( start, end + 1 ): #range(1,11)
     # print(x)

#Print_num()
#i= 'ankita'
#j= 'bishta'
#def fname(i,j):
 # print(i  + ' ' + j + ' account is blocked')
#fname( "ankit" , "bisht")
#'fname()+ account is blocked'
#def isPrimeum(num):
  #countFactor=0
  #if num==1:
   # countFactor=0
  #else:
    #for i in range(2,num):
     # if (num%i==0):
        #countFactor=countFactor+1
  #if(countFactor > 0):
    #print('Number is not prime')
    #return False
  #else:
   # print('Number is prime') 
    #return True 
  #+
 #print('No. of factors is %d' %countFactor)   

def fact(num):
  if num<0:
    j=0
  else:
    if num==0:
       j=1
    else:
       j=1
       for i in range(1,num+1):
         j=j*i
  return j 


def sodV2(num):
  multiplier = 1
  b=0
  if num < 0:
    num = num * -1
    multiplier = -1
  while num > 0:
    a = num % 10
    num=(num-a)/10
    b = b + a
  return b * multiplier

def sodV1(num):
  if num<10:
    return num
  else:
    b=0
    while num > 10: 
      a=num%10
      num=(num-a)/10
      b=b+a
      if num<10:
        j=b+num
  return j

"""
Comments or rough work: 
num 123, 12, 1, 0
i 0, 1, 2, 3
a 3, 2, 1
b 0, 3, 5, 6

num 123, 12, 1
i 0, 1, 2
a 3, 2
b 0, 3, 5
j 6
"""


def dod(num):
  if num<10:
    return num
  else:
    i=10
    b=0
    x=0
    for i in range(i,num): 
      x=x+1
      a=num%10
      num=(num-a)/10
      b=b+(((-1)**x)*a)
      if num<10:
        j=b+num
      else:
        i=i*10

  return j  



def lst(x):
  for i in x:
    print(i)  
  j = 0
  while (j < len(x)):
    print(x[j]) 
    j = j+1 




