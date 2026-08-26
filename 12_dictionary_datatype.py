# Dictionary:

    # age = 45
    # ages = [12, 32, 23, 34, 44, 45, 65, 89]
    # ages = {"Anant": 12, "Anil": 32, "Avinash": 23, "Radha":34, "Kumar": 44, "Sandhya":45}

    # NOTE Dictionary is a key-value pair collection

fruit_prices = {
    "Apple": 200,
    "Grapes": 100,
    "Mango": 150,
    "Sitafal": 90
}

# print(fruit_prices)
# print(type(fruit_prices))

# # Get the keys
# print(list(fruit_prices.keys()))   #['Apple', 'Grapes', 'Mango', 'Sitafal']

# # Get the values
# print(list(fruit_prices.values()))

#-----------------------------------------------------------------

# How to access a value from dictionary:
# NOTE dictionary doesnt support numeric indexing
# but it supports key base indexing

# print(fruit_prices["Mango"])
# print(fruit_prices["Sitafal"])

# In-built Methods:

# How to add a ne key-value pair in dictionary 
fruit_prices["Pineapple"] = 60

# print(fruit_prices)

# How to update the value of existing key-value
# fruit_prices["Mango"] = 300

# print(fruit_prices)

# wants to add multiple key value pairs

new_fruits = {
    "avocado": 500,
    "dragon fruit": 200,
    "Jamakay": 120,
    "Coconut": 50
}

fruit_prices.update(new_fruits)
# print(fruit_prices)

#----------------------------------------------------------

# .get()
# print(fruit_prices.get("Jamakay"))

# .pop()  => to remove a key value pair
fruit_prices.pop("avocado")
# print(fruit_prices)

# .popitem()  => removes last key-value pair
fruit_prices.popitem()
# print(fruit_prices)

# .copy() => to create a shallow copy
indina_fruits = fruit_prices.copy()
# print(indina_fruits)

#---------------- CREATE DICTIONARIES FROM:

# student_list = ["Kiran", "Amit", "Jaya", "Radha"]
# marks = [67, 78, 87, 89]

# student_marks = dict(zip(student_list, marks))
# print(student_marks)


# material = ["Tape-rcorder", "Mobile", "Laptop", "TV"]

# matrial_categories = dict.fromkeys(material, "Electronics")
# print(matrial_categories)

