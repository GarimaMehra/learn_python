def get_student_names(x):
  a=[]
  for i in x:
    a = a + [x[i]]
    b= sorted(a, reverse= True)
  print(sorted(a))
  print(b)      


def dict_example(thisdict):      
  thisdict =	[{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }, {"brand": "Maruti",
  "model": "Mustang",
  "year": 1964}]
  i=0
  while (i< len(thisdict)):
    for k in thisdict[i].values():
  	  print(k)
    i=i+1


def unique_sort(x):
  i = 0
  a =sorted(x)
  b = []
  while (i < len(a)-1):
    if (a[i] != a[i+1]):
      b = b + [a[i]]
    i = i+1
  b = b+ [a[i-1]]  
  print(b)    


def matrix(x,y,z):
  a = []
  i=0
  while (i < x):
    b = []
    j = 0
    while (j < y):
      b = b + [z]
      j = j + 1
    a = a + [b]
    i = i + 1  
  print(a)  


def count_all(x):
  count_int = 0
  count_letter = 0
  i = 0
  while (i < len(x)):
    if (x[i].isdigit() == True): 
      count_int = count_int + 1
    if ((x[i]).isdigit() == False):
      count_letter = count_letter + 1
    if (x[i] == ' '):
      count_letter = count_letter - 1 
    i = i + 1 
  print(count_letter)
  print(count_int)


def find_occurrences(x,y):
  a = {}
  i = 0
  b = ""
  while (i < len(x)):
    b = b + x[i]
    if (x[i] == " "):
      j = 0
      count = 0
      while ( j < len(b)):
        if (b[j] == y):
          count = count + 1
        j = j + 1  
      a[b] = count
    i = i + 1
  print(a)
     



