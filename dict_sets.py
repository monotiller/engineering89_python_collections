# Dictionaries and Sets both are data collections in python
# Dict?
# Sets?
#
# Dict are another way to manage data but can be a little more dynamic
# Dict work as a KEY AND VALUE
# KEY = reference of the object
# VALUE = what the data storage mechanism you wish to use
# Dynamic as we have lists, and another dict inside a dict
# Syntax - name = {}
# We use {} brackets to declare a dict
# key = value

# key
students_1 = {
    "name": "James",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["data types", "git and github", "operators", "lists and tuples"]
}
#Let's check if we have got the syntax correct and print the dict
print(students_1)
print(type(students_1))
print(students_1["stream"]) # To print a specific value, we can reference the key like this
print(students_1["completed_lessons_names"][1])

# print the second last index of key completed_lessons_names:[]
print(students_1["completed_lessons_names"][-2])

# Could we apply CRUD on a dict?
# How can we cahnge the value of any key in our dict?
students_1["completed_lessons"] = 3
print(students_1["completed_lessons"])

# Let's see how can we remove an item from our completed lessons names
students_1["completed_lessons_names"].remove("operators")
print(students_1["completed_lessons_names"])

# We have some built in methods that we can use with dict
# To print all the keys keys()
print(students_1.keys())

# To print all the values()
print(students_1.values())

# Sets are also data collection
# Syntax name = {"", "", ""}
# What is the difference between sets and dict
# Sets are unordered
shopping_list = ["eggs", "tea", "milk"]
car_part = {"engine", "wheels", "window"}
print(shopping_list)
print(car_part)

# Can we add anything to a set?
car_part.add("seats")
print(car_part)

# Can we remove?
car_part.remove("wheels")
print(car_part)