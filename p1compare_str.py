# Input string containing brackets
s="{[([])]}"

# List of adjacent bracket pairs
adj = ['[]','{}','()']

# Dictionary for mapping opening brackets to their corresponding closing brackets
d={"{":"}","(":")","[":"]",}


# Function to check if the bracket sequence is balanced
def c_s_b(a):
    # Initialize iteration counter
    i=0

    # Continue until the string is empty
    while (len(a)>0):
        i+=1

         # Check for unbalanced conditions     
        if len(a)==1 or i>len(a)  :
            return "Unbalanced"
        # for k , v in d.items():   # Uncomment these to lines to replace the adjacent pairs using dictionary
        #     a=a.replace(k+v,"")

        # Remove adjacent pairs of brackets
        for j in adj:
            # Replace adjacent bracket pairs with an empty string
            a=a.replace(j,"")

    return "balanced"


# Call the function and print the result
op=c_s_b(s)
print(op)
     


