def check_palindrome(s):
    # Initialize an empty string to store the filtered characters
    ss = ''
    
    # Iterate through each character in the input string
    for i in s:
        # Check if the character is alphanumeric
        if i.isalnum():
            # Convert the character to lowercase and add it to the filtered string
            ss += i.lower()

    # Check if the filtered string is equal to its reverse
    if ss == ss[::-1]:
        # Return "Palindrome" if they are the same
        return "Palindrome"  
    else:
         # Return "Not a Palindrome" otherwise
        return "Not a Palindrome" 


str1 = "Malayalam"
# Call the function and print the result
op = check_palindrome(str1)
print(op) 
