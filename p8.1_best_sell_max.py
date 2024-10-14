def best_profit(l):
    # Initialize the maximum profit variable to 0
    max1 = 0
    
    # Iterate through the list using two nested loops
    for i in range(len(l)-1):
        
        if l[i+1]-l[i]>max1:
            print(l[i],l[i+1])
             # Add the profit to the total maximum profit
            max1 += l[i+1] - l[i]
               
    # Return the maximum profit found
    return max1  


l1 = [2, 7, 5, 1,8]
# Call the function and print the result
op = best_profit(l1)
print(f"profit {op}")  
