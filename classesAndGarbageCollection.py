"""
TODO -> Inheritance in OOPS

Python OOPS syntax -> https://www.w3schools.com/python/python_classes.asp and https://data-flair.training/blogs/python-object/

OOPs understanding ->https://medium.com/@richardeng/a-simple-explanation-of-oop-46a156581214 or https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/ or see some youtube videos

-> object oriented programming(OOPs) paradigm's basic unit is class. 

-> In OOPs every varible points to an object which has a type. And we can interact with those objects using its properties and methods.

-> Every object is created using a blueprint called its class, which defines what will be the properties aka variables and methods aka functions of those objects and class. In OOPS we refer object's or class's variables as properties and object's or class's methods as functions.

-> examples of classes we have been already using is pandas.series, pandas.dataframe, string, list, dict etc.

"""
class myStringClass:
  #mystr = ""
  #mylen = 0
  k = 3
  """
  All classes which have a function called __init__(), will have their __init__ function always executed when the class is being initiated i.e. creating object. like obj1ofMyStringClass = myStringClass("type")
  """
  def __init__(self, estring):#init method is also called constructor of class
    self.mystr = estring
    self.mylen = len(self.mystr)

  """
  The self parameter is a reference to the current object which is calling that function or property in class
  """
  def reverse(self):
    self.mystr = self.mystr[::-1]

  def printAPoem():#can not call it using an object. See line around 122 for more details. an not use self inside it as self has not been defined in argumeny unlike reverse method above.
    print("Johnny Johnny yes papa")

  def __str__(self):# this funtion named __str__ overrides print() behavior when we call print on any object of this class it will call this function internally and return its content to print. thus print function shows this function's return value.
    return "String is: " + self.mystr + ", length is: " + str(self.mylen)


class myCircle:
  pie = 3.14#best practise: avoid defining a property in class like this use approach of defining property in __init__method. Even if your proeprty is a not using a argument value give it a contant value as for property pieWithMorePrecision

  def __init__(self, radius):
    self.radius = radius
    self.pieWithMorePrecision = 3.141516

  """
  retuning self for allowing method chaining in this function. To support chaing of methods in a class plese return self from those methods.
  """
  def increaseRadiusBy(self, inc):
    self.radius+=inc
    return self


  """
  The self parameter is a reference to the current object which is calling that function or property in class
  """
  def getArea(self):
    return self.pie * (self.radius)**2

  #It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
  def getCircumference(callingObject):
    return 2 * callingObject.pie * callingObject.radius

  #overiding print behaviour for this class's object
  def __str__(self):
    return "Circle radius: " + str(self.radius) + " Circle area: " + str(self.getArea())# also calling a class methond using self 



class myMathsOperations:
  #defining __init__ function in a class is not mandatory

  def plus(self, a, b):
    return a + b

  def minus(self, a, b):
    return a - b

  def multiply(self, a, b):
    return a * b

  def divide(self, a, b):
    return a / b



