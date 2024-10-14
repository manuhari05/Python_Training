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
