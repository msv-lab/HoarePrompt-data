#State of the program right berfore the function call: a and b are non-empty strings consisting only of the characters "0" and "1", with lengths between 1 and 1000 inclusive.
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` is a non-empty string, `b` is a non-empty string, `pa` is the count of '1's in the input string, and `i` is the last character of the input string processed.
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` is a non-empty string, `b` is a non-empty string, `pa` is the count of '1's in the input string, `i` is the last character of the input string processed, `pb` is the count of '1's present in the input string.
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function accepts two non-empty strings consisting of the characters "0" and "1", reads them from input, counts the number of '1's in each string, and prints 'YES' if the count of '1's in the first string is greater than or equal to that in the second string; otherwise, it prints 'NO'. Note that the function does not explicitly pass the parameters `a` and `b`, and instead reads them directly from input, which may lead to confusion regarding the expected input behavior.

