#State of the program right berfore the function call: **p is a string containing a program in HQ9+ with ASCII-code of each character between 33 and 126, inclusive.**
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing a program in HQ9+ with ASCII-code of each character between 33 and 126, inclusive, `a` is a non-empty string. If any character in `a` is 'H', 'Q', or '9', 'YES' is printed and `a` is set to 'tstr123'. Otherwise, no changes are made to the program state.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing a program in HQ9+ with ASCII-code of each character between 33 and 126, inclusive, `a` is a non-empty string. If any character in `a` is 'H', 'Q', or '9', 'YES' is printed and `a` is set to 'tstr123'. Otherwise, no changes are made to the program state. The value of `a` is 'tstr123'
#Overall this is what the function does:The function `func` does not accept any parameters. It reads a string `a` as input and iterates through each character. If any character in `a` is 'H', 'Q', or '9', it prints 'YES' and updates `a` to 'tstr123'. If none of the characters match, it prints 'NO'. The function executes an HQ9+ program represented by the input string `p`, but there is a missing return value or explicit output.

