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
