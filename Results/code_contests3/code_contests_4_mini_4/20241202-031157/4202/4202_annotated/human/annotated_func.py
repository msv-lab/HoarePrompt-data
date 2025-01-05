#State of the program right berfore the function call: a and b are strings composed of the characters "0" and "1", and both strings have lengths between 1 and 1000 inclusive.
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` is a string composed of "0" and "1", `b` is a string composed of "0" and "1", `pa` is the count of '1's in the input string, and `i` is the last character of the input string.
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` is a string composed of "0" and "1", `b` is a string composed of "0" and "1", `pa` is the count of '1's in the input string, `i` is the last character of the input string, `pb` is the count of '1's in the input string from the raw input.
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function reads two strings composed of the characters "0" and "1" from user input, counts the number of '1's in each string, and then prints 'YES' if the count of '1's in the first string is greater than or equal to the count in the second string; otherwise, it prints 'NO'. It does not accept parameters, and the return value is not specified, as it prints output directly.

