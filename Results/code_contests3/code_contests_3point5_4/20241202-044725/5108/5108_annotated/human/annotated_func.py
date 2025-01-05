#State of the program right berfore the function call: The function does not take any input parameters.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `a` is a non-empty string. If any character in `a` is 'H', 'Q', or '9', then `a` is reassigned to 'tstr123'.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`a` is a non-empty string. If any character in `a` is 'H', 'Q', or '9', then `a` is reassigned to 'tstr123'. Additionally, if `a` was not originally 'tstr123', then it remains the same after the execution of the if statement.
#Overall this is what the function does:The function `func` reads an input string `a`, iterates through each character of `a`, and if any character is 'H', 'Q', or '9', it prints 'YES', reassigns `a` to 'tstr123', and then breaks the loop. If none of the characters are 'H', 'Q', or '9', it prints 'NO'. This function does not accept any input parameters and performs the described actions based on the content of the input string `a`.

