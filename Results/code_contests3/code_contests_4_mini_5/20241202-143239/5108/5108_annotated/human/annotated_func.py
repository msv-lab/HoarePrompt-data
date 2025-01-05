#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, where each character's ASCII code is between 33 and 126, inclusive. The string p may include the characters 'H', 'Q', '9', and '+', which are the only valid instructions for the HQ9+ programming language.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, `a` is 'tstr123', and `i` is the last character of `a`. If any character in `a` was 'H', 'Q', or '9', 'YES' would have been printed and the loop would have exited early.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters, `a` is 'tstr123', and `i` is the last character of `a'. If `a` is not equal to 'tstr123', then 'NO' is printed.
#Overall this is what the function does:The function accepts no parameters and reads a string input from the user. It checks if the input contains any of the characters 'H', 'Q', or '9'. If any of these characters are found, it prints 'YES' and terminates the loop. If none of these characters are present, it prints 'NO' after the loop. The function essentially determines if the input string includes specific instructions from the HQ9+ programming language.

