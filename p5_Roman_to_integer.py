def roman_to_integer(s):
    # Dictionary mapping Roman numerals to their integer values
    r_i = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
     # Initialize the total integer value
    integer = 0 

    # Loop through each character in the Roman numeral string
    for i in range(len(s)):
        # Check if the current numeral is less than the next numeral
        if i < len(s) - 1 and r_i[s[i]] < r_i[s[i + 1]]:
            # Subtract value if it’s less than the next numeral
            integer -= r_i[s[i]]  
        else:
            # Otherwise, add the value
            integer += r_i[s[i]]  

    # Return the computed integer value
    return integer  


roman = "XIV"
op = roman_to_integer(roman)
print(op)  