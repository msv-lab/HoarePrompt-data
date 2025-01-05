#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, where each character has an ASCII code between 33 (exclamation mark) and 126 (tilde), inclusive.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, `a` is 'tstr123', and 'YES' is printed if at least one character in `a` was 'H', 'Q', or '9', otherwise no output is printed.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters. If `a` is not equal to 'tstr123', then 'NO' is printed. If `a` is equal to 'tstr123', no output is printed.
#Overall this is what the function does:The function accepts user input as a string. It checks if the input contains any of the characters 'H', 'Q', or '9'. If it does, it prints 'YES'; otherwise, it prints 'NO'. The variable `a` is set to 'tstr123' if a matching character is found, but this variable does not affect the output since the function only prints based on the presence of the characters in the input. The function does not return any value.

