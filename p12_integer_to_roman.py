# def i_r(n):
#     r={"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
#     result=""
#     for k,v in r.items():
#         while n>=v:
#             result+=k
#             n-=v
#     return result

# inp1=int(input("Enter a number: "))
# print(f"The {inp1} in integer in {i_r(inp1)}")

def i_r(n):
    # Mapping of Roman numerals to their integer values
    r=[["M",1000],["CM",900],["D",500],["CD",400],["C",100],["XC",90],["L",50],["XL",40],["X",10],["IX",9],["V",5],["IV",4],["I",1]]
    
    # Initialize an empty string to build the Roman numeral
    result=""
    
    # Iterate through the list of Roman numeral mappings
    for i in r:
        # While n is greater than or equal to the current numeral's value
        while n>=i[1]:
            # Append the Roman numeral to the result
            result+=i[0]
            # Subtract the numeral's value from n
            n-=i[1]
            
     # Return the constructed Roman numeral string
    return result


inp1=int(input("Enter a number: "))

 # Print the Roman numeral representation of the input
print(f"The {inp1} in integer in {i_r(inp1)}")