# Day 4: 14/10/2024


## 1. Best Profit from Stock Prices

This program calculates the maximum profit that can be obtained by buying and selling stocks. It iterates through a list of stock prices and adds up the profits from any upward price movements. The function also prints the buying and selling prices that contribute to the profit.

```python
def best_profit(l):
    # Initialize the maximum profit variable to 0
    max1 = 0
    
    # Iterate through the list using two nested loops
    for i in range(len(l) - 1):
        if l[i + 1] - l[i] > max1:
            print(l[i], l[i + 1])  # Print the buying and selling prices
            # Add the profit to the total maximum profit
            max1 += l[i + 1] - l[i]
               
    # Return the maximum profit found
    return max1  

l1 = [2, 7, 5, 1, 8]
# Call the function and print the result
op = best_profit(l1)
print(f"profit {op}")
```

## 2. Prime Numbers in a Given Range

This program prompts the user to input two numbers and then finds all prime numbers between them. It uses a set to store unique prime numbers and checks each number in the range for primality by testing divisibility. The user can repeat the process as desired.

```python
while True:
    def prime_numbers(n1, n2):
        # Initialize an empty set to store prime numbers
        prime = set()
        
        # Iterate through the range from n1 to n2 (inclusive)
        for i in range(n1, n2 + 1):
            # Check if the number is greater than 1
            if i > 1:
                # Special case for the number 2, which is prime
                if i == 2:
                    prime.add(i)
                # Check for factors from 2 to i-1
                for j in range(2, i):
                    # If i is divisible by j, it is not a prime number
                    if (i % j) == 0:
                        break
                else:
                    # If no factors were found, i is a prime number
                    prime.add(i)
        
        # Print the set of prime numbers found in the range
        print("Prime numbers between", n1, "and", n2, "are:", prime)
    
    # Input: First number of the range
    n1 = int(input("Enter the first number : "))
    # Input: Second number of the range
    n2 = int(input("Enter the second number : "))
    # Call the function to find prime numbers in the specified range
    prime_numbers(n1, n2)
    print("\n")
    
    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    # If the user does not want to continue, break the loop
    if choice.lower() != 'y':
        break
```


## 3. Prime Numbers Generator

This version uses a generator to yield prime numbers in a specified range. Instead of returning a list, it yields one prime number at a time, allowing for memory-efficient processing. The program takes user input for the range and prints the first three prime numbers found.

```python
def prime_numbers(n1, n2):
    # Iterate through the range from n1 to n2 (inclusive)
    for i in range(n1, n2 + 1):
        # Check if the number is greater than 1
        if i > 1:
            # Special case for the number 2, which is prime
            if i == 2:
                # Yield 2 as a prime number
                yield i  
            # Check for factors from 2 to i-1
            for j in range(2, i):
                # If i is divisible by j, it's not a prime number
                if (i % j) == 0:
                    break  # Exit the loop if a divisor is found
            else:
                yield i  # If no divisors were found, yield i as a prime number
                break  # Exit the loop after yielding

# Input: First number of the range
n1 = int(input("Enter the first number : "))
# Input: Second number of the range
n2 = int(input("Enter the second number : "))
# Create a generator object for prime numbers in the specified range
op = prime_numbers(n1, n2)
# Print the first prime number yielded by the generator
print(next(op))
# Print the second prime number yielded by the generator
print(next(op))
# Print the third prime number yielded by the generator
print(next(op))

```

## 4. Prime and Fibonacci Class

This program defines a class Prime_fibb that computes both prime numbers and Fibonacci numbers up to a given input. It contains methods to check for primality, generate a list of primes, and produce the Fibonacci series. The user is prompted to enter a number, and the program displays both prime numbers and Fibonacci numbers within that range.

```python
class Prime_fibb:
    def __init__(self, number):
        # Initialize the class with the given number
        self.number = number
        
    def is_prime(self, n):
        # Check if the number n is prime
        if n < 2:  
            # Prime numbers are greater than or equal to 2
            return False
        # Check for factors from 2 up to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:  
                # If n is divisible by any i, it's not prime
                return False
        # If no divisors were found, n is prime
        return True  
    
    def prime(self):
        # Create a list to hold prime numbers
        primes = []
        # Iterate through numbers from 2 to the given number
        for i in range(2, self.number + 1):
            # Check if i is prime
            if self.is_prime(i):
                # Add i to the list of primes  
                primes.append(i)  
        
         # Return the list of prime numbers
        return primes 

    def fibb(self):
        # Initialize a list to hold Fibonacci numbers, starting with 0 and 1
        c = [0, 1]
        a, b = 0, 1
        # Generate Fibonacci numbers while b is less than the given number
        while b < self.number:
            # Update a and b to the next Fibonacci numbers
            a, b = b, a + b  
            if b > self.number:  
                # If the next Fibonacci number exceeds the limit, break
                break
            # Append the Fibonacci number to the list
            c.append(b)  
        # Return the list of Fibonacci numbers
        return c  

# Input: Get a number from the user
num = int(input("Enter a number: "))
# Create an instance of the Prime_fibb class with the user's number
op = Prime_fibb(num)
# Print the list of prime numbers within the range
print(f"The prime numbers within a range {num} are {op.prime()}")
# Print the Fibonacci series up to the user's number
print(f"The Fibonacci series of {num} is {op.fibb()}")

```

## 5. Fibonacci Series Generator

This program generates Fibonacci numbers up to a specified target using a generator function. It yields each Fibonacci number in the sequence until the target value is reached. The user inputs a target number, and the program prints all Fibonacci numbers less than that target.

```python
def fibb(target):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # Continue generating Fibonacci numbers while a is less than the target
    while a < target:
        # Yield the current Fibonacci number
        yield a
        # Update a and b to the next two Fibonacci numbers
        a, b = b, a + b

# Input: Get the target number from the user
num = int(input("Enter the number: "))
# Create a generator object for Fibonacci numbers up to the target number
op = fibb(num)

# Iterate through the generated Fibonacci numbers and print them
for i in op:
    print(i, end=" ")  # Print each Fibonacci number in the same line

```