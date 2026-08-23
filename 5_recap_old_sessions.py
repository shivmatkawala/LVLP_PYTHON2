# Python:-  

    # What is Python ?
        # Python is a programming Language.
        # High level programming language.
        # General purpose programming language.
        # Python is english like programming language.
        # Python is Dynamically typed programming language.
        # Python is loosely coupled programming language.
        # Python is Hybrid programming language.
        # Python supports procedural, functional, object oriented and modular programming paradigms.


    # What topics of python we are going to cover in this python course:
        # variables
        # datatypes -> 10 types
        # operators -> 8 types
        # conditional statements -> if, elif, else
        # match case -> match, case
        # control statements -> while loop, for loop
        # comprehensions -> 4 types
        # lambda functions
        # map, filter, reduce, sorted, reversed with lambda
        # file handeling -> open, openpyxl
        # error and exception handeling -> try, except, else, finally, exception class
        # functional programming :- no arg func, pos arg func, default arg func, keyword arg func, var len arg func, var len keyword arg func
        # regex

#------------------------------------------------------------------

# Chapter 1: Variables:-

    # English ==> My name is shivkumar  (H-> H)
    # Python  ==> My_name = 'shivkumar' (H-> S)
            # My_name => variable
            # 'shivkumar' => data/ value/ info

    # Python has give set of rules to follow while creating variables:

        # Rule 1: You can use alphabets (A-Z, a-z) to create a variable.

        # Rule 2: You can use decimal numbers (0-9) to create a variable,
        # but never ever start a variable from number.

        # Rule 3: You can not use special charecters (@#$. "{-}") to create
        # variable except _

        # Rule 4: Yo can not use keywords as variables.
        # What is mean by keyword?
            # A word which is used by python internally is called keyword.
            # 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 
            # 'await', 'break', 'class', 'continue', 'def', 'del', 
            # 'elif', 'else', 'except', 'finally', 'for', 'from', 
            # 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
            # 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 
            # 'with', 'yield'

        # Rule 5: Create a meaningful variable.


# ----------------- PRACTICE OF VARIABLES:

name = 'alan'
NAME = 'Sara'
Name = 'Jay'
NamE = "Sanajana"
NAMe = 'Mallesh'

# NOTE: Python is case sensitive programming language.

# 34ways = 'chinese reaurant'  # incorrect => starts with number

sanjana_age = 27
china_36_town = 'Chinese temple'

#-------------- While creating variables:-

# snake case
    # In python snake case is famous
    # ram_city_population = 450009990

# camel case
    # In JavaScript camel case famous
    # ramCityPopulation = 3478383893

#-------------------------------------------------------

# Data :-

    # x = 5           Data  => Integer
    # y = 'tomorrow'  Data  => Text
    # z = 4.5         Data  => decimal

# num1 = "Hello"
# num2 = 23

# hey, perform substraction operation on num1 and num2
# print(num1 - num2)

# NOTE: It completely depends upon data that what operations can be 
# performed.

#-------- How many different datatypes python supports -------

# Datatypes:
    # Primitive :
            # Numeric:
                # 1) Integer:- A number without decimal point is an integer, 
                # Integers can be +ve and -ve including 0

                # Ex: 23, -12, 0, 56, -1000
                #-----------------------------------

                # 2) Float:- A number with decimal point is a float,
                # floats can be +ve and -ve

                # Ex: -12.222, 90.0, 67.234, -45.0001
                #-----------------------------------

                # 3) Complex:- A combination of Real NUmber and Imaginary Numaber
                # Real:- All Integers and Floats are real numbers
                # Ex: 34, -12, -4.4, 0, 0.0001, -2.001

                # Imaginary: A number suffixed by 'j'
                # Ex: 90j, 12j, -4j, -1.1j, -0.009j

                # Complex Ex: 34-90j, -12-7j, -0.111j+67j
                #---------------------------------------------


            # Text:
                # 1) String
                    # A sequence of charecters enclosed by quotes
                    # charecters can be => alphabets, numbers, special

                    # Quotes:
                            # Famous to use for small strings
                            # ''  => Single quote
                            # ""  => Double quote

                            # Famous to use for big strings
                            # ''' ''' => Tripple Single quote
                            # """ """ => Tripple Double quote

                    #Ex:  'Hello', "Hello"  '''Hello this is shivkumar'''  """My dear friends this is python session"""

str1 = 'Hello this """is""" "shivkumar"'

str2 = "Hello '''this''' is 'shivkumar'"

str3 = '''Hello 'this' "is" """shivkumar""""'''

str4 = """Hello 'this' "is" '''shivkumar'''"""

# What type of dattatype is string?
# string is immutable (once created can not be modified)
# string is a sequence of charecters
# string is ordered
# it supports indexing


# Indexing:-

str1 = "HELLO"
print(str1)

print(str1[0])
print(str1[-5])

print(str1[1])
print(str1[-4])


# SLICING
# print(str1[0:2:1])
# print(str1[3:5:1])
# print(str1[1:4:1])

# print(str1[0:5:2])
# print(str1[0:5:3])

# print(str1[4::-1])
# print(str1[-1:-4:-1])
# print(str1[-1::-2])

#-------------------------------------------------------
            # Boolean:
                # True  => 1
                # False => 0

    # Non-Primitive:
            # Collections:
                # 1) List 
                # 2) Tuple
                # 3) Set

            # Range

            # Dictionary