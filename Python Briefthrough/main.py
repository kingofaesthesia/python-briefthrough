# user_name = input("Please tell us your name; ")
# print(f"Hi,Welcome {user_name}!")

# #More Booleans...
# x is y ---- # x is the same as y
# x is not y ---- # x is not the same as y

#Calculating the gross-pay for a user by provided parameters for their Hours and Rate.
#Handling exceptional errors.
#Adding conditional flows.
# try:
#     hours = int(input("Enter Hours; "))
#     rate = float(input("Enter Rate; "))
#     if hours > 40:
#         gross_pay = hours * rate * 1.5
#     else:
#         gross_pay = hours * rate

#     print(f"The gross pay for {hours} hours and {rate} rate is {gross_pay}.")
# except ValueError:
#     print("Invalid Input\n"
#           f"Try numeric inputs.")

# #Building a Grade Checker System that collects and measures inputs from (0.0 - 1.0)
# try:
#     score = float(input("Enter a grade between 0.0 and 1.0 to get an Alphabet Score!\n ; "))
#     if score > 0.0 and score < 1.01:
#         # continue
#         if score == 0.9:
#             print("A")
#         elif score >= 0.8:
#             print("B")
#         elif score >= 0.7:
#             print("C")
#         elif score >= 0.6:
#             print("D")
#         elif score >= 0.5:
#             print("E")
#         elif score <= 0.4:
#             print("F")
#         else:
#             print("Invalid Range.")
#     else:
#         print("Out of Range\n"
#               f"Try inputing from ranges 0.0 upward(ends at 1.0)")
# except ValueError:
#     print("Error, try numeric values(decimals preferably.)")

# def compute_pay():
#     try:
#         hours = int(input("Enter Hours; "))
#         rate = float(input("Enter Rate; "))
#         if hours > 40:
#             gross_pay = hours * rate * 1.5
#         else:
#             gross_pay = hours * rate
#         print(f"The gross pay for {hours} hours and {rate} rate is {gross_pay}.")
#     except ValueError:
#         print("Invalid Input\n"
#             f"Try numeric inputs.")

# compute_pay()

# def compute_pay(a,b):
#         if a > 40:
#             pay = a * b * 1.5
#         else:
#             pay = a * b
#         return pay
    
# print(compute_pay(29,6.5)

# word = 'banana'
# count = 0
# for letter in word:
#    if letter == str('n'):
#       count = count + 1
# print(count)

# class Letter_counter:
#     def __init__(self,word,letter):
#         self.word = word
#         self.letter = letter

#     def calculate_alp(self,word,letter):
#         word = self.word
#         count = 0
#         for letter in self.word:
#             if self.letter == str(letter):
#               count += 1
#         return count
        
#     def display_details(self):
#         return f"Your word is {self.word} and your letter is {self.letter}."
    

# my_num = Letter_counter('banana','a')
# print(my_num.display_details())
# print(my_num.calculate_alp('banana','a'))

# def letter_checker(word,letter):
#      count = 0
#      for i in word:
#         if i == str(letter):
#            count += 1
#      return count

# print(letter_checker('banahahahana','a'))

# ----------Data Structures = Lists,Tuples,Arrays and Dictionaries.------------------------------------------------#

#More String,Lists and Files Built-In functions.
# startswith() Returns either True or False
# endswith() Returns either True or False
# find() Specify a position to start looking.
# open() Opens a specific file (txt).
# close() Closes an opened file (txt).
# exit() Terminate the program.
# extend() Takes a list as an argument and appends all items into a specific list.
# remove() Removes an item from a list.
# sort()/list.sort(Reverse=True) Arrange items in a list in ascending order/descending order.
# del() Deletes an item in a list.
# pop() Temporary removes items from a list.
# sum() Adds up the sum of each integer in a given list.
# len() Counts the number of items in a list.
# min() Finds the maximum integer in a list.
# max() Finds the minimum integer in a list.
# list() Converts strings to a list of characters.
# split() Split items in a list.
# join() Combine items to a given list.
# delimeter() A symbol used to seperate words. e.g ;(-) The hyphen.
# list() Used to convert a string into a list.
# zip() Used to combine two or more sequence into a sequence
# dict()
# values()
# items()
# get('key','default value')
# lower()
# sorted()
# reversed()
# punctuation()
# translate()
# tuple()

