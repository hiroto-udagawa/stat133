# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Stat 133: Homework 5 - Part A - Looping and Branching

# <markdowncell>

# The exercises below are taken from Chapters 1 and 2 of following book (freely available online from within the campus):
# 
# [A Primer on Scientific Programming with Python](http://link.springer.com/book/10.1007/978-3-642-18366-9/page/1)
# 
# If may be a good idea to browse through these chapters: Especially Chapter 1 sections 1.1, 1.2, 1.3, 1.4, and 1.5 and the whole Chapter 2. 

# <markdowncell>

# ## Chapter 1: section 1.8

# <markdowncell>

# ###Exercice 1.1:
# * Write a Python program in a file named "1plus1.py" that assign the result of 1+1 to a variable and print that variable. (Don't forget the bang line)

# <codecell>

%%file 1plus1.py
#!/usr/bin/python

#write your code here
x = 1 + 1
print x

# <markdowncell>

# * Execute your program in the cell bellow

# <codecell>

%%bash

chmod +x 1plus1.py
./1plus1.py

# <markdowncell>

# ###Exercise 1.2
# * Write a file named "hello_world.py" containing a Python programm that print "Hello World!"

# <codecell>

%%file hello_world.py
#!/usr/bin/python

print "Hello World!"

# <markdowncell>

# * Execute your program in the cell below

# <codecell>

%%bash

chmod +x ./hello_world.py
./hello_world.py

# <markdowncell>

# ###Exercise 1.10
# Consider the normal distribution
# $$f(x) = \frac{1}{\sqrt{2\pi}s}\exp\left[{-\frac12\left(\frac{x-m}{s}\right)^2}\right]$$
# 
# Write Python code to be executed in the cell below that evaluates the function $f$ for $m=0$, $s=2$, and $x=1$. Write it in a way that makes it easy to change the values of the parameters $s$, $m$ and the variable $x$. 

# <codecell>

from math import sqrt, pi, exp

s = 2.0
m = 0
x = 1

Normalization = 2*sqrt(s*pi)
Argument = -0.5*((x-m)/2.0)**2 

print (1/Normalization)*exp(Argument)

# <markdowncell>

# ### Optional
# * Try all the exercises in section 1.8 using an editor to create the programm file, and execute it on the command line. 

# <markdowncell>

# ##Chapter 2: section 2.7

# <markdowncell>

# ###Exercise 2.2 
# An approximative formula to convert Fahrenheit degrees (F) to Celsius degrees (C) is $$C = (F-30)/2.$$
# 
# Write some Python code to be executed in the cell below that prints a table with two columns: the left column should contain the temperatures in Fahrenheit from 0 to 100 in steps of 10 (i.e. 0, 10, 20,..., 100) and the right column should contain the converted temperature in Celsius degrees.
# Both columns should be formatted with 10 characters aligned to the left.

# <codecell>

print "%-10s\t%-10s" %("Fahrenheit", "Celsius")

for fahrenheit in range(0,100,10):
    celsius = (fahrenheit - 30)/2.0
    print "%-10g\t%-10g" %(fahrenheit, celsius)

# <markdowncell>

# ###Exercise 2.4 and 2.5 (variant)
# Write some Python code to be executed in the next cell that generates all odd numbers from 1 to n, store them in a list using <code>append</code>, and then print the list.  
# Set n in the beginning of the program and use a while loop to compute the numbers and store them in the list. (Make sure that if n is an even number, the largest generated odd number is n-1.) 

# <codecell>

n = 100
odd_numbers = []

k=0
while 2*k+1 <= n: 
    odd_numbers.append(2*k+1)
    k += 1
    
print odd_numbers

# <markdowncell>

# ###Exercise 2.5
# Redo the previous exercise using a list comprehension (with for and range).
# 
# **Hint:** you may need to use the expression <code>n/2 + n%2</code> not to always have the correct range.

# <codecell>

n = 10

odd_numbers = []

for odd in [2*k+1 for k in range(0,n/2+n%2)]:
    odd_numbers.append(odd)
    
print odd_numbers

# <markdowncell>

# ###Chapter 3: Read texbook chapter 3 and do the following exercises from section 3.5
# 
# * sections 3.3 is optional (nice examples of bioinformatic there though)

# <markdowncell>

# ###Exercise 3.1
# The exact formula for converting Fahrenheit degrees to Celsius reads
# $$C = \frac59(F −32).$$
# 
# 1. Write a function C(F) that takes a temperature F in Fahrenheit and returns the temperature in Celsius.
# 
# 1. Write a function F(C) that converts Celsius into Fahrenheit
# 
# 1. Verify your implementation by checking that c always equals C(F(c)) for any temperature for any temperature c
# 
# **Hint:** For the last point, test an appropriate boolean expression for a range of values (say from 0 to 100), and print an error message the first time c is not equal to C(F(c)). 
# 
# **Caution:** you should be careful though with comparing real numbers with <code>==</code> (see Exercise 2.24).

