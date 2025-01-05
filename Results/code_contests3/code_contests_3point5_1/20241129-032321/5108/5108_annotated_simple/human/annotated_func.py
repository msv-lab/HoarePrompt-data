#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, inclusive, with ASCII codes between 33 and 126, inclusive.**
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: p remains a string containing between 1 and 100 characters with ASCII codes between 33 and 126. If any character in a is 'H', 'Q', or '9', the program outputs 'YES' and a is assigned the string 'tstr123'.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` remains a string containing between 1 and 100 characters with ASCII codes between 33 and 126. If any character in `a` is 'H', 'Q', or '9', the program outputs 'YES' and `a` is assigned the string 'tstr123'. Additionally, if `a` is not equal to 'tstr123', the function will execute.
#Overall this is what the function does:The function `func` reads a string `p` as input and iterates through each character. If any character is 'H', 'Q', or '9', it prints 'YES' and assigns the string 'tstr123' to `a`. If none of the characters match, it prints 'NO'. The function does not explicitly return any value. The input string `p` must contain between 1 and 100 characters with ASCII codes between 33 and 126, inclusive.

