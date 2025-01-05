#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, where each character has an ASCII code between 33 and 126, inclusive. The string may contain any characters, but only 'H', 'Q', and '9' (case-sensitive) are considered instructions that produce output.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters; if any character in `a` is 'H', 'Q', or '9', then 'YES' has been printed, `a` is 'tstr123' and the loop has terminated early; if none of the characters in `a` are 'H', 'Q', or '9', then 'YES' has not been printed, and `a` remains unchanged.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters. If `a` is not equal to 'tstr123', then 'NO' is printed and `a` remains unchanged. If `a` is 'tstr123', then there is no action taken in this block.
#Overall this is what the function does:The function accepts a string input, checks for the presence of the characters 'H', 'Q', or '9'. If any of these characters are found, it prints 'YES' and alters the variable `a` to 'tstr123'. If none of these characters are found, it prints 'NO'. The function does not return any value, and it only prints output based on the conditions evaluated.

