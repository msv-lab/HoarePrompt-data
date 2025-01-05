#State of the program right berfore the function call: a and b are 01-strings (strings that only contain the characters "0" and "1") with lengths between 1 and 1000.
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the count of occurrences of '1' in the input string.
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the count of occurrences of '1' in the input string, `pb` is the count of occurrences of '1' in the input string, `i` is the last character of the input string.
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function reads two binary strings (strings consisting of characters '0' and '1') from standard input, counts the number of '1's in each string, and then prints 'YES' if the count of '1's in the first string is greater than or equal to that in the second string, and 'NO' otherwise. It does not accept parameters directly but relies on user input for the two binary strings.

