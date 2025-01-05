#State of the program right berfore the function call: p is a string consisting of 1 to 100 characters, where each character has an ASCII code between 33 and 126, inclusive. The string may contain any characters, but only 'H', 'Q', and '9' will produce output when executed in the HQ9+ programming language.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string consisting of 1 to 100 characters, `a` is 'tstr123', and `i` is the last character of the string `a`. If any character in `a` was 'H', 'Q', or '9', 'YES' was printed; otherwise, no 'YES' was printed.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string consisting of 1 to 100 characters, `a` is 'tstr123', and `i` is the last character of the string `a`. If `a` is not equal to 'tstr123', then 'NO' is printed. Otherwise, no output is generated.
#Overall this is what the function does:The function accepts no parameters and reads a string input. It checks if the input contains any of the characters 'H', 'Q', or '9'. If any of these characters are found, it prints 'YES' and terminates the check. If none of these characters are present, it prints 'NO'. The function does not return any value but produces output based on the presence of these specific characters in the input string.

