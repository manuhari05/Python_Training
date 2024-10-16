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


# for i in range(1,num+1):
#     print("The factorial of", i, "is", fact(i))


