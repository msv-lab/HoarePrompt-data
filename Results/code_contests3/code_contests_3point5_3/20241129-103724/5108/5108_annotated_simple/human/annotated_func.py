#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, inclusive, with ASCII codes between 33 and 126, inclusive.**
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, inclusive, with ASCII codes between 33 and 126, inclusive. `a` is 'tstr123', `i` is not defined after the loop finishes.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters, inclusive, with ASCII codes between 33 and 126, inclusive. If `a` is not equal to 'tstr123', 'NO' is printed and `i` is not defined after the loop finishes.
#Overall this is what the function does:The function `func` reads a string `a` from user input, iterates over each character in the string, and if any character is 'H', 'Q', or '9', it prints 'YES' and assigns 'tstr123' to `a`. If none of these characters are found, it prints 'NO'. The function does not accept any parameters and does not return anything. The functionality also ensures that the string `a` must contain characters with ASCII codes between 33 and 126, inclusively.

