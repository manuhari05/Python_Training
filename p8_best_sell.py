def best_profit(l):
    # Initialize the maximum profit variable to 0
    max1 = 0
    
    # Iterate through the list using two nested loops
    for i in range(len(l)):
        # The inner loop starts from the next element after the outer loop's current element
        for j in range(i + 1, len(l)):
            # Calculate the potential profit
            if l[j] - l[i] > max1:
                # Update max1 if the current profit is greater
                max1 = l[j] - l[i]
                print(i,j)
               
    # Return the maximum profit found
    return max1  


l1 = [2, 7, 5, 1,8]
# Call the function and print the result
op = best_profit(l1)
print(f"profit {op}")  
