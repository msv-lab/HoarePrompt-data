#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, inclusive, where each character has an ASCII code between 33 (exclamation mark) and 126 (tilde), and it may include the characters 'H', 'Q', '9', or '+'.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, `a` is 'tstr123' if any character in the original `a` was 'H', 'Q', or '9', otherwise `a` remains unchanged and is a non-empty string.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters and `a` is a non-empty string. If `a` does not equal 'tstr123', then 'NO' is printed. If `a` equals 'tstr123', the function simply does not print anything.
#Overall this is what the function does:The function accepts a string input `p` with a length between 1 and 100 characters, composed of ASCII characters between 33 and 126. It checks if any character in the string is either 'H', 'Q', or '9'. If one of these characters is found, it prints 'YES' and sets the variable `a` to 'tstr123'. If no such character is found, it prints 'NO'. The function does not return any value; it only produces output based on the conditions checked.

