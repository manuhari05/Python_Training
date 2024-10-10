# List of strings to find the longest common prefix
li = ["door", "dog", "done"]

# Check if the list is empty
if not li:
    print("empty list")
else:
    # Sort the list of strings
    li.sort()
    
    # Take the first and last string in the sorted list
    first = li[0]
    last = li[-1]
    Long_prefix = ''

    # Compare characters of the first and last string
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            # Add the matching character to the prefix
            Long_prefix += first[i]  
        else:
            # Stop when characters differ
            break  

        
    # Print the longest common prefix found
    print(f"The longest prefix is: {Long_prefix}")
