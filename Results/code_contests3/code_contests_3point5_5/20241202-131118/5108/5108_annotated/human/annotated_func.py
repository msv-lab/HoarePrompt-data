#State of the program right berfore the function call: **Precondition**: The input program p is a string of length between 1 and 100 characters, inclusive. Each character in p has an ASCII code between 33 and 126, inclusive.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `a` is a non-empty iterable. If any element of `a` is 'H', 'Q', or '9', then `a` is assigned the value 'tstr123' and the loop breaks out of the most internal loop or if statement. Otherwise, `a` remains unchanged.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`a` is a non-empty iterable. If any element of `a` is 'H', 'Q', or '9', then `a` is assigned the value 'tstr123' and the loop breaks out of the most internal loop or if statement. Otherwise, `a` remains unchanged. 'NO' is printed.
#Overall this is what the function does:Functionality: The function `func` reads a string input `a` and iterates over each character. If any character is 'H', 'Q', or '9', it prints 'YES', assigns 'tstr123' to `a`, and breaks out of the loop. If none of the characters match, it prints 'NO'. The function does not accept any parameters and does not return any value. However, the annotations mention that `a` is assigned 'tstr123' in a specific condition, but this assignment is missing from the actual code.

