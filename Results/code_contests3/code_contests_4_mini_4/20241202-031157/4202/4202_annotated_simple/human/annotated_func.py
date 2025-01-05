#State of the program right berfore the function call: a and b are non-empty strings consisting only of the characters '0' and '1', with lengths between 1 and 1000.
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` is a non-empty string consisting of '0' and '1'; `b` is a non-empty string consisting of '0' and '1'; `pa` is the count of '1's in the input received during the loop execution.
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` is a non-empty string of '0' and '1', `b` is a non-empty string of '0' and '1', `pa` is the count of '1's in the input received during loop execution, `pb` is the count of '1's in the input received from raw_input().
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function accepts two non-empty strings consisting only of '0' and '1', counts the number of '1's in each string, and prints 'YES' if the count of '1's in the first string is greater than or equal to the count in the second string, otherwise it prints 'NO'. The function does not explicitly define how it receives its inputs, as it calls `raw_input()` twice to read the two strings instead of accepting them as parameters.

