# Day 5 : 15/10/2024

## 1.Python Program to Compute Factorial of a Number

The code defines a recursive function to calculate the factorial of a non-negative integer. It prompts the user for input, checks if the input is negative or zero, and then computes and displays the factorial for positive integers using the recursive fact function.

```python
def fact(n):
    # Base case: if n is 0, return 1 (0! is 1)
    if n == 0:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * fact(n-1)

# Get user input and convert it to an integer
num = int(input("Enter a number:"))

# Check if the input number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
# Check if the input number is 0
elif num == 0:
    print("The factorial of 0 is 1")
# If the input number is positive, calculate and print its factorial
else:
    print("The factorial of", num, "is", fact(num))
```

## 2.Roman Numeral Converter
This code defines a function i_r(n) that converts a given integer n into its Roman numeral representation. It uses a mapping of Roman numerals to their integer values, iteratively appending the appropriate symbols to the result string based on the input number. The program prompts the user for an integer input and then outputs the corresponding Roman numeral.

```python
def i_r(n):
    # Mapping of Roman numerals to their integer values
    r=[["M",1000],["CM",900],["D",500],["CD",400],["C",100],["XC",90],["L",50],["XL",40],["X",10],["IX",9],["V",5],["IV",4],["I",1]]
    
    # Initialize an empty string to build the Roman numeral
    result=""
    
    # Iterate through the list of Roman numeral mappings
    for i in r:
        # While n is greater than or equal to the current numeral's value
        while n>=i[1]:
            # Append the Roman numeral to the result
            result+=i[0]
            # Subtract the numeral's value from n
            n-=i[1]
            
     # Return the constructed Roman numeral string
    return result


inp1=int(input("Enter a number: "))

 # Print the Roman numeral representation of the input
print(f"The {inp1} in integer in {i_r(inp1)}")

```

## 3.Word Reversal Class
This code defines a Word class that can reverse the order of words in a given string. It initializes with a word and contains a method reverse() that splits the string into individual words, reverses their order, and then joins them back into a single string. An instance of the class is created with the string "hello world" ,and the reversed result is printed.

```python
class Word:
    def __init__(self, word):
        # Initialize the class with a word
        self.word = word

    def reverse(self):
        # Split the word into a list of words
        word = self.word
        # Split the string into words
        l = word.split()  
         # Reverse the order of the words
        l.reverse()  

        # Join the reversed list back into a string
        return ' '.join(l)  

# Create an instance of the Word class with the string 'hello world'
word = Word('hello world')
# Call the reverse method to reverse the order of words
reversed_word = word.reverse()
# Print the reversed word string
print(reversed_word)  # Output: 'world hello'
```
## 4.Remove Duplicates with Maximum Two Occurrences

This code defines a function r_d(l) that removes excess duplicates from a sorted list, ensuring that each element appears at most twice. The list is first sorted, and then the function iterates through the list to check if any element occurs more than twice. If it does, it removes the extra occurrences and appends a placeholder (underscore) to maintain the list's length. The modified list is then returned and printed.

```python
def r_d(l):
    # Sort the list in ascending order
    l.sort() 
    n=len(l) 
    # Iterate through the list, stopping before the last two elements
    for i in range(len(l) - 2):
        # Check if the current element is equal to the element two positions ahead  
        while l[i] == l[i + 2]:  
            # Remove the duplicate element
            l.remove(l[i]) 
            if l[i]=="_":
                break 
            # Append a placeholder to maintain list length
            l.append("_")  
        while len(l)<n:
            l.append("_")
            
    return l  # Return the modified list

# Input list with duplicates
list1 = [0, 1, 1, 1, 2, 2, 3, 3, 3]
# Call the function to remove excess duplicates
op = r_d(list1)
# Print the modified list with duplicates removed
print(f"Removed sorted duplicate list {op}")
```
## 5.Rotate the array

This code defines a function **rotate_array(l, k)** that rotates a given list **l** to the right by **k** positions. The function uses a loop to remove the last element of the list and insert it at the beginning. This process is repeated **k** times. Finally, the modified list is returned and printed.

```python

def rotate_array(l, k):
    # Rotate the array k times
    for _ in range(k):
        # Remove the last element from the list
        last = l.pop() 
        # Insert the removed element at the beginning of the list 
        l.insert(0, last)
    # Return the modified list  
    return l  

# Input list to be rotated
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
 # Number of positions to rotate
rt = 3 
# Call the function to rotate the array
op = rotate_array(list1, rt)
# Print the rotated array
print(f"The rotated array is {op}")
```