# DAY 6 : 16/10/2024

## Problem: JUMP GAME

The function `jump` is designed to determine the number of jumps needed to reach the last index of a list, where each element specifies the maximum jump length from that position. It starts from the second element (index 1) and counts the jumps taken while moving through the list. The function checks whether a jump would exceed the bounds of the list or if a zero is encountered, which would indicate that no further jumps are possible. In such cases, it returns `False`. If the function successfully reaches the last index, it returns the total number of jumps made. If reaching the end is not feasible, it outputs a message stating that the jump is not possible; otherwise, it displays the total number of jumps taken.

```python
def jump(l):
    # Start from the second element (index 1)
    i=1  
    # Initialize the count of jumps
    c=1 
    # Continue until the index exceeds the length of the list 
    while i<len(l):  
        #print(l[i])  # Uncomment to see the current jump value
        # Check if the jump exceeds the bounds of the list
        if i+l[i]>len(l): 
            # Return False if jump is not possible 
            return False  
        # If the current jump value is 0, can't proceed
        elif l[i]==0:  
            # Return False if jump is not possible
            return False  
        # Move to the next index based on the jump value
        i+=l[i]  
        # Increment the count of jumps
        c+=1  
        # Check if we have reached the last index
        if i==len(l)-1:  
             # Return the total number of jumps
            return c 
# Example list of jump values
l1=[2,0,1,0,4]  
# Call the jump function with the list
op=jump(l1)  
# Check if the jump was successful
if op==False:  
     # Output if jump isn't possible
    print(f"The jump is not possible") 
else:
     # Output the number of jumps
    print(f"The jump steps are {op}") 
```