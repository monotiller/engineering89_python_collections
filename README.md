# Introduction to python collections
## Types
- Lists
- Tuples
- Dict
- Sets

## Lists
A.K.A. arrays in other languages
- Shopping list - multiple items
- add, edit, delete, update
- CRUD
    - Create
    - Read
    - Update
    - Delete

Syntax:
```python
name_of_list = ["item1", "item2"]
```
Here's a sample list:
```python
shopping_list = ["apples", "eggs", "dark chocolate", "tea"]
```
How can we access "dark chocolate"?
```python
print(shopping_list[2]) # Will display "dark chololate". Indexing still starts from 0
print(shopping_list[-1]) # Still prints the last value of the list
```
How can we replace an item in the list?
```python
shopping_list[0] = "mango" # = ['mango', 'eggs', 'dark chocolate', 'tea']
```
How can we add an item to our shopping list?
```python
shopping_list.append("tuna") # = ['mango', 'eggs', 'dark chocolate', 'tea', 'tuna']
```
How could we delete an item on index 3 from this list?
```python
shopping_list.pop(3) # = ['mango', 'eggs', 'dark chocolate', 'tuna']
```
We can have multiple data types in the same list
```python
mix_list = [1, 2, 3, "one", "two", "three"] # Integers and strings in here
```
## Tuples
But what are the difference between lists and tuples?

Because tuples are immutable, they can't be altered. That means they aren't the right choice when you need to loop over data and append it to a data structure.

Syntax:
```python
name_of_tuple = {"item1", "item2"}
```
Here's a tuple:
```python
essentials = {"paracetamol", "milk", "butter"}
```
So, here's something you can't do:
```python
essentials.pop(1)
```
```commandline
Traceback (most recent call last):
  File "/Users/monotiller/Developer/Sparta Global/engineering89_python_collections/Lists_Tuples.py", line 34, in <module>
    essentials.pop(1)
TypeError: set.pop() takes no arguments (1 given)
```
These are immutable so you cannot change the data once the program starts running. You will just recieve an error if you try to manipulate the data.

## Dictionaries
Dictionaries and Sets both are data collections in python

Dict? Sets?
- Dict are another way to manage data but can be a little more dynamic
- Dict work as a KEY AND VALUE
- KEY = reference of the object
- VALUE = what the data storage mechanism you wish to use
- Dynamic as we have lists, and another dict inside a dict

Syntax:
```python
name = {
    "key": "value",
}
```
We use {} brackets to declare a dict. Here's a dictionary:
```python
students_1 = {
    "name": "James",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["data types", "git and github", "operators", "lists and tuples"]
}
```
Then when we print it:
```commandline
{'name': 'James', 'stream': 'DevOps', 'completed_lessons': 4, 'completed_lessons_names': ['data types', 'git and github', 'operators']}
```
To print a specific value, we can reference the key like this:
```python
print(students_1["stream"]) # = "DevOps"
print(students_1["completed_lessons_names"][1]) # = "git and github"
```
Could we apply CRUD on a dict?

How can we cahnge the value of any key in our dict?
```python
students_1["completed_lessons"] = 3
print(students_1["completed_lessons"]) # = 3
```

Let's see how can we remove an item from our completed lessons names
```python
students_1["completed_lessons_names"].remove("operators")
print(students_1["completed_lessons_names"]) # = ['data types', 'git and github', 'lists and tuples']
```
We have some built in methods that we can use with dict
To print all the keys keys()
```python
print(students_1.keys())
```
To print all the values()
```python
print(students_1.values())
```
## Sets
Sets are also data collection

Syntax:
```python
name = {"", "", ""}
```
What is the difference between sets and dict? Sets are unordered
```python
shopping_list = ["eggs", "tea", "milk"]
car_part = {"engine", "wheels", "window"}
print(shopping_list) # Always in the order: ['eggs', 'tea', 'milk']
print(car_part) # Can print in any order: {'wheels', 'window', 'engine'} or {'engine', 'wheels', 'window'}
```
Can we add anything to a set?
```python
car_part.add("seats")
print(car_part) # = {'seats', 'engine', 'wheels', 'window'}
```
Can we remove?
```python
car_part.remove("wheels")
print(car_part) # = {'window', 'engine', 'seats'}
```