# def chop(a):
#     return a[1:-1]
# list = [0,1,3,4,5,5,6,8]

# print(chop(list))

# def middle(a):
#     return a[0:-1]
# list = [0,1,3,4,5,5,6,8]
# print(middle(list))
    
# print(help(type(list)))

#Writing a program that collects integric inputs,appends them into a list and finally,prints out the minimum and maximum value in it.
# empty_list = []
# while True:
#     num = input("Enter a number; ").title()
#     if num == "Done":
#        break
#     value = int(num)
#     empty_list.append(value)
# print(f"{empty_list}\n"
#       f"Minimum Value ; {min(empty_list)}\n"
#       f"Maximum Value ; {max(empty_list)}")

# #Calculating the number of times a letter appears in a dictionary using loops and conditions.
# word = 'boogie'
# d = dict()
# for i in word:
#     if i not in d:
#        d[i] = 1
#     else:
#       d[i] = d[i] + 1
# print(d)

#You can’t modify the elements of a tuple, but you can replace one tuple with another:
# t = tuple('a',)
# t = ('A',) + t[1:]
# print(t)

# #Splitting words in a text.
# text = 'How are you?'
# split_list = text.split() #Splits elements in list into words.
# print(split_list)
# >>> ['How','are','you?'}


# One of the unique syntactic features of the Python language is the ability to have
# a tuple on the left side of an assignment statement. This allows you to assign more
# # than one variable at a time when the left side is a sequence.
# m = [ 'have', 'fun' ]
# (x, y) = m # Omitting the parentheses has an equally valid syntax.
# print(x) 
# >>>'have'
# print(y)
# >>>'fun'

#Tuples also allow us to swap  the values of two variables in a simple syntax, e.g; 
# a, b = b, a

# The number of variables on the left and the number of values on the right must be
# the same,else it gives the exception;  ValueError

# addr = 'monty@python.org'
# uname, domain = addr.split('@') #Remove the '@' symbol and split the remaining elements into two.
# The return value from split is a list with two elements; the first element is assigned
# to uname, the second to domain.
# print(uname)
# >>>monty
# print(domain)
# >>>python.org

# Regex(Regular Expressions)
# import re
# re.search() '^'- Beginning of a line.
# re.findall() '\S+key\S+' Search for any word with 'key's' specific character.
# ˆ Matches the beginning of the line.
# $ Matches the end of the line.
# . Matches any character (a wildcard).
# \s Matches a whitespace character.
# \S Matches a non-whitespace character (opposite of \s).
# * Applies to the immediately preceding character(s) and indicates to match zero or more times.
# *? Applies to the immediately preceding character(s) and indicates to match zero or more times in “non-greedy mode”.
# + Applies to the immediately preceding character(s) and indicates to match one or more times.
# +? Applies to the immediately preceding character(s) and indicates to match one or more times in “non-greedy mode”
# ? Applies to the immediately preceding character(s) and indicates to match zero or one time.
# ?? Applies to the immediately preceding character(s) and indicates to match zero or one time in “non-greedy mode”.
# [aeiou] Matches a single character as long as that character is in the specified set.
# In this example, it would match “a”, “e”, “i”, “o”, or “u”, but no other characters.
# [a-z0-9] You can specify ranges of characters using the minus sign. This example
# is a single character that must be a lowercase letter or a digit.
# [ˆA-Za-z] When the first character in the set notation is a caret, it inverts the logic. This example matches a single character that is anything other than an uppercase or lowercase letter.
# ( ) When parentheses are added to a regular expression, they are ignored for the purpose of matching, but allow you to extract a particular subset of the matched string rather than the whole string when using findall().
# \b Matches the empty string, but only at the start or end of a word.
# \B Matches the empty string, but not at the start or end of a word.
# \d Matches any decimal digit; equivalent to the set [0-9].
# \D Matches any non-digit character; equivalent to the set [ˆ0-9]
# s.count(substr) Counts the number of occurences of a substring
# s.find(substr) Finds index of the first occurence of a substring, or -1
# s.rfind(substr) Finds index of the last occurence of a substring, or -1
# s.index(substr) Like find, except ValueError is raised if not found
# s.rindex(substr) Like rfind, except ValueError is raised if not found
# s.startswith(substr) Returns True if string starts with a given substring
# s.endswith(substr) Returns True if string ends with a given substring
# s.replace(substr, replacement) Returns a string where occurences of one string are replaced by another
# s.lower() Change all letters to lowercase
# s.upper() Change all letters to uppercase
# s.capitalize() Change the first character to upper case and change the rest to lower case
# s.title() Change to titlecase
# s.swapcase() Change all uppercase letters to lowercase, and vice versa



