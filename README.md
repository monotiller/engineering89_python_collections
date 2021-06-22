# Introduction to python collections
## Types
- Lists
- Tuples
- Dict
- Sets

### Lists
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