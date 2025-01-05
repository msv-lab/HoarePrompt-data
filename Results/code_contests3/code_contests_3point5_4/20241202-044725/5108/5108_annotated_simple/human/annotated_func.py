#State of the program right berfore the function call: The input program is a string containing characters from the HQ9+ programming language, where each character has an ASCII code between 33 and 126 (inclusive).
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `a` contains the character input by the user. If `a` contains 'H', 'Q', or '9', then 'YES' is printed and `a` is assigned the value 'tstr123'. If `a` does not contain 'H', 'Q', or '9', no changes are made to `a`.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`a` contains the character input by the user. If `a` contains 'H', 'Q', or '9', then 'YES' is printed and `a` is assigned the value 'tstr123'. If `a` does not contain 'H', 'Q', or '9' and `a` is not equal to 'tstr123' after the if condition, then 'YES' is printed and `a` is assigned the value 'tstr123'. Otherwise, no changes are made to `a`.
#Overall this is what the function does:The function `func` reads a string input from the user and checks if it contains any of the characters 'H', 'Q', or '9'. If it does, it prints 'YES' and assigns a specific value to the input string. If the input string does not contain any of these characters, it prints 'NO'. The function does not have any specific return value. However, there is missing functionality in the annotations as it does not cover the case where the input string does not contain any of the specified characters and is equal to 'tstr123' after processing.

