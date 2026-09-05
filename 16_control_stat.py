# for loop:

# write program to print "Hello World" 5 times.

# print("Hello World")   # NOTE: Not Practical approach
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

#------------------------------------

# count = 0
# while count < 5:
#     print("Hello World")
#     count +=1

#----------------------------------------------

# for i in range(0, 5, 1):  # 0, 1, 2, 3, 4
#     print("Hello World", i)

#---------------------------------------------------
# Write a program to print 1 to 10 numbers. 

# for i in range(1, 11, 1):
#     print(i, end=" ")

#----------------------------------------------------

# Write a program to print table of 23

# for i in range(1, 11):
#     print(f"{23} * {i} = {23*i}")

# Write a program to print even numbers in between 23 and 50

# for i in range(23, 50):
#     if i % 2 == 0:
#         print(i, end=" ")

# Write a program to print all numbers which are divisible
# by 3, 4, 5 in 1 to 100.

# for i in range(1, 100):
#     if i % 3 == 0 and i % 4 == 0 and i % 5 ==0:
#         print(i)

#----------------------------------------

# Write aprogram to print all Capital letters from 
# bellow string.
# str1 = "Ghj91KlOP$%sedQ"   # GKOPQ

# for i in str1:
#     if i.isalpha() and i == i.upper():  # G == G,   h == H
#         print(i, end=" ")

#_----------------------------------------------------------

# Write a program to print all special chrarecters from 
# string.

# str2 = "Asd23&*hKKJ#%PL21@"

# for i in str2:
#     if not(i.isalnum()):
#         print(i, end=" ")

#-------------------------------------------

# Write a program to print all numbers from string.
# str3 = "ER87Kol*&^56g&j4"

# for i in str3:
#     if i.isdigit():
#         print(i, end=" ")


#--------------------------------------

# Write a program to print all those numbers which are 
# greter than 5 from bellow list
# l1 = [8, 2, 1, 9, 11, 3, 7, 2]

# for i in l1:
#     if i > 5:
#         print(i)

#-----------------------------------------------------------
# Write a program to print all those students 
# names with marks who passed in exam. 
# NOTE above or equal 50 ==> Pass

# student_marks = {
#     "Sagar": 23,
#     "Sachin": 89,
#     "Samiksha": 56,
#     "Kirthana": 34,
#     "Raghu": 77,
#     "Daya": 50
# }

# for name, marks in student_marks.items():
#     if marks >= 50:
#         print(f"{name} ==> {marks}")

#---------------------------------------------------
# Write a program which ll ask to give number.
# and will print whether than number is even or odd.

# while True:
#     num = input("Enter a number: ")
#     if num.title() == "Exit":
#         break
#     elif num.isdigit() or (num[0] == "-" and num[1::].isdigit()):
#         if int(num) % 2 == 0:
#             print("Even")
#         else:
#             print("Odd")
#     else:
#         print("Invalid charecter")

#--------------------------------------------------

