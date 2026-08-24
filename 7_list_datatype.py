# List:
    # List is a collection datatype
    # Lis is created using []
    # List is mutable (can be modified)
    # List is heterogenous (can contain variety of data)
    # List is ordered datatype
    # list supports indexing

# Create a list of students

# students = ["Ajay", "Sara", "David", 'Preti']
# print(students)
# print(type(students))

# marks = [45, 55, 66, 77]
# print(marks)
# print(type(marks))

# heights = [1.23, 1.44, 1.56, 1.53]
# print(heights)
# print(type(heights))

#---------------------------------------------------

# List Indexing:

# l1 = [12, 23, 34, "A", True, 1.23, 5+7j, [1, 2, 3], ("a", "b", "c"), {"@", "#", "$"}]
# print(l1)
# print(type(l1))

#---------------Indexing:

# l2 = [23, 34, 45, 56, 67, 78]
# print(l2[0])
# print(l2[3])

# print(l2[-6])
# print(l2[-3])

# ----------------Slicing
# [Start_index: End_Index: Step]

# l3 = [56, 43, 45, 78, 98, 90]
# print(l3[0:4:1])
# print(l3[2::1])
# print(l3[0::2])
# print(l3[-1:-4:-1])

#-------------------------------------------------
# List In built methods:

l1 = [11, 222, 33, 44, 55, 66, 77, 88, 990, 9009]

    # Insertion methods:
        # .append()  ==> it will add new element at the end of list
# l1.append(1000)

        # .extend() ==> it will add multiple elements at the end of list
# l1.extend([1, 2, 3, 4, 5, 6])

        # .insert() => it will add element at specific index number
# l1.insert(0, 500)
# l1.insert(5, 600)

# print(l1)

        # deletion methods
            # .pop() => it ll delete last element of the list
# l1.pop()
# l1.pop()
            # .remove()  => it ll delete the element which is asked
# l1.remove(222)
# l1.remove(66)

            # .clear() => whloe elements from list ll be deleted
# l1.clear()

# print(l1)

#----------------------------------------

l2 = [23, 12, 56, 5, 4, 90, 1, 3, 78, 1]

# print(l2.count(1))
# print(l2.index(90))
# l3 = l2.copy()
# print(l3)

# l2.sort(reverse=True)
# print(l2)  #[1, 1, 3, 4, 5, 12, 23, 56, 78, 90]
# l2.reverse()
# print(l2)
