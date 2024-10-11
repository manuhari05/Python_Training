# DAY 1 09/10/2024

# Python Data Types and Methods

## 1. Numeric Types
### a. Integer (`int`)
Represents whole numbers.

### b. Float (`float`)
Represents floating-point numbers.

### c. Complex (`complex`)
Represents complex numbers.

### Example:
```python
num_int = 5
num_float = 3.14
num_complex = 2 + 3j
# <class 'int'> <class 'float'> <class 'complex'>
print(type(num_int), type(num_float), type(num_complex))  

```
##  2. String (str)
Represents a sequence of characters.
### Methods:

- **capitalize()**: Converts the first character to uppercase.
- **count(value)**: Counts occurrences of value.
- **find(value)**: Returns the index of value.
- **replace(old, new)**: Replaces occurrences of old with new.
- **split(separator)**: Splits the string into a list.
- **join(iterable)**: Joins elements of iterable into a string.
- **lower()**: Converts the string to lowercase.
- **upper()**: Converts the string to uppercase.
- **strip()**: Removes leading and trailing whitespace.
- **startswith(value)**: Returns True if the string starts with value.

### Examples
 ```python
 s = "  hello world  "
print(s.capitalize())             # "  Hello world  "
print(s.count('o'))               # 2
print(s.find('l'))                # 2
print(s.replace('world', 'Python'))  # "  hello Python  "
print(s.split(' '))               # ['', 'hello', 'world', '']
print(", ".join(['apple', 'banana']))  # "apple, banana"
print(s.lower())                  # "  hello world  "
print(s.upper())                  # "  HELLO WORLD  "
print(s.strip())                  # "hello world"
print(s.startswith('hello'))      # False
```
## 3. List (list)
Ordered collection of elements.

### Methods:
- **append()**: Adds an element at the end.
- **remove(value)**: Removes the first occurrence of value.
- **sort()**: Sorts the list.
- **insert(index, value)**: Inserts value at index.
- **pop(index)**: Removes and returns the element at index.
- **reverse()**: Reverses the list.
- **extend(iterable)**: Extends the list by appending elements from iterable.
- **clear()**: Removes all elements.
- **copy()**: Returns a shallow copy of the list.

### Examples
```python
lst = [3, 1, 4]
lst.append(2)                   # [3, 1, 4, 2]
lst.remove(1)                  # [3, 4, 2]
lst.sort()                     # [2, 3, 4]
lst.insert(1, 5)               # [2, 5, 3, 4]
print(lst.pop(0))              # 2; lst becomes [5, 3, 4]
lst.reverse()                  # [4, 3, 5]
lst.extend([6, 7])             # [4, 3, 5, 6, 7]
print(lst.copy())              # [4, 3, 5, 6, 7]
lst.clear()                    # []
```

## 4. Tuple (tuple)
Ordered, immutable collection of elements.

## Methods:
- **count(value)**: Counts occurrences of value.
- **index(value)**: Returns the index of value.
- **len()**: Returns the length of the tuple.
- **max()**: Returns the largest item.
- **min()**: Returns the smallest item.

### Examples
 ```python
 tup = (1, 2, 2, 3)
print(tup.count(2))            # 2
print(tup.index(3))            # 3
print(len(tup))                # 4
print(max(tup))                # 3
print(min(tup))                # 1
 ```


## 5. Dictionary (dict)
Collection of key-value pairs.

### Methods:
- **get(key)**: Returns value for key.
- **keys()**: Returns a view of keys.
- **pop(key)**: Removes and returns value for key.
- **update(other_dict)**: Updates the dictionary with key-value pairs from another dictionary.
- **items()**: Returns key-value pairs as tuples.
- **setdefault(key, default)**: Returns value for key, inserting key with default if not present.
- **clear()**: Removes all items.
- **copy()**: Returns a shallow copy of the dictionary.

### Examples
```python
d = {'a': 1, 'b': 2}
print(d.get('a'))              # 1
print(d.keys())                # dict_keys(['a', 'b'])
print(d.pop('b'))              # 2
d.update({'c': 3})             # {'a': 1, 'c': 3}
print(d.items())               # dict_items([('a', 1), ('c', 3)])
print(d.setdefault('d', 4))    # 4; d becomes {'a': 1, 'c': 3, 'd': 4}
d.clear()                      # {}
```

## 6. Set (set)
Unordered collection of unique elements.

### Methods:
- **add(value)**: Adds an element.
- **remove(value)**: Removes the specified element.
- **union(other)**: Returns the union of sets.
- **intersection(other)**: Returns the intersection of sets.
- **difference(other)**: Returns the difference between sets.
- **discard(value)**: Removes an element if it exists.
- **pop()**: Removes and returns an arbitrary element.
- **clear()**: Removes all elements.

### Examples
```python 
s = {1, 2, 3}
s.add(4)                       # {1, 2, 3, 4}
s.remove(2)                   # {1, 3, 4}
s2 = {3, 4, 5}
print(s.union(s2))             # {1, 2, 3, 4, 5}
print(s.intersection(s2))       # {3, 4}
print(s.difference(s2))         # {1}
s.discard(3)                  # {1, 4}
print(s.pop())                 # Removes an arbitrary element (1 or 4)
s.clear()                     # set()

```

## 7. Boolean (bool)
Represents True or False values.

### Examples
```python
true_value = True
false_value = False
print(type(true_value), type(false_value))  # <class 'bool'> <class 'bool'>
```

## 8. None Type
Represents a null value or no value at all.

### Examples
```python
none_value = None
print(type(none_value))  # <class 'NoneType'>
```

# Type Casting
Convert one data type into another.

### Examples
```python
num_str = "123"
num_int = int(num_str)       # 123
num_float = float(num_str)    # 123.0
```

