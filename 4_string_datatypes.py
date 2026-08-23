#--------------------- STRING-------------------------#

    # To form a string we use quotes:
        # '',  "", ''' ''', """ """

# NOTE : It is famous to use '', "" for small strings.
str1 = 'Hello "Brother"'
str2 = "'Woww' This is Awesome"

# NOTE: It is famous to use ''' ''',  """ """ for Big strings
str3 = '''My dear students We are learning """Python for data engineering."""'''
str4 = """Python is very important to work in IT in 2026. Most of the fields in IT do use Pytho programming"""


# ------------------------------------------------------

# What type of datatype is string:

            # String is immutable (can not be modified)
            # String is a squence of charecters
            # String is ordered datatype
            # String supports Indexing (+ve , -ve)
            # String formed using quotes

# Initilize String:

# s1 = "12345688"   # when numbers written inside quotes are called string
# print(s1, type(s1))

# s2 = "@#$%^&*"    # when special charecters written inside quotes are called string
# print(s2, type(s2))
# s3 = "ABCDEFG"    # when capital letters written inside quotes are alled string
# print(s3, type(s3))

# s4 = "abenwqjkbd" # when small letters written inside quotes are called string
# print(s4, type(s4))

# s5 = "🐶🪸" # when emojis are written inside quotes are called string
# print(s5, type(s5))

# s6 = "123@#$ABCefgh🪸" #this is also a string
# print(s6, type(s6))

#------------------ INDEXING ---------------------------

str1 = "Apple@123"

        # +ve Indexing: starts from left
        # +ve indexing starts from 0

        # -ve Indexing: starts from right
        # -ve indexing starts from -1
# print(str1)
# print(str1[0])
# print(str1[1])
# print(str1[2])
# print(str1[3])
#-----------------------------------------
# print(str1[-1])
# print(str1[-2])
# print(str1[-3])
# print(str1[-9])
# #-------------------------SLICING----------------------

# # Slicing [Start_Index: End_Index: Step]

# print(str1[0:5:])
# print(str1[0:5:1])

# print(str1[-3::1])
# print(str1[::2])

# print(str1[-1:-4:-1])
# print(str1[-1::-2])
