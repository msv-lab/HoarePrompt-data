#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, where each character is an ASCII character with a code between 33 (exclamation mark) and 126 (tilde), inclusive.
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
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters. If `a` is not equal to 'tstr123', then 'NO' is printed. If `a` is equal to 'tstr123', no output is generated.
#Overall this is what the function does:The function accepts a string input of 1 to 100 ASCII characters. If the string contains any of the characters 'H', 'Q', or '9', it prints 'YES' and sets a variable `a` to 'tstr123'. If none of these characters are found, it prints 'NO'. The function does not return any value.

