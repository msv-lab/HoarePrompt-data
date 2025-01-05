#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, where each character has an ASCII code between 33 and 126, inclusive.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters; `a` is either 'tstr123' if any character in the original `a` was 'H', 'Q', or '9', or remains unchanged if none of those characters were found.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters. If `a` is not equal to 'tstr123', then 'NO' is printed while `a` remains unchanged. If `a` contains any character that was 'H', 'Q', or '9', then `a` will be 'tstr123'; otherwise, `a` remains unchanged.
#Overall this is what the function does:The function accepts a string input from the user, checks if it contains any of the characters 'H', 'Q', or '9'. If any of these characters are found, it prints 'YES' and sets a variable to 'tstr123'. If none of these characters are present, it prints 'NO'. The function does not actually accept an external parameter `p` as indicated in the annotations, and the string length is not validated, meaning it can also accept an empty string or a string longer than 100 characters.

