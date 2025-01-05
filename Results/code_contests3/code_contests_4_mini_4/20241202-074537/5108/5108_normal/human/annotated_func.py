#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, where each character's ASCII code is between 33 (exclamation mark) and 126 (tilde), inclusive.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, `a` is 'tstr123', and `i` is the last character of the string 'tstr123'. If none of the characters in `a` are 'H', 'Q', or '9', then 'YES' is not printed and the loop executes until all characters in `a` have been processed.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters, `a` is 'tstr123', and `i` is the last character of 'tstr123'. If `a` is not equal to 'tstr123', 'NO' is printed. If `a` is equal to 'tstr123', no action is taken and the loop continues until all characters in `a` have been processed.
#Overall this is what the function does:The function accepts a string input and prints 'YES' if the string contains 'H', 'Q', or '9'; otherwise, it prints 'NO'. It does not return any value.

