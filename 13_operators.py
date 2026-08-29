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

    # Ternary Operators
    # Bitwise OPerators