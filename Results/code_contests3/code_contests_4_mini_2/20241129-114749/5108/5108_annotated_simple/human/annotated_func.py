#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, where each character has an ASCII code between 33 and 126. The string may contain uppercase characters 'H', 'Q', '9', and '+' as valid instructions, while other characters are ignored.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, `a` is either the original input string or 'tstr123' based on the characters in `a`.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters. If `a` is not equal to 'tstr123', the output is 'NO'.
#Overall this is what the function does:The function accepts a string input `a` and checks for the presence of the characters 'H', 'Q', or '9'. If any of these characters are found, it prints 'YES' and changes `a` to 'tstr123'. If none of these characters are found, the function prints 'NO'. The function does not handle any invalid input cases or characters outside of the specified ones, and it only checks for specific characters while ignoring others.

