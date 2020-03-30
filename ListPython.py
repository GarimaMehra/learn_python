
"""
array is same as list in python
List is a collection( can contains multiple constants) of elements of same or differnt type. It maintains the order in which element are inserted.
it allows a single variable to store any number of elements.

l = [ 1, 2, "stri", True]
"""

def listOperations(x):#x here should be a list
  list1 = [ 1, 2, "stri", True]# this list has elements of different types
  list2 = [ 1, 2, 3]# this list has all elements of different types
  list3 = [ "a", "b", "c"]# this list has all elements of different types
  list4 = x

  #prints all element of list
  print(list1, list2, list3, list4)
  
  #length of list
  print(len(list1), len(list2), len(list3),len(list4) )

  #accessing a element in list using square brackets [], list is a collection/ array of elements and its first element is at 0 and last at length - 1
  print(list1[0])#first element
  print(list1[ len(list1) - 1])#last element

  #To change the value of a specific item, refer to the index number:(this does not works for a string)
  list4[0] = 'k'
  print(list4)

  #Looping through alist
  #square brackets can also be used to print all elements in list as following
  #"IndexError: list index out of range" if you access a element a location more than list length
  j = 0
  while j < len(list1):
    print(list1[j])
    j+=1
  
  for element in list1:
    print(element)

  #To determine if a specified item is present in a list use the in keyword

  if "stri" in list1:
    print("Yes, 'stri' is in list1")

  #To add an item to the end of the list, use the append() method
  list4.append("orange")
  print(list4) 

  # concatenation two or more lists using + operator
  listNew = list1 + list2
  print( listNew)

  # you can create an empty list too and append elements to it as per need
  listEmpty = []
  listEmpty.append("first element")
  print(listEmpty)

  # read remove(), pop(), insert(), clear(), copy()
  
  # more operations on lists can be found at https://www.w3schools.com/python/python_lists.asp