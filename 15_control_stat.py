# Control Statements:
    # We also call control statements as loops.
    # loops are important to perform operations on collections each element.
    # Types of Loops:
        # For Loop
        # While Loop

#--------------------------------------------------------------

# while loop:
# Ex: Write a program to print "Hello World" 50000 times

# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

# count = 0     # To count how many "Hello worlds printed so far"

# while count < 5:          # 0, 1, 2, 3, 4, 
#     print("Hello World", count)
#     count+=1


#-----------------------------------------------

# Ex- Print table 1 to 100000 numbers 
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# number = 1
# while number < 10001:
#     print(number)
#     number +=1

#---------------------------------------
# Ex- Write a program to print table of 7
# 7, 14, 21, 28, 35, 42, 49, 56, 63, 70
# print(7)
# print(14)
# print(21)
# print(28)
# print(35)
# print(42)
# print(48)
# print(56)
# print(63)
# print(70)

# number = 1
# while number < 11:
#     print(number*7, end=" ")
#     number +=1

#-------------------------------------------

# Ex- Write a program to print all even numbers in between
# 1 to 20
# 2, 4, 6, 8, 10, 12, 14, 16, 18 => Even

# number = 1
# while number < 20:
#     if number % 2 == 0:
#         print(number, end=" ")
#     number += 1


# Find Odd numbers in between 1 to 20

# number = 1
# while number < 20:
#     if number % 2 != 0: 
#         print(number, end=" ")
#     number +=1

# Ex- Write  a program to print all those numbers which are
# divisible by 3 and 7 and 5 in between 1 to 1000

# number = 1
# while number < 1000:
#     if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
#         print(number, end=" ")
#     number +=1


# Write a program to print consonents from bellow string
# str1 = "PYTHON GREAT"  # Consonents / Vowels (a, e, i, o, u)

# index = 0
# while index < len(str1):
#     if str1[index] not in "AEIOUaeiou":
#         print(str1[index], end=" ")
#     index+=1

#-------------------------------------------------