# <codecell>

def C(F):
    return (5/9.0)*(F - 32)
C(10)

def F(C):
    return (9/5.0)*C + 32

test_range = range(100) 

for c in test_range:
    if not(-0.1 < c - C(F(c)) < 0.1):
       print "implementation error: C(F(c)) not equal to c for c =", c
       break

# <markdowncell>

# 

# <markdowncell>

# ###Exercise 3.12
# 
# Write various hello-world functions in the cell below. Write three functions:
# 
# 1. hw1, which takes no arguments and returns the string ’Hello, World!’
# 1. hw2, which takes no arguments and returns nothing, but the string ’Hello, World!’ is printed in the terminal window
# 1. hw3, which takes two string arguments and prints these two argu-ments separated by a comma.

# <codecell>

def hw1():
    return "Hello, World!"

def hw2():
    print "Hello, World!"
    
def hw3(arg1, arg2):
    print "%s, %s" %(arg1, arg2)

# <markdowncell>

# Check that your "Hello World!" functions are correct by executing the next cell; the three functions should produce the exact same output:

# <codecell>

print hw1()
hw2()
hw3("Hello", "World!")

# <markdowncell>

# ###Exercise 3.32
# 
# Below is a list of the nearest stars and some of their properties. The list elements are 4-tuples containing the name of the star, the distance from the sun in light years, the apparent brightness, and the luminosity. 
# 
# The apparent brightness is how bright the stars look in our sky compared to the brightness of Sirius A. The luminosity, or the true brightness, is how bright the stars would look if all were at the same distance compared to the Sun. 
# 
# The data is given in the cell below as a list of 4-tuples:

# <codecell>

## Format: (Name, Distance (light-years), Apparent Brightness, Luminosity)
data = [
("Alpha Centauri A", 4.3, 0.26, 1.56), 
("Alpha Centauri B", 4.3, 0.077, 0.45), 
("Alpha Centauri C", 4.2, 0.00001, 0.00006), 
("Barnard Star", 6.0, 0.00004, 0.0005), 
("Wolf 359", 7.7, 0.000001, 0.00002), 
("BD +36 degrees 2147", 8.2, 0.0003, 0.006),
("Luyten 726-8 A", 8.4,  0.000003,  0.00006),
("Luyten 726-8 B", 8.4,  0.000002,  0.00004),
("Sirius A", 8.6,  1.00,      23.6),
("Sirius B", 8.6,  0.001,     0.003),
("Ross 154", 9.4,  0.00002,   0.0005),
]

# <markdowncell>

# The purpose of this exercise is to sort this list with respect to distance, apparent brightness, and luminosity.
# 
# To sort a list data, one can call <code>sorted(data)</code>, which returns the sorted list (cf. Table 2.1). However, in the present case each element is a 4-tuple, and the default sorting of such 4-tuples result in a list with the stars appearing in alphabetic order:

# <codecell>

sorted(data)

# <markdowncell>

# We need to sort with respect to the 2nd, 3rd, or 4th element of each 4-tuple. 
# 
# If a tailored sort mechanism is necessary, we can provide our own sort function as a second argument to sorted, as in <code>sorted(data, mysort)</code>. Such a tailored sort function mysort must take two arguments, say a and b, and returns −1 if a should become before b in the sorted sequence, 1 if b should become before a, and 0 if they are equal. In the present case, a and b are 4-tuples, so we need to make the comparison between the right elements in a and b. For example, to sort with respect to luminosity we write

# <codecell>

def mysort(a, b):
    if a[3] < b[3]:
        return -1
    elif a[3] > b[3]:
        return 1
    else:
        return 0

sorted(data, mysort)

# <markdowncell>

# Similarly as above, write in the cell below a two sort functions 
# <code>distance_sort(a,b)</code> and <code>brightness_sort(a,b)</code> allowing
# us to sort the data table </code>data<code> by distance and brightness; then sort the data table according these criteria. 

# <codecell>

def custom_sort(a, b, col=0):
    if a[col] < b[col]:
        return -1
    elif a[col] > b[col]:
        return 1
    else:
        return 0

def distance_sort(a,b):
    return custom_sort(a,b,1)

def luminosity_sort(a,b):
    return custom_sort(a,b,2)




# <codecell>

sorted(data, distance_sort)

# <codecell>

sorted(data, luminosity_sort)

