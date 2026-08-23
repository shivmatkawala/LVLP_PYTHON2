# String In-Built Methods:

# # Case manipulaation methods:
#     # .upper()  => Converts strings lowercase alphabets into uppercase.
# str1 = "hello"
# print(str1)
# print(type(str1))
# print(str1.upper())

#     # .lower()  => Converts strings uppercase alphabets into lowercase.
# str2 = "BYE"
# print(str2)
# print(type(str2))
# print(str2.lower())

#     # .capitalize() => Converts strings first alphabet if it starts with alphabet to uppercase and rest alphabets into lowercase.
# str3 = "this is python class"
# print(str3)
# print(type(str3))
# print(str3.capitalize())

#     # .title() => Converts strings each words first alphabet if it is lowercase then into uppercase and rest alphabets into lowercase.
# str4 = "we love python"
# print(str4)
# print(type(str4))
# print(str4.title())

#     # .swapcase() => Converts uppercase into lowercase and vice versa.
# str5 = "TIgeR"
# print(str5)
# print(type(str5))
# print(str5.swapcase())

#-------------------------------------------------------------

# Search and Find Methods:
    # Returns charecters +ve index

str6 = "APPLE"

    # .index() 
# print(str6)
# print(type(str6))
# print(str6.index("P"))
# print(str6.index("L"))
# print(str6.index("Z"))   #ValueError: substring not found

    # .rindex()
# print(str6.rindex("P"))
# print(str6.rindex("X"))    #ValueError: substring not found

#     # .find()
# print(str6.find("P"))
# print(str6.find("Z"))     # -1  => default value when char is not found.

#     # .rfind()
# print(str6.rfind("P"))
# print(str6.rfind("X"))   # -1   => default value when char is not found.

#----------------------------------------------------

# # is methods: (True/ False)

#     # .isalpha()
# str1 = "aasdfg."
# print(str1.isalpha())

#     # .isdigit()
# str2 = "1234578@"
# print(str2.isdigit())

#     # .isupper()
# str3 = "123@#$ASDFGf"
# print(str3.isupper())

#     # .islower()
# str4 = "1234%^&dfghA"
# print(str4.islower())

#     # .istitle()
# str5 = "Apple is Great"
# print(str5.istitle())

#     # .isalnum()
# str6 = "1234"
# print(str6.isalnum())
# str7 = "sdfghj"
# print(str7.isalnum())
# str8 = "dfgh345"
# print(str8.isalnum())
# str9 = "234sdfgh "
# print(str9.isalnum())

#     # .isspace()
# str10 = "    "
# print(str10.isspace())

#-----------------------------------

# l1 = ["A", "M", "A", "N", "O", "R", "A"]

# str1 = ""
# str1 = str1.join(l1)
# print(str1)

# ----------------------------------------
# Some other operations of string:

# Concatination:
# s1 = "Hello"
# s2 = "World"

# s3 = s1+" "+s2
# print(s3)

# Repetation
# s1 = "Bye"
# print(s1 * 3)

