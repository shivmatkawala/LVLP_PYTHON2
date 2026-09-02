# Conditional Statements:

    # To give the output of on conditional basis we use conditional statements.
    # we can write a first condition with "if" keyword
    # we can write rest of the conditions "elif" keyword
    # we can write default condition using "else" keyword

#----------------------------------------------------
# Write a program to print favourate primary color:

# fav_prim_color = input("Enter your favourate primary color: ")

# if fav_prim_color == "Red":       # first condition
#     print("Sacrifice")
# elif fav_prim_color == "Blue":
#     print("Peace")
# elif fav_prim_color == "Green":
#     print("Nature")
# else:
#     print("Invalid color")

#----------------------------------------------------

# Write a program where you enter a number in between 1 to 100
# if number is even print "even" if number is "odd" print "odd"

# number = int(input("Enter your number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


#--------------------------------

# User will enter a charecter.
# if it is number ==> print "number"
# if it is alphabet ==> print "alphabet"
# if it is special charecter ==> print "Special Charecter"


# chareter = input("Enter a charecter: ")

# if chareter.isdigit():
#     print("Number")
# elif chareter.isalpha():
#     print("Alphabet")
# elif not(chareter.isalnum()):
#     print("Special Charecter")
# else:
#     print("Invalid charecter")


#------------------------------------------------

# Write a program to print elgiblity of marrage as per indian mariage act
# if gender is male and age 22 or more --> Eligible
# if gender is female and age 18 or more ---> Eligible

# gender = input("Enter your gender: ")
# age = int(input("Enter your age: "))

# if gender == "Male" and age >= 22:
#     print("Eligible")
# elif gender == "Male" and age < 22:
#     print("Not eligible")
# elif gender == "Female" and age >= 18:
#     print("Eligible")
# elif gender == "Female" and age < 18:
#     print("Not Eligible")
# else:
#     print("Invalid information.")

#-------------------------------------------

# Write a program to where use enters -10 to 10 any number
# you have to find
    # if number is +ve or -ve
    # if number is even or odd

# num = int(input("Enter a number: "))

# if num > 0 and num < 11:
#     print("+ve Number")
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# elif num < 0 and num > -11:
#     print("-ve Number")
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# else:
#     print("Invalid numbers")

#-----------------------------------

# Write aprogram where you ask to enter users name.
# if name is big than 5 charecters  then print "Big name"
# if name is exactly 5 charecters then print "Good name"
# if name is less than 5 charecters then print "small name"

# name = input("Enter name: ")

# if len(name) > 5:
#     print("Big Name")
# elif len(name) == 5:
#     print("Good Name")
# else:
#     print("Small Name")

