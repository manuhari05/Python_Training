def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

num=int(input("Enter a number:"))
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of",num,"is",fact(num))

# for i in range(1,num+1):
#     print("The factorial of", i, "is", fact(i))


