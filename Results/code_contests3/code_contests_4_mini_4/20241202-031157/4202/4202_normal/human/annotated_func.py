#State of the program right berfore the function call: a and b are strings consisting only of the characters '0' and '1', and both strings have lengths between 1 and 1000 inclusive.
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the total count of '1's in the input string; `a` is a string of '0's and '1's; `b` is a string of '0's and '1's.
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the total count of '1's in the input string, `pb` is equal to `pa`, and `a` and `b` are the original input strings.
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function accepts two binary strings `a` and `b`, each consisting of characters '0' and '1', with lengths between 1 and 1000. It counts the number of '1's in each string and prints 'YES' if the count of '1's in `a` is greater than or equal to the count in `b`, and 'NO' otherwise. The function does not explicitly accept parameters; instead, it reads input directly via `raw_input()`, which may not align with the initial description of accepting two parameters.

