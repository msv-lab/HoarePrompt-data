#State of the program right berfore the function call: a and b are strings containing only the characters "0" and "1", with lengths between 1 and 1000 inclusive.
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` is a string containing "0" and "1", `b` is a string containing "0" and "1", `pa` is the count of '1's in the input string.
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` is a string containing "0" and "1", `b` is a string containing "0" and "1", `pa` is the count of '1's in the input string, `pb` is the count of '1's in the non-empty input string.
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function reads two binary strings from the input, counts the number of '1's in each string, and compares these counts. It prints 'YES' if the count of '1's in the first string is greater than or equal to the count in the second string, otherwise it prints 'NO'. The function does not take any parameters but expects input from the user directly.

