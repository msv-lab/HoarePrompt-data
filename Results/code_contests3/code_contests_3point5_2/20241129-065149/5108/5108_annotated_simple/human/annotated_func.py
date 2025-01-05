#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, inclusive, where each character has an ASCII-code between 33 and 126, inclusive.**
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, inclusive, where each character has an ASCII-code between 33 and 126, inclusive; `a` is either 'tstr123' if 'H', 'Q', or '9' is found in `p`, or the input string `p` otherwise.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters, inclusive, where each character has an ASCII-code between 33 and 126, inclusive. `a` is either 'tstr123' if 'H', 'Q', or '9' is found in `p`, or the input string `p` otherwise. If `a` is not 'tstr123', then the overall state remains the same.
#Overall this is what the function does:The function `func` reads a string `p` from the user, iterates through each character in the string, and checks if any character is 'H', 'Q', or '9'. If any of these characters are found, it prints 'YES' and assigns 'tstr123' to `a`. If none of these characters are found, it prints 'NO'. The function does not explicitly return any value.

