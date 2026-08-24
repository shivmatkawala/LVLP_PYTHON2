# Set :

    # Set is also a collection datatype
    # Set is partially herogeneous (it only contains immutable data)
    # Set itself is mutable

    # Set is unordered datatype
    # Set doesnt support indexing
    # Set Set allows only unique elements

    # Set is created using {}

#--------------------------------------------
# How to create a set:

# s1 = {1}
# print(s1)
# print(type(s1))

# s2 = {1, 2.2, 3+6j, "apple", False, (1, 2, 3, 4)}
# print(s2)
# print(type(s2))

# s3 = {12, 34, 56, 12, 89, 0, 5, 12}
# print(s3)
# print(type(s3))

# s4 ={12, 9.5, True, (11, 22, 33)}
# print(s4)
# print(type(s4))


#-----------------------------------------

# set1 = {34, 12, 89, 0, 45, 67, 33}
# print(set1)

# --------------------------------------
# Set In-Built Methods:

# s1 = {1, 2, 3, 4}
# s1.add(5)       # new element will be added
# s1.remove(3)     # specified element will be removed
# s1.pop()          # any random number will be removed
# s1.clear()

# print(s1)

#----------------------------------------
# Set Operations:
# s1 = {1, 2, 3, 4}
# s2 = {4, 5, 6, 7}

# Union  (|, .union())
# s3 = s1.union(s2)
# s4 = s1 | s2
# print(s3)
# print(s4)


# Difference (-, .difference())
# s3 = s1.difference(s2)
# s4 = s2.difference(s1)
# print(s3)
# print(s4)

# s3 = s1 -s2
# s4 = s2-s1
# print(s3)
# print(s4)

# Intersection (&, .intersection())
# s3 = s1 & s2
# s4 = s1.intersection(s2)

# print(s3)
# print(s4)


#------------------------------------------------
# Updates

# s1.update(s2)
# s1.difference_update(s2)
# s1.intersection_update(s2)


# print(s1)
# print(s2)
#---------------------------------

# superset and subset:

# s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}  # Superset of s2
# s2 = {3, 7, 0}   # Subset of s1

# print(s1.issuperset(s2))
# print(s2.issubset(s1))

# print(s1.issubset(s2))
