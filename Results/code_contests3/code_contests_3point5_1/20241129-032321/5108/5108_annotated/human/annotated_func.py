#State of the program right berfore the function call: **p is a string containing a program in HQ9+ with ASCII codes between 33 and 126 inclusive.**
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing a program in HQ9+ with ASCII codes between 33 and 126 inclusive, `a` is either 'tstr123' if the first character of the input was 'H', 'Q', or '9', or the original value of `a` if none of the characters matched.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing a program in HQ9+ with ASCII codes between 33 and 126 inclusive, `a` is either 'tstr123' if the first character of the input was 'H', 'Q', or '9', or the original value of `a` if none of the characters matched. Additionally, `a` is not equal to 'tstr123'. When `a` is not 'tstr123', 'NO' is printed.
#Overall this is what the function does:The function func reads user input and checks if the input contains the characters 'H', 'Q', or '9'. If any of these characters are found, it prints 'YES' and assigns 'tstr123' to the variable `a`. If none of the characters are found, it prints 'NO'. The function does not explicitly return a value.

