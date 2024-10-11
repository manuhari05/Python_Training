def majority_element(l):
    # Initialize an empty dictionary to count occurrences of each element
    c_dict = {}
    
    # Iterate through each element in the list
    for i in l:
        # If the element is not already a key in the dictionary
        if i not in c_dict.keys():
            # Count the occurrences of the element in the list and store in the dictionary
            c_dict[i] = l.count(i)
    
    # Create a list of counts from the dictionary values
    l1 = list(c_dict.values())
    
    # List to store the elements that have the maximum count
    l2 = []
    
    # Iterate through the dictionary items to find the elements with the maximum count
    for k, v in c_dict.items():
        # Check if the current count is equal to the maximum count found
        if max(l1) == v:
            # If yes, append the corresponding key (element) to the result list
            l2.append(k)
    # Return the list of majority elements
    return l2  


main_l = [2, 1, 2, 3, 2, 1, 1]
# Call the function and print the result
op = majority_element(main_l)
print(op)
