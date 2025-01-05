#State of the program right berfore the function call: p is a string consisting of 1 to 100 characters, where each character has an ASCII code between 33 (inclusive) and 126 (inclusive).
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string consisting of 1 to 100 characters with ASCII codes between 33 and 126, `a` is 'tstr123', and `i` is the last character of the input string 'a'. If any character in 'a' is one of 'H', 'Q', or '9', 'YES' is printed and the loop exits early; otherwise, the loop will have gone through all characters of 'a' without printing 'YES'.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string consisting of 1 to 100 characters with ASCII codes between 33 and 126, `a` is 'tstr123', and `i` is the last character of the input string 'a'. If `a` is not equal to 'tstr123', then 'NO' is printed. Otherwise, the program does not execute any action as there is no else part.
#Overall this is what the function does:The function accepts a string input consisting of 1 to 100 characters, where each character has an ASCII code between 33 and 126. It checks if any character in the input string is 'H', 'Q', or '9'. If any of these characters are found, it prints 'YES' and exits the loop. If none of these characters are found after checking all characters, it prints 'NO'. The function does not return any value.

