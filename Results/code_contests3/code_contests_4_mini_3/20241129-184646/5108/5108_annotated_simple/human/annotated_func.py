#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, where each character has an ASCII code between 33 and 126, inclusive. The string may include the characters 'H', 'Q', '9', and '+', which are the only instructions that produce output in the HQ9+ programming language.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, `a` is either 'tstr123' if any character in `a` was 'H', 'Q', or '9', or remains as the original non-empty string.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters. If `a` is a non-empty string that is not equal to 'tstr123', 'NO' is printed. If `a` is equal to 'tstr123', nothing is printed.
#Overall this is what the function does:The function accepts a string input and checks if it contains any of the characters 'H', 'Q', or '9'. If it finds any of these characters, it prints 'YES'. If none of these characters are present in the input string, it prints 'NO'. The function does not return any value.

