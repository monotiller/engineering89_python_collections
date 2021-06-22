# Let's create a shopping list
# Syntax: name_of_list = ["item1", "item2"]

shopping_list = ["apples", "eggs", "dark chocolate", "tea"]
print(shopping_list)
# Checking the type of this data with type()
print(type(shopping_list))

# How can we access "dark chocolate"?
print(shopping_list[2]) # Will display "dark chololate". Indexing still starts from 0
print(shopping_list[-1]) # Still prints the last value of the list

# How can we replace an item in the list?
shopping_list[0] = "mango"
print(shopping_list)

# How can we add an item to our shopping list?
shopping_list.append("tuna")
print(shopping_list)

# How could we delete an item on index 3 from this list?
shopping_list.pop(3)
print(shopping_list)

# We can have multiple data types in the same list
mix_list = [1, 2, 3, "one", "two", "three"] # Integers and strings in here
print(mix_list)

# Let's check out tuples
# Syntax name_of_tuple = {"item1", "item2"}
essentials = {"paracetamol", "milk", "butter"}
print(essentials)
print(type(essentials))
essentials.pop(1)
print(essentials)