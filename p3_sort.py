# Initialize a list of integers
list1=[1,4,2,3,7,5]

# Print the original list
print(f"The given list is : {list1}")

# Loop through each element in the list
for i in range(0,len(list1)):

    # Inner loop for comparing adjacent elements
    for j in range(0,len(list1)-1):
        #print(list1,j)
        if list1[j]>list1[j+1]:

            # If the current element is greater than the next element ,Swap the elements to sort in ascending order
            list1[j],list1[j+1]=list1[j+1],list1[j]
# Print the sorted list
print(f"The sorted list is : {list1}")    