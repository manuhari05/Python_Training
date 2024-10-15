
def rotate_array(l, k):
    # Rotate the array k times
    for _ in range(k):
        # Remove the last element from the list
        last = l.pop() 
        # Insert the removed element at the beginning of the list 
        l.insert(0, last)
    # Return the modified list  
    return l  

# Input list to be rotated
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
 # Number of positions to rotate
rt = 3 
# Call the function to rotate the array
op = rotate_array(list1, rt)
# Print the rotated array
print(f"The rotated array is {op}")