# Search for lines that start with 'From' and # Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#    line = line.rstrip()
#    if re.search('^From:'/ '^F..m', line): '^' line's that start with 'Word'., '..' Starts with F and two chharacters before 'm'.
#      print(line)

#Example 2
# # Search for lines that start with From and have an at sign
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#    line = line.rstrip()
#    if re.search('^From:.+@', line):  # "Keyword :.+ 'sign'" 
#     print(line)
# >>> From: stephen.marquard@uct.ac.za #Matches From with @ sign.


# # Find all words in this string that starts from "@"(email-addresses)
# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\S+@\S+', s) / non whitespace character - '@' sign - another non whitespace character.
# print(lst)
# >>> ['csev@umich.edu', 'cwen@iupui.edu']

# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#    line = line.rstrip()
#    if re.search('^X\S*: [0-9.]+', line): #
#    print(line)
#Translating this, we are saying, we want lines that start with X-, followed by zero
# or more characters (.*), followed by a colon (:) and then a space. After the 
# space we are looking for one or more characters that are either a digit (0-9) or
# a period [0-9.]+. Note that inside the square brackets, the period matches an
# actual period (i.e., it is not a wildcard between the square brackets).

#Extracting the numbers.
# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.

# import re
# hand = open('mbox-short.txt')
# for line in hand:
    # line = line.rstrip()
    # x = re.findall('^X\S*: ([0-9.]+)', line)
    # if len(x) > 0:
        # print(x)

# ^From .* [0-9][0-9]:
# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
#OR
# The translation of this regular expression is that we are looking for lines that start
# with From (note the space), followed by any number of characters (.*), followed by
# a space, followed by two digits [0-9][0-9], followed by a colon character. This is
# the definition of the kinds of lines we are looking for.

# import re
# hand = open('mbox-short.txt')
# for line in hand:
    # line = line.rstrip()
    # x = re.findall('^From .* ([0-9][0-9]):', line)
    # if len(x) > 0:
    #    print(x)

# import re
# x = 'We just received $10.00 for cookies.'
# y = re.findall('\$[0-9.]+',x)
# print(y)
# >>>$10.00

#Networking programs on the Internet with sockets for Python.

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#       break
#     print(data.decode(),end="")
  
# mysock.close()

# #Making a multiplication table with a for loop;
# time = 8
# for i in range(12):
#     print(f"{time} multiplied by {i} is equal to {time * i}")

# #Using the join method to concatenate lots of strings
# a="first"
# b="second"
# print(a+b)
# print(" ".join([a, b, b, a]))

# #Summing up a set of numbers in a list.
# s=0
# for i in [0,1,2,3,4,5,6,7,8,9]:
#     s = s + i
# print("The sum is", s) #45

# #Using format strings
# from math import sqrt, log
# l=[1,3,65,3,-1,56,-10]
# for x in l:
#     if x < 0:
#         continue
#     print(f"Square root of {x} is {sqrt(x):.3f}") #:.3f in three floats.
#     print(f"Natural logarithm of {x} is {log(x):.4f}") #:. 4f in four floats.

#Dice.py

# numbers = [1,2,3,4,5,6]
# time = [1,2,3,4,5,6]

# for num in numbers:
#     print(f"{num} in range({time}")
#     if num < 0:
#         for i in time:
# #             print(f"{num},{i}")

# Dice = [1,2,3,4,5,6]
# time = range(6)

