# List of strings to find the longest common prefix
li=["door","dog","done"]

# Initialize variables for tracking the longest prefix
Long_prefix=''

# Check if the list is empty
if not li:
    print("empty list") 
else:
    # Check if the list is empty
    for i in range(len(li)):

         # Start with the current string as the initial prefix
        prefix=li[i]

        # Flag to control the loop
        t=True

        # Compare the current prefix with each string in the list
        for j in li:
            if j == li[i]:
                # Skip comparison with itself
                continue
            while t:
                
                # print(prefix)
                if not j.startswith(prefix):

                    # If the current string does not start with the prefix, Reduce the prefix by one character from the end
                    prefix=prefix[:-1]
                    
                else :
                    # Exit the inner loop if prefix matches
                    t=False

            # Update the longest prefix if the current one is longer
            if len(Long_prefix)<=len(prefix):
                Long_prefix=prefix

                
    print(f"the longest prefix is: {Long_prefix}")