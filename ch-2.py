#(L - 2) Introduction to Data Structures:

#1. What are Data Structures?
#-> (The basic Python data structures in Python include list, set, tuples, and dictionary.Each of the data structures is unique in its own way. Data structures are “containers” that organize and group data according to type. The data structures differ based on mutability and order.)
# ---------------------------------------------------------------

#2. Divisionds of Data Structures:
#->                 Data Stuctures

#Linear D.S (                              Non-Linear D.S (
# Array                                      Binary Tree
# Linked List                                Heap                
# Stack                                      Hash Table
# Queue                                      Graphs.)
# Matrix.)
# ---------------------------------------------------------------

#3.   Data Structures Specific to Python:
#->. These Data Structures are specific to Python language and they give greater flexibility in storing the different types of data and faster proccessing in Python Enviorment.

#*. Python Specific Data Structures.

# list
# tuple
# Dictionary
# set

#*. Python can be divided into two type of Data Structures.
                  #Data Structure

#Built-in-D.S ;                           User-defined-D.S;
# List                                    Stack
# Dictionary                              Queue
# Tuple                                   Tree
# Set                                     Lincked List
#                                         Graph
#----------------------------------------------------------------

#4. Lists in Python:
#Ans - Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# List can be run in Square brackets. Lists can contain Strings as wll as Numbers also.
# The elements within the Lists are seprated by Commas and enclosed within the Square brackets.Lists are mutable.
# ---------------------------------------------------------------

#5. Implementing Lists in Python:
#list = []
#print(list)

#list = [1,2,3,4]
#print(list)

#list = [1,2,3,"Hey",4]
#print(list)

#list = ["you", "can", "do", "it"]
#print(list)

#* Nested Lists(List inside list)
#list = [["hey","good"],['good-morning']]
#print(list)

#* To chech the Size of the list(by using *len()* method):
#list1 = []
#print(len(list1))

#list2 = [1,2,3,4]
#print(len(list2))

#list3 = ["hey", "there"]
#print(len(list3))

#list4 = [1,2,3,4,5,"hey"]
#print(len(list4))
#---------------------------------------------------------------

#6. Tuples in Python:
#1* What is Tuple?
#- Tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable.

#tuple1 = (1, '3', 2, 4)
#print(type(tuple1))

#my_tuple = (1,)
#type(my_tuple)

#tuple3 = ('hey',2 ,5, 3, 'hey')
#print(tuple3)

#---------------------------------------------------------------

#7. Properties of Tuple:
#- Tuple items are ordered, unchangeable, and allow duplicate values. Tuple items are indexed, the first item has index [0] , the second item has index [1] etc.

#---------------------------------------------------------------

#8. Maps in Python:
#- Map in Python is a function that works as an iterator to return a result after applying a function to every item of an iterable (tuple, lists, etc.). It is used when you want to apply a single transformation function to all the iterable elements. The iterable and function are passed as arguments to the map in Python

#---------------------------------------------------------------

#9. Dictionaries in Python:
#- . Dictionaries are used with curly brackets.Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates. As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

#---------------------------------------------------------------

#10. Creating Dictionary:

#dict = {}
#print(dict)

#dict = {1:'abcd', 2:'efgh',3:'ijkl'}
#print(dict)

#dict = {'Name':'Class',1:[1,2,3,4,5]}
#print(dict)

#Dict ={1: 'DSA', 2:'Python',3:'ShreyxnshXR Gaming'}
#print(Dict)

#---------------------------------------------------------------

#11. Set Data Structures in Python:
#- Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage. A set is a collection which is unordered, unchangeable*, and unindexed. * Note: Set items are unchangeable, but you can remove items and add new items.

#set1 = set()
#print(set1)
#type(se