# for i in Dice:
#     for i in time:
#         if (i + time) == 5:
#             print(f"{i} ,{time}")

# numbers = [1,2,3,4,5,6]
# for i in numbers:
#     print(i)


# #Functions
# def double(x):
#     "This function multiplies its argument by two." #Python saves the docstring for documentation.
#     return x*2
# print(double(4), double(1.2), double("abc"))

# #Accessing Saved Docstrings.
# print("The docstring is:", double.__doc__)
# help(double)   # Another way to access the docstring

# def sum_of_squares(a, b):
#     "Computes the sum of arguments squared"
#     return a**2 + b**2
# print(sum_of_squares(3, 4))


# def sum_of_squares(lst):
#     "Computes the sum of squares of elements in the list given as parameter"
#     s=0
#     for x in lst:
#         s += x**2
#     return s
# #The arguments were bring wrapped into a list.
# print(sum_of_squares([-2])) #-2 * -2 = 4
# print(sum_of_squares([-2,4,5])) # -2 * -2 + 4 * 4 + 5 * 5 = 45

#  This works perfectly!
# There is however some extra typing with the brackets around the lists.
# #  Let's see if we can do better:

# #Argument Packing.
# def sum_of_squares(*n): #(*) Accepts mulgtiple parameters.
#     "Computes the sum of squares of arbitrary number of arguments"
#     ans=0
#     for i in n:
#         ans = ans + i**2
#     return ans

# lst=[1,5,8]

# print("With list unpacked as arguments to the functions:", sum_of_squares(*lst))

# print(sum_of_squares(-2)) #4
# # print(sum_of_squares(-2,4,5)) # 45


# #Argument Unpacking
# There is also syntax for argument unpacking.
# It has confusingly exactly same notation as argument packing (star), 
# but they are separated by the location where used. 
# Packing happens in the parameter list of the functions definition, 
# and unpacking happens where the function is called:

# lst=[1,5,8]
# print("With list unpacked as arguments to the functions:", sum_of_squares(*lst))
# # print(sum_of_squares(lst))    # Does not work correctly


# print(1, 2, 3, end=' |', sep=' -*- ') # end with this " 1" and seperate them with " -*- "
# print("first", "second", "third", end=' |', sep=' -*- ') #Space sensitive


# Global variables(Variables Visibility)
# i=2
# def f():
#     global i
#     i=5       # rebind the global i variable #Take all instances of i and make them 5.
#     print(i)  # This will print 5
# f()
# print(i)      # This will print 5

# def number():            # outer function
#     n=2
#     def inside_num():        # inner function
#         #nonlocal n   #nonlocal n, makes all n variables = 20 # Without this nonlocal statement, (P.S : See it as; Not your average n, hehe)
#         n=20         # this will create a new local variable
#         print(n)
#     inside_num()   #Calling n as 2 because of it being an outer function.
#     print(n) #Call the initial n in the number() function, which is 2.

# #The main function running.    
# number()
# # >>>>20
# # >>>>20 withhout 'nonlocal n' it gives 2

# The global and nonlocal statements are similar. 
# The first will force a variable refer to a global variable, 
# and the second will force a variable to refer to the variable in the nearest outer scope 
# (but not the global scope).

# def triple(*n):
#     ans = 0
#     for i in n:
#        ans = ans + i*3
#        return f"triple of {i} is equal to {ans}."
    
# print(triple(5,6,7))

# def square(*n):
#     ans = 0
#     for i in n:
#         ans = ans + i**2
#         return f"square{i} = {ans}"
# # print(square(2))
       
# lst = [1,2,3,4,5,6,7,8,9,10]
# for i in lst:
#     print(f"{square(i)},{triple(i)}")

# #Data Structures
# The generic form of a slice is sequence[first:last:step]. 
# If any of the three parameters are left out, 
# they are set to default values as follows: first=0, last=len(L), step=1. 
# So, for instance "abcde"[1:]=="bcde". 
# The step parameter selects elements that are step distance apart from each other.


# We can assign values to elements of a list by indexing or by slicing. An example:
# L=[11,13,22,32]
# L[2]=10          # Changes the third element
# print(L)
# >>>[11, 13, 10, 32]

# # Or we can assign a list to a slice:
# L[1:3]=[4]
# print(L)
# >>>[11, 4, 32]

# #Zip function - zip()
# L1=[1,2,3]
# L2=["first", "second", "third"]
# print(zip(L1, L2))               # Note that zip does not return a list, like range
# print(list(zip(L1, L2)))         # Convert to a list

# Here's another example of using the zip function.

# days="Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split() #Seperate each space character into a comma 
                                                                          #and make it a single element,
# weathers="rainy rainy sunny cloudy rainy sunny sunny".split()
# temperatures=[10,12,12,9,9,11,11]
# for day, weather, temperature in zip(days,weathers,temperatures):
#     print(f"On {day} it was {weather} and the temperature was {temperature} degrees celsius.")

# # Or equivalently:
# #for t in zip(days,weathers,temperatures):
# #    print("On {} it was {} and the temperature was {} degrees celsius.".format(*t))
# >>>On Monday it was rainy and the temperature was 10 degrees celsius, e.t.c.


# #Using the enumerate() function;
# L=[1,2,98,5,-1,2,0,5,10]
# counter = 0
# for i, x in enumerate(L):
#     if x == 5:
#         counter += 1
#         if counter == 2:
#             break
# print(i)
# >>>7

# #Alternative syntaxes to Dictionary Creation
# dict([("key1", "value1"), ("key2", "value2"), ("key3", "value3")]) # list of items
# dict(key1="value1", key2="value2", key3="value3") #Tuples are hashable

# d={}
# d[2]="value"
# print(d)
# >>>{2: 'value'}

# # Dictionary object contains several non-mutating methods:
# d.copy()
# d.items()
# d.keys()
# d.values()
# d.get(k[,x])

# Some methods mutate the dictionary:
# d.clear()
# d.update(d1)
# d.setdefault(k[,x])
# d.pop(k[,x])
# d.popitem()

# Sets
# Set is a dynamic, unordered container. 
# It works a bit like dictionary, but only the keys are stored. 
# And each key can be stored only once.

# s={1,1,1}
# print(s)
# s=set([1,2,2,'a'])
# print(s)
# s=set()  # empty set
# print(s)
# s.add(7) # add one element
# print(s)
# >>>{1}
# >>>{1, 2, 'a'}
# >>>set()
# >>>{7}

# A more useful example of sets:
# s="mississippi"
# print(f"There are {len(set(s))} distinct characters in {s}")
# There are 4 distinct characters in mississippi
# The set provides the following non-mutating methods:

# s=set()
# s1=set()
# s.copy()
# s.issubset(s1)
# s.issuperset(s1)
# s.union(s1)
# s.intersection(s1)
# s.difference(s1)
# s.symmetric_difference(s1);

# s=set([1,2,7])
# t=set([2,8,9])
# print("Union:", s|t)
# print("Intersection:", s&t)
# print("Difference:", s-t)
# print("Symmetric difference", s^t)
# >>>Union: {1, 2, 7, 8, 9}
# >>>Intersection: {2}
# >>>Difference: {1, 7}
# >>>Symmetric difference {1, 7, 8, 9}
# There are also the following mutating methods:
# s.add(x)
# s.clear()
# s.discard()
# s.pop()
# s.remove(x)

# first, second = [4,5]
# a,b,c = "bye"
# print(c)
# d=dict(a=1, b=3)
# key1, key2 = d
# print(key1, key2)
# >>>e
# # >>>a b

# L=[ a**3 for a in range(1,11)]
# print(L)
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# L=[ 100*a + 10*b +c for a in range(0,10)
#                     for b in range(0,10)
#                     for c in range(0,10) 
#                     if a <= b <= c]
# print(L)
# >>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23,]

# Similary a dictionary comprehension creates a dictionary:

# d={ k : k**2 for k in range(10)}
# print(d)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# And a set comprehension creates a set:

# s={ i*j for i in range(10) for j in range(10)}
# print(s)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27,]

# The map function gets a list and a function as parameters, 
# and it returns a new list whose elements are elements of the original list transformed by the parameter function. 
# For this to work the parameter function must take exactly one value in and return a value out. 
# An example will clarify this concept:

