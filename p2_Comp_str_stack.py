# Define opening and closing brackets
open_br="{(["
close_br="})]"

# Function to check if the bracket sequence is balanced
def Check_balance(s):
    # stack the open brackets
    stack=[] 

     # Iterate through each character in the string  
    for i in s:

         # If the character is an opening bracket, push it onto the stack
        if i in open_br:
            stack.append(i)
        elif i in close_br:

            # Get the position of the closing bracket
            pos=close_br.index(i)

            # check for the initial stack size for incorect begining of bracket and verify the same bracket by its position
            if len(stack)>0 and (open_br[pos]==stack[len(stack)-1]):
                # Pop the matching opening bracket from the stack
                stack.pop()
            else:
                return "Unbalanced"

    
     # If the stack is empty, all brackets are balanced       
    if len(stack)==0:
        return "Balanced"
    else:
        return "Unbalanced"


# Test string containing brackets
string="{[[])]}"
op=Check_balance(string)
print(op)