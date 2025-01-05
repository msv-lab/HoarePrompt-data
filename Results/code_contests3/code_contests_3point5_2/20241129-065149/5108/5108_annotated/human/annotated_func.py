#State of the program right berfore the function call: **Precondition**: p is a string containing between 1 and 100 characters. Each character in p has an ASCII code between 33 and 126, inclusive.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, each character in `p` has an ASCII code between 33 and 126, inclusive. `a` is either 'tstr123' if 'H', 'Q', or '9' is in `a`, or it remains the same as the initial value.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters, each character in `p` has an ASCII code between 33 and 126, inclusive. `a` is either 'tstr123' if 'H', 'Q', or '9' is in `a`, or it remains the same as the initial value. Additionally, if `a` is not equal to 'tstr123', the final state of `a` remains the same as the initial value.
#Overall this is what the function does:The function `func` prompts the user for input, checks if any of the characters in the input string are 'H', 'Q', or '9'. If any of these characters are found, it prints 'YES' and updates the value of `a` to 'tstr123' then exits the loop. If none of these characters are present, it prints 'NO'. The function does not accept any parameters and the output is not specified.

