#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, inclusive, with ASCII code of each character between 33 and 126, inclusive.**
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, inclusive, with ASCII code of each character between 33 and 126, inclusive; `a` is either 'tstr123' if 'H', 'Q', or '9' is in the input string, or the original input string if none of 'H', 'Q', or '9' is in the input string.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters, inclusive, with ASCII code of each character between 33 and 126, inclusive; `a` is either 'tstr123' if 'H', 'Q', or '9' is in the input string, or the original input string if none of 'H', 'Q', or '9' is in the input string. If `a` is not equal to 'tstr123', the state of the program variables remains as described
#Overall this is what the function does:The function `func` reads a string input `p` and checks if it contains any of the characters 'H', 'Q', or '9'. If it does, it prints 'YES' and assigns 'tstr123' to the variable `a`. If none of these characters are found in the input string, it prints 'NO'. The function does not have any specific output in the constraints provided.

