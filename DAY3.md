

# Day 3 Date: 11/10/2024

### Overview
Three Python functions aimed at solving common programming problems: checking for palindromes, finding the majority element in a list, and calculating the maximum profit from a list of prices.

---

### 1. Palindrome Checker



**Purpose**: To determine if a given string is a palindrome, considering only alphanumeric characters and ignoring case.

**Code**:
```python
def check_palindrome(s):
    ss = ''
    for i in s:
        if i.isalnum():
            ss += i.lower()

    if ss == ss[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

# Example usage
str1 = "Malayalam"
op = check_palindrome(str1)
print(op)  # Output: Palindrome
```
### Explanation:
- The function iterates through the input string, filtering out non-alphanumeric characters and converting the remaining characters to lowercase.
- It checks if the filtered string reads the same forwards and backwards.

# 2. Majority Element Finder


**Purpose**: To identify the element that appears most frequently in a given list.

**Code**:

```python
def majority_element(l):
    c_dict = {}
    for i in l:
        if i not in c_dict.keys():
            c_dict[i] = l.count(i)

    l1 = list(c_dict.values())
    l2 = []
    for k, v in c_dict.items():
        if max(l1) == v:
            l2.append(k)
    return l2

# Example usage
main_l = [2, 1, 2, 3, 2, 1, 1]
op = majority_element(main_l)
print(op)  # Output: [2]
```
### Explanation:
- The function creates a dictionary to count occurrences of each element in the list.
- It then identifies the elements with the maximum count and returns them.

# 3. Maximum Profit 


**Purpose**: To calculate the maximum profit that can be made from a list of prices, where you can buy and sell once.

**Code**:
```python
def best_profit(l):
    max1 = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] - l[i] > max1:
                max1 = l[j] - l[i]
    return max1

# Example usage
l1 = [2, 7, 5, 1]
op = best_profit(l1)
print(f"profit {op}")  # Output: profit 5
```


### Explanation:
- The function uses nested loops to check all possible pairs of buying and selling prices.
- It calculates the potential profit for each pair and keeps track of the maximum profit found.