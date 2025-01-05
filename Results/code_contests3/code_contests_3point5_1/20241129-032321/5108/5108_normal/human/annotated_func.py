#State of the program right berfore the function call: p is a string containing between 1 and 100 characters where each character's ASCII code is between 33 and 126 inclusive.**
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, `a` is either the original input string or 'tstr123', depending on whether 'H', 'Q', or '9' was found in the input string `a`.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters. `a` is either the original input string or 'tstr123', depending on whether 'H', 'Q', or '9' was found in the input string `a`. If `a` is not equal to 'tstr123', then the values of `p` and `a` remain unchanged.
#Overall this is what the function does:The function reads a string input `a`, iterates through each character in `a`, and checks if any character is 'H', 'Q', or '9'. If any of these characters are found, it prints 'YES' and assigns the value 'tstr123' to `a`, then breaks out of the loop. After the loop, if `a` is not equal to 'tstr123', it prints 'NO'. The function does not accept any parameters and does not return any value.

