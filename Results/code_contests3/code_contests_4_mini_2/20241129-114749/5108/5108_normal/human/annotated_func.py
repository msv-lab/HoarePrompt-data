#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, where each character's ASCII code is between 33 (inclusive) and 126 (inclusive). The string may contain uppercase 'H', 'Q', '9', or '+' which are the valid instructions in the HQ9+ language.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters; `a` is either the original input string or 'tstr123' if a character in `a` is 'H', 'Q', or '9' was found during the loop. If none of these characters were found, then 'YES' is not printed.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters. If `a` is the original input string, 'NO' is printed. If `a` is equal to 'tstr123', then no output is generated.
#Overall this is what the function does:The function accepts a string input containing up to 100 characters, where each character's ASCII code is between 33 and 126. It checks if the string contains any of the characters 'H', 'Q', or '9'. If any of these characters are found, it prints 'YES' and assigns the string 'tstr123' to the variable. If none of these characters are found, it prints 'NO'. The function does not return any value and does not handle cases where the input string is empty.

