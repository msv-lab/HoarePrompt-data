#State of the program right berfore the function call: **Precondition**: p is a string containing between 1 and 100 characters. Each character of p has an ASCII code between 33 and 126, inclusive.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, `a` is a string with the value 'tstr123'. If any character in `a` is in ['H', 'Q', '9'], 'YES' is printed and the program breaks out of the loop. Otherwise, no action is taken.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string with between 1 and 100 characters, `a` is the string 'tstr123'. If `a` is not equal to 'tstr123', 'NO' is printed. If any character in `a` is 'H', 'Q', or '9', 'YES' is printed and the program breaks out of the loop. Otherwise, no action is taken.
#Overall this is what the function does:The function `func` reads a string `a` from the user input. It then iterates over each character of `a` and if any character is 'H', 'Q', or '9', it prints 'YES', assigns 'tstr123' to `a`, and breaks out of the loop. After the loop, if `a` is not equal to 'tstr123', it prints 'NO'. The function does not accept any parameters and has no explicit return value.

