# Operators:-

    # Expression:-
        # Expressions are defined using operators and operands.
        # Ex:    x+6 = 11
                # operands => x, 6, 11
                # operators => +, =

# There variety of types operators:

    # Arithmetic Operators:
        # To perform operations on only numbers we use these operators:
# x = 5
# y = 3
#         # Addition +
# print(x+y)

#         # Substraction -
# print(x - y)

#         # Multiplication *
# print(x * y)

#         # True Division /
# print(x / y)

#         # Floor Division //
# print(x // y)

#         # Power **
# print(x ** y)

#         # Modulus (Mod) %
# print(x % y)
    
    # Assignment Operators
        # Assignment operators are used to assign a value to variable
        # Assign =:
# x = 5
# print(x)

#         # Add and Assign +=:
# # x = x + 5
# x+=5
# print(x)

#         # Substract and assign -=:
# x-=3
# print(x)

#         # Multiply and assign *=:
# x*=4
# print(x)

#         # true divide and assign /=:
# x/=3
# print(x)

#         # floor divide and assign //=:
# x//=5
# print(x)

#         # power and assign **=:
# x**=2
# print(x)

#         # mod and assign %=:
# x%=3
# print(x)


    # Comparison Operators:
        # To compare values we use these operators:
# x = 5
# y = 3
#         # Greater than >
# print(x > y)

#         # Lesser than <
# print(x < y)

#         # Greater or equal to >=
# print(x >= y)

#         # Lesser or equal to <=
# print(x <= y)

#         # Not equal to !=
# print(x != y)

#         # Equl to ==
# print(x == y)

    # Membership Operators
        # These operators are used to check elements are avaliable in collection, string or not
# s1 = {23, 78, 1, 0, 56, 3, 9, 11}

        # in
# print(3 in s1)
# print(100 in s1)

#         # not in
# print(3 not in s1)
# print(100 not in s1)

    # Identity Operators
        # is
        # is not
# references, shallow copy, deep copy

# Reference:
# x = [1, 2, 3, 4, [34, 56]]
# y = x
# x[0] = 100

# print(f"x: {x}")
# print(id(x))

# print(f"y: {y}")
# print(id(y))

#-----------------------------
# Shallow copy

# x = [1, 2, 3, 4, [34, 56]]
# y = x.copy()
# x[0] = 100
# x[4][0] = 500

# print(f"x: {x}")
# print(id(x))

# print(f"y: {y}")
# print(id(y))
#----------------------------
# Deep Copy 
from copy import deepcopy

# x = [2, 3, 4, 5, [56, 78]]
# y = deepcopy(x)

# x[0] = 100
# x[4][0] = 1000

# print(f"x: {x}")
# print(id(x))

# print(f"y: {y}")
# print(id(y))
#-------------------------------------
x = [1, 2, 3, [4, 5]]
# y = x
# print(x is y)
# print(x is not y)

# y = x.copy()
# print(x is y)
# print(x is not y)

# y = deepcopy(x)
# print(x is y)
# print(x is not y)

    # Logical Operators
        # Logical operators ar use to get the combined output of multiple expressions together.
        # and
        # or
        # not
x = 5
y = 3
z = 2
# print(x > y and y > z and z < x)  # True and True and True => True
# print(x < y and y > z and z < x)  # True and True and False => False


# print(x > y or y > x or z > x)   # True or False or False => True

# print(not(z < x))

    # Ternary Operators:
        # Ternary operators are used to provide conditional output.
        # ternary operators do use if and else keywords
        # ternary operators are single line expressions
        # They are faster.
        # It is recommended to use ternary operators if conditions are less and simple.
        # For complex and many conditions use conditional statements not ternary operators.

# Ask user to enter his/her favourate primary color. [Red, Blue, Green]
# And accordingly display the meaning of color.
# Red ==> Sacrifice
# Blue ===> Peace
# Green ===> Nature

# fav_prim_color = input("Enter your favourate primary color: ")
# result = "Sacrifice" if fav_prim_color == "Red" else "Peace" if fav_prim_color == "Blue" else "Nature" if fav_prim_color == "Green" else "Invalid Color"
# print(result)

# Write a program where you ask user to enter his/her marks
# and you tell the grade which they got.

# marks < 40 ===> Fail
# marks >= 40 and marks < 60 ===> Class B
# marks >= 60 and marks < 80 ===> Class A
# marks >= 80 and marks < 100 ====> Class A+
# else  ==> "Invalid Marks"


# marks = int(input("Enter your marks: "))
# result = "Fail" if marks < 40 else "B" if marks >=40 and marks < 60 else "A" if marks >=60 and marks <80 else "A+" if marks >= 80 and marks < 100 else "Invalid Marks"
# print(result)

    # Bitwise OPerators
        # Bitwise operators work at bit levels.
        # To make search of element in collection faster we can use it.
        # To perform any operators faster we use it.

        # Types of Bitwise Operators:
            # &  (AND)
# print(23 & 45)   # 5
# first convert 23 and 45 into binary
# print(bin(23))   # 10111
# print(bin(45))   # 101101 
# print(int("101", 2))

            # |  (OR)
# print(23 | 45)   # 63
# print(int("111111", 2))

            # ^  (XOR)
# print(23 ^ 45)
# print(int("111010", 2))