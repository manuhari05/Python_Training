# DAY 2:10/10/2024
# Problem Solving in Python

## Problem 1: Sorting a List Without Using `sort()`

To sort a list without using the built-in `sort()` method, we can implement the Bubble Sort algorithm. This algorithm repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

### Example Code:
```python
# Initialize a list of integers
list1 = [1, 4, 2, 3, 7, 5]
print(f"The given list is: {list1}")

# Bubble Sort algorithm
for i in range(len(list1)):
    for j in range(len(list1) - 1):
        # If the current element is greater than the next element, swap them
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

# Print the sorted list
print(f"The sorted list is: {list1}")
```

### Explanation:
- The outer loop iterates through each element in the list.
- The inner loop compares adjacent elements and swaps them if necessary.
- The process continues until the entire list is sorted.

## Problem 2: Finding the Longest Common Prefix Using Sorting
To find the longest common prefix among a list of strings, we can sort the list and then compare the first and last strings. The longest common prefix will be the characters they share from the beginning.
### Example code:
```python
# List of strings to find the longest common prefix
li = ["door", "dog", "done"]

# Check if the list is empty
if not li:
    print("empty list")
else:
    # Sort the list of strings
    li.sort()
    
    # Take the first and last string in the sorted list
    first = li[0]
    last = li[-1]
    Long_prefix = ''

    # Compare characters of the first and last string
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            Long_prefix += first[i]  # Add the matching character to the prefix
        else:
            break  # Stop when characters differ

    # Print the longest common prefix found
    print(f"The longest prefix is: {Long_prefix}")
```

### Explanation:
- The list is checked for emptiness, and a message is printed if it is empty.
- The list is sorted to arrange the strings in order.
- The code compares the first and last strings in the sorted list to find matching characters.
- The common prefix is built until a character mismatch occurs, and the result is printed.

## Problem 3: Finding the Longest Common Prefix Without Using sort()
We can also find the longest common prefix without sorting by comparing each string with a base string and gradually trimming the prefix.

### Example code:
```python
# List of strings to find the longest common prefix
li=["door","dog","done"]

# Initialize variables for tracking the longest prefix
Long_prefix=''

# Check if the list is empty
if not li:
    print("empty list") 
else:
    # Check if the list is empty
    for i in range(len(li)):

         # Start with the current string as the initial prefix
        prefix=li[i]

        # Flag to control the loop
        t=True

        # Compare the current prefix with each string in the list
        for j in li:
            if j == li[i]:
                # Skip comparison with itself
                continue
            while t:
                
                # print(prefix)
                if not j.startswith(prefix):

                    # If the current string does not start with the prefix, Reduce the prefix by one character from the end
                    prefix=prefix[:-1]
                    
                else :
                    # Exit the inner loop if prefix matches
                    t=False

            # Update the longest prefix if the current one is longer
            if len(Long_prefix)<=len(prefix):
                Long_prefix=prefix

                
    print(f"the longest prefix is: {Long_prefix}")
```
### Explanation:
- The code initializes the longest prefix with the first string.
- It checks if the list is empty, and if so, prints a message.
- The code iterates through the remaining strings, trimming the longest prefix until it matches the start of each string.
- Finally, it prints the longest common prefix found.