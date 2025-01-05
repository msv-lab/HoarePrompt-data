#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, where each character has an ASCII code between 33 and 126, inclusive.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, `a` is either unchanged or set to 'tstr123', and if any character in `a` was 'H', 'Q', or '9', then 'YES' is printed.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters. If `a` is not equal to 'tstr123', then 'NO' is printed. If `a` is equal to 'tstr123' and contains any character that is 'H', 'Q', or '9', then 'YES' is printed. Otherwise, `a` remains unchanged.
#Overall this is what the function does:The function accepts a string input from the user, checks if it contains any of the characters 'H', 'Q', or '9', and prints 'YES' if any of these characters are found. If none of these characters are found, it prints 'NO'. The function does not accept any parameters directly and does not return any values. The input string can be between 1 and 100 characters long.

