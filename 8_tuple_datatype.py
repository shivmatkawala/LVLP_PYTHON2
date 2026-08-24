# Tuple:-

    # Tuple is also a collection datatype
    # Tuple is immutable (Cant be modified)
    # Tuple is heterogeneous (can contain variety of type data)
    # Tuple is ordered datatype
    # Tuple supports indexing
    # Tuple is created using ()

# How to create a tuple:

# tup1 = ()
# print(tup1)
# print(type(tup1))

# tup2 = (1, 2, 3, 4, 5)
# print(tup2)
# print(type(tup2))

# tup3 = (1, 2, 3.3, 4.4, 5+7j, True, "Apple", [11, 22, 33], (100, "A", "B"))
# print(tup3)
# print(type(tup3))

#--------------------------------------------------

# Indexing on tuple:

# t1 = (11, 22, 33, 44, 55, 66, 77, 88, 99, 111, 222)
# print(t1[4])
# print(t1[-7])

# print(t1[-3])
# print(t1[8])

#-----------------------------------------
# Slicing:
# print(t1[0:5:1])
# print(t1[5::1])
# print(t1[-3:-8:-1])
# print(t1[0::3])
# print(t1[-1::-4])

#-------------------------------------------

# -------- In-Built Methods:

    # .count()  ==> From a tuple if you want to count an appearances of a particular element 

t2 = (2, 4, 3, 66, 77, 34, 2, 1, 9, 0, 2, 5, 2)
# print(t2.count(2))
# print(t2.count(66))

    # .index()  ==> to get the index of an element

# print(t2.index(66))
# print(t2.index(2))


#--------------------------------
# Tuple some other operations
# x, y, z = (1, 2, 3)   # Packing and unpacking
# print(x)
# print(y)
# print(z)