#funtion to show class's demo
def classExamples():
  """
  class is a basic blueprint that defines behavior and data stored in it. 
  """
  print(myStringClass)
  #below method to create object of a class
  obj1ofMyStringClass = myStringClass("type")#class is just a blueprint or can be thought as a type. Individually it does not have any life. like 'list' class do not have a life. To give it life we must create an object using this blueprint aka class.

  #print(mystr)#Scope of methods and variables are as as modules scope. modules are like "import xyz as k". any property(variable) or method(function) defined inside a class can not be used out of it.To use it out of it we need dot(.) operator and 'object' of the class both.

  print(obj1ofMyStringClass)
  print(type(obj1ofMyStringClass))#So, essentially class is the type of that object

  #lets play with list class which comes in python by default
  listObject = list()#create its object. Object is copy of list class. we must make object of a class to use it. So, class id a map to go to paris and object is a trip using that map. Its a building created using that class bluprint. So, class do not have it own like like map an dblueprints. But buildings and trips have a life
  listObject.append(1)
  listObject.append(2)
  listObject.append(3)
  print(listObject)#[1, 2, 3]
  print(type(listObject))#<class 'list'>
  print(listObject.pop())#use dot(.) operators to access class's methods and properties
  print(listObject)#[1, 2]
  """
  examples of classes we have been already using is pandas.series, pandas.dataframe, string, list, dict etc.
  """
  """
  classes are used to store logically same type of functions and data at same place. List list class contains all methods and data used for doing operartion on a list and Pandas.DataFrame class contains all methods needed for DataFrame type in data Science.
  """
  """
  every object created from a class has differnet data. And it is not shared. even thogh they are object of same class type. This allows us to reuse the code for mutiple things/ operations in same program. Like we can use two list to store even numbers and odd number. AS, they do not share data. Like we can have different dataframe loaded in different object of datafram class.
  """
  listObject2 = list([7,8,9])
  print(listObject2)#[7,8,9]
  print(type(listObject2))#<class 'list'>
  print(listObject)#[1,2]
  print(type(listObject))#<class 'list'>

  """
  Class also have methods aka function which can operate on data contained in that class. All such functions and methods should be used using dot operator in front of object of that class.
  """
  listObject2.append(4)
  listObject.append(0)
  print(listObject)#[1,2,0]
  print(listObject2)#[7,8,9,4]
  #print(list.pop())# gives this error "TypeError: descriptor 'pop' of 'list' object needs an argument". Because class do not have its own life. We need its object to use it methods or properties. So next line will work.
  listObject2.pop()

  """
  class ideally should contain data and operation logically related to it only. Like a car class should contain data like speed, model name etc and functions like drive, accelarate. Adding function like readCsv to car class will not make sense. Although we can do it. But not advisable. ReadCsv method should belong to a class like pandas.
  """
  """
  We can write our custom code unit using a class. Here I am writing a class called myStringClass which will be similar to string class of python but will have a function called reverse to revert the string, String class of python does not have reverse function. So, my class is giving additional feature. And as it is a class any one can use it. 
  https://www.w3schools.com/python/python_howto_reverse_string.asp

  Also, print a sting object only print its content. Here I have change that behaviour for myStringClass. Here print() prints its content and its length too. hence giving another extra feature.
  """
  a = myStringClass("ankit")
  b = myStringClass("garima")
  print(a.mystr)
  print(a.mylen)
  print(a.k)
  print(b.mystr)
  print(b.mylen)
  print(b.k)
  a.k = 9
  print(a.k)
  b.k = 9
  print(b.k)#9 this fetches property k of object

  print(myStringClass.k)#3 this fetches property k of CLASS
  #print(myStringClass.mystr)#AttributeError: type object 'myStringClass' has no attribute 'mystr'. As, myStringClass donot have any property named mystr, unlike property k.
  print(a.mystr)#ankit As, mystr property is part of object a as if you see above code it has been defined in __init__ function with self. Read about self and __init__ in class code above.

  print(a)# if __str__ if not present in class it will show <classes.myStringClass object at 0x7f88cf504dc0>. Else it will call __str__ and display value returned by it.
  print(b)

  a.reverse()#calling method of a object
  print(a.mystr)
  print(b.mystr)

  #myStringClass.reverse()#TypeError: reverse() missing 1 required positional argument: 'self' As, reverse takes one argument as self. Whicch is by default the object. Here we are claaing it by class not object, so it is saying missing one argument.

  #a.printAPoem()#TypeError: printAPoem() takes 0 positional arguments but 1 was given. As, printAPoem takes zero argument. Here we called it via the object.So it python called printAPoem with 'a' object as first argument. So error is saying one argument given but not needed any argument.

  myStringClass.printAPoem()#so when you call a class's method using a class object the first argument always to that method become the calling object itself. But, if you call it via className like myStringClass it will not add any extra argument, unlike calling by object

  c1 = myCircle(2)
  print(c1.increaseRadiusBy(1).getArea(), end="next line")#method chaining
  c2 = myCircle(3)
  print(c1.getArea())
  print(c2.getArea())
  print(c1.getCircumference())
  print(c2.getCircumference())
  print(c1)
  print(type(c1))
  print(c2)
  print(type(c2))

  mo1 = myMathsOperations()#as no init has been defined
  mo2 = myMathsOperations()
  print(mo1.plus(2,13))
  print(mo1.minus(20,13))
  print(mo1.multiply(20,13))
  print(mo1.divide(26,13))

  print(mo2.plus(20,13))
  print(mo2.minus(200,13))
  print(mo2.multiply(200,13))
  print(mo2.divide(260,13))


  print(type(mo1))

  #read about destructors in Python https://www.geeksforgeeks.org/destructors-in-python/ low priority topic

  # read about garbage collection in python https://www.tutorialspoint.com/How-does-garbage-collection-work-in-Python. Python has an automatic grabage colector which uses unused variables and object when not in use to reclaim memory as every object and varibale uses memory.


#classExamples()#remove the comment here


