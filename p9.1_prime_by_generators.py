def prime_numbers(n1, n2):
    # Iterate through the range from n1 to n2 (inclusive)
    for i in range(n1, n2 + 1):
        # Check if the number is greater than 1 (only numbers > 1 can be prime)
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
