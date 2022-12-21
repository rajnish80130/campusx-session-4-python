# Lists
# What are Lists?
# Lists Vs Arrays
# Characterstics of a List
# How to create a list
# Access items from a List
# Editing items in a List
# Deleting items from a List
# Operations on Lists
# Functions on Lists

#Lists--->List is a data type where you can store multiple items under 1 name.
# More technically, lists act like dynamic arrays which means you can add more items on the fly.

# L = [20,'raj',True,40.54]

#************ Array Vs Lists************
# Fixed Vs Dynamic Size
# Convenience -> Hetrogeneous
# Speed of Execution ---> Array have more
# Memory ---> Lists take more memory 

'''L = [1,2,3]

print(id(L))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))
print(id(1))
print(id(2))
print(id(3))  #id function tell you where your code are store

#************* Characterstics of a List***************
# Ordered
# Changeble/Mutable
# Hetrogeneous
# Can have duplicates
# are dynamic
# can be nested
# items can be accessed
# can contain any kind of objects in python

# ordered
L = [1,2,3]
L1 = [3,2,1]

print(L == L1)

#**************creating a list**********
# Empty
print([])
# 1D -> Homo
print([1,2,3,4,5])
# 2D --> two lists
print([1,2,3,[4,5]])
# 3D
print([[[1,2],[3,4]],[[5,6],[7,8]]])
# Hetrogenous
print([1,True,5.6,5+6j,'Hello'])
# Using Type conversion
print(list('hello'))

#************Accessing Items from a List***********

# Indexing
L1=[1,2,'raj']
print(L1[2])

L = [[[1,2],[3,4]],[[5,6],[7,8]]]
#positive
print(L[0][0][1])

# Slicing
L = [1,2,3,4,5,6]

print(L[::-1])

# ***********Adding Items to a List************
# append ----> append add one element
L = [1,2,3,4,5]
L.append(True)
print(L)

# extend ----> add more than one element
L = [1,2,3,4,5]
L.extend([6,7,8])
print(L)

L = [1,2,3,4,5]
L.append([6,7,8])
print(L)

L = [1,2,3,4,5]
L.extend('delhi')
print(L)

# insert  --> insert take two argument one is index and other is number
L = [1,2,3,4,5]

L.insert(4,100)
print(L)

#**************Editing items in a List*********

L = [1,2,3,4,5]

# editing with indexing
L[-3] = 500
print(L)
# editing with slicing
L[0:2] = [300,400]

print(L)

#**************Deleting items in a List*********
# del Function
L = [1,2,3,4,5]

# indexing
del L[-1]

# slicing
del L[1:3]
print(L)

# remove Function

L = [1,2,3,4,5]

L.remove(5)

print(L)
# pop Function
L = [1,2,3,4,5]

L.pop(1)   #you cannot give the index no if not index no then delete last element

print(L)

# clear function ---> delete all the in of list
L = [1,2,3,4,5]

L.clear()

print(L)

# ****************Operations on Lists**********
# Arithmetic (+ ,*)

L1 = [1,2,3,4]
L2 = [5,6,7,8]

# Concatenation/Merge
print(L1 + L2)

print(L1*3)
# Membership
L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]

print(5 not in L1)
print([5,6] in L2)
# Loops
L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]
L3 = [[[1,2],[3,4]],[[5,6],[7,8]]]

for i in L1:
  print(i)

for i in L3:
  print(i)

#**************Lists Function********
# len
L = [2,1,5,7,0]

print(len(L))

#min
print(min(L))

#max
print(max(L))

#sorted
print(sorted(L))   #---->ascending order
print(sorted(L,reverse=True)) #--->desending order

# count 
L = [1,2,1,3,4,1,5]
print(L.count(5))

# index
L = [1,2,1,3,4,1,5]
print(L.index(1))

# reverse
L = [2,1,5,7,0]
# permanently reverses the list
L.reverse()
print(L)

# sort (vs sorted)
L = [2,1,5,7,0]
print(L)
print(sorted(L))
print(L)
L.sort()  #----> sort the list permanentely
print(L)

# copy -> shallow
L = [2,1,5,7,0]
print(L)
print(id(L))
L1 = L.copy() #---> copy function create a duplicate list
print(L1)
print(id(L1))

# List Comprehension
# List Comprehension provides a concise way of creating lists.

# newlist = [expression for item in iterable if condition == True]

# Advantages of List Comprehension

# More time-efficient and space-efficient than loops.
# Require fewer lines of code.
# Transforms iterative statement into a formula.

# Add 1 to 10 numbers to a list
L = []

for i in range(1,11):
  L.append(i)

print(L)

#from list comprehension

L = [i for i in range(1,11)]
print(L)

# scalar multiplication on a vector
v = [2,3,4]
s = -3
# [-6,-9,-12]

print([s*i for i in v])

# Add squares
L = [1,2,3,4,5]

print([i**2 for i in L])

# Print all numbers divisible by 5 in the range of 1 to 50

print([i for i in range(1,51) if i%5 == 0])

# find languages which start with letter p
languages = ['java','python','php','c','javascript']

print([language for language in languages if language.startswith('p')])

# Nested if with List Comprehension
basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','grapes','banana']

# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'

print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')])

# Print a (3,3) matrix using list comprehension -> Nested List comprehension
print([[i*j for i in range(1,4)] for j in range(1,4)])

# cartesian products -> List comprehension on 2 lists together
L1 = [1,2,3,4]
L2 = [5,6,7,8]

[i*j for i in L1 for j in L2]

#************2 ways to traverse a list************
# itemwise
# indexwise

# itemwise
L = [1,2,3,4]

for i in L:
  print(i)

# indexwise
L = [1,2,3,4]

for i in range(0,len(L)):
  print(L[i])
#*****************Zip Function**************

# The zip() function returns a zip object, which is an iterator of tuples 
# where the first item in each passed iterator is paired together,
#  and then the second item in each passed iterator are paired together.

# If the passed iterators have different lengths, the iterator with the least 
# items decides the length of the new iterator.

# Write a program to add items of 2 lists indexwise

L1 = [1,2,3,4]
L2 = [-1,-2,-3,-4]

print(list(zip(L1,L2))) 

print([i+j for i,j in zip(L1,L2)])

L = [1,2,print,type,input]

print(L)
#*************Disadvantages of Python Lists***************
# Slow
# Risky usage
# eats up more memory

a = [1,2,3]
b = a.copy()

print(a)
print(b)

a.append(4)
print(a)
print(b)

# lists are mutable

# Create 2 lists from a given list where 
# 1st list will contain all the odd numbers from the original list and
# the 2nd one will contain all the even numbers 

L = [1,2,3,4,5,6]
even = []
odd = []

for i in L:
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)

print(even)
print(odd)'''