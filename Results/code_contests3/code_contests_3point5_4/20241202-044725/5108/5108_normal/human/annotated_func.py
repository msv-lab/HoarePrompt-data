#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, inclusive, where each character has an ASCII code between 33 and 126, inclusive.**
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, inclusive, where each character has an ASCII code between 33 and 126, inclusive; `a` is either 'tstr123' if 'H', 'Q', or '9' is in the input provided by the user, or it remains the same as the user input if 'H', 'Q', or '9' is not present.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters, inclusive, where each character has an ASCII code between 33 and 126, inclusive; `a` is either 'tstr123' if 'H', 'Q', or '9' is in the input provided by the user, or it remains the same as the user input if 'H', 'Q', or '9' is not present. If `a` is not equal to 'tstr123', then the program executes the if part.
#Overall this is what the function does:The function reads an input string 'p' and checks if it contains the characters 'H', 'Q', or '9'. If any of these characters are present, it prints 'YES' and assigns 'tstr123' to the variable 'a'. If none of these characters are found, it prints 'NO'. The function does not accept any parameters and does not return any value.