# def double(x):
#     return 2*x
# L=[12,4,-1]
# print(map(double, L))
# >>><map object at 0x7fb81413ef60>

# The map function returns a map object for efficiency reasons. 
# However, since we only want print the contents, 
# we first convert it to a list and then print it:

# print(list(map(double,L)))
# >>>[24, 8, -2]

# s="12 43 64 6"
# L=s.split()        # The split method of the string class, breaks the string at whitespaces
#                    # to a list of strings.
# print(L)
# print(sum(map(int, L)))  # The int function converts a string to an integer

# #Lamda Functions
# The lambda expression has the form lambda param1,param2, ... : expression

# L=[2,3,5]

# print(list(map(lambda x : 2*x+x**2, L)))

# Filter Function
# def is_odd(x):
#     """Returns True if x is odd and False if x is even"""
#     return x % 2 == 1         # The % operator returns the remainder of integer division
# L=[1, 4, 5, 9, 10]
# print(list(filter(is_odd, L)))
# >>>[1,5,9]

# L=[1,2,3,4]
# from functools import reduce   # import the reduce function from the functools module
# reduce(lambda x,y:x+y, L, 0)
# >>>10

# If we wanted to get a product of all numbers in a sequence, we would use
# reduce(lambda x,y:x*y, L, 1)
# >>>24

# An iterable is an object whose elements can be gone through one by one using a for loop. 
# Such as range(1,7)

# "--".join(["abc", "def", "ghi"])
# 'abc--def--ghi'
# L=[str(x) for x in range(100)]
# s=""
# for x in L:
#     s += " " + x    # Avoid doing this, it creates a new string at every iteration
# print(s)            # Note the redundant initial space
# print(" ".join(L))  # This is the correct way of building a string out of smaller strings

# >>> 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 
# >>>35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 
# >>>67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99
# >>>0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 
# >>>34 35 36 37 38 39 40 41 42 43 


#Classes
# class MyClass(object):
#     """Documentation string of the class"""

#     def __init__(self, param1, param2):
#         "This initialises an instance of type ClassName"
#         self.b = param1 # creates an instance attribute
#         c = param2      # creates a local variable of the function
#         # statements ...
    
#     def f(self, param1):
#         """This is a method of the class"""
#         # some statements

# class B(object):
#     def f(self):
#         print("Executing B.f")
#     def g(self):
#         print("Executing B.g")
    
# class C(B):
#     def g(self):
#         print("Executing C.g")
        
# x=C()
# x.f() # inherited from B
# x.g() # overridden by C

# The inheritance relation of two classes B and C can be tested with function issubclass: 
# issubclass(C,B)==True but issubclass(B,C)==False
# Function isinstance(obj, cls) allows us to test whether an instance has type cls or has an ancestor class of type cls. Let’s create instances x=C() and y=B(). 
# Now we have isinstance(x,B)== isinstance(x,C)==isinstance(y,B)==True. But isinstance(y,C)==False.
# a=1 # This creates a class attribute


#World's simplest browser with Python.
# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket protocols as parameters

# mysock.connect(('data.pr4e.org', 80)) #We connect the site we want to retrieve to Port 80

# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #r\n\rn as blank spaces(equivalent)
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:   #if reply ois less than 1 break the connection.
#        break
#     print(data.decode(),end='') #Decode the data and end with space.

# mysock.close()  #Close the connncetion.

# #Webpage
# HTTP/1.1 200 OK
# Date: Wed, 11 Apr 2018 18:52:55 GMT
# Server: Apache/2.4.7 (Ubuntu)
# Last-Modified: Sat, 13 May 2017 11:22:22 GMT
# ETag: "a7-54f6609245537"
# Accept-Ranges: bytes
# Content-Length: 167
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/plain

# #Text in document(body)
# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief

# # encode() and decode() methods convert strings into bytes objects and back again
# The next example uses b'' notation to specify that a variable should be stored as
# a bytes object. encode() and b'' are equivalent

# hello = b'Hello world'
# print(hello)
# hello.decode()
# # b'Hello world'
# hello.encode()
