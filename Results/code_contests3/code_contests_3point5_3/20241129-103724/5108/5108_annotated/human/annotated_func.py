#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, inclusive, where each character has an ASCII code between 33 and 126, inclusive.**
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, inclusive, where each character has an ASCII code between 33 and 126, inclusive. `a` is 'tstr123'. If any character in `a` is in ['H', 'Q', '9'], 'YES' is printed and the program breaks out of the most internal loop or if statement.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters, inclusive, where each character has an ASCII code between 33 and 126, inclusive. `a` is 'tstr123'. If `a` is not equal to 'tstr123', 'NO' is printed. If any character in `a` is in ['H', 'Q', '9'], 'YES' is printed and the program breaks out of the most internal loop or if statement.
#Overall this is what the function does:The function `func` reads input from the user, checks if any character in the input string is 'H', 'Q', or '9'. If any of these characters are found, it prints 'YES' and sets `a` to 'tstr123'. If none of these characters are found, it prints 'NO'. The function does not accept any parameters and does not have a specific return value.

