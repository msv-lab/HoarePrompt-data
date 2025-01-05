#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, where each character has an ASCII code between 33 (exclamation mark) and 126 (tilde), inclusive.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, `a` is 'tstr123' if any character in `a` is 'H', 'Q', or '9'; otherwise, `a` remains unchanged.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters. If `a` is not equal to 'tstr123', then `a` remains unchanged and "NO" is printed. If `a` is equal to 'tstr123', the condition is not met, and no action is taken.
#Overall this is what the function does:The function accepts user input as a string (expected to be between 1 and 100 characters long with ASCII codes between 33 and 126). It checks if the input string contains any of the characters 'H', 'Q', or '9'. If any of these characters are found, it prints 'YES' and sets a variable `a` to 'tstr123'. If none of these characters are found, it prints 'NO'. There is no return value from the function.

