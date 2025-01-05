#State of the program right berfore the function call: **Precondition**: p is a string containing between 1 and 100 characters, inclusive. The ASCII-code of each character in p is between 33 and 126, inclusive.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters, inclusive, the ASCII-code of each character in `p` is between 33 and 126, inclusive. `a` is either 'tstr123' if 'H', 'Q', or '9' is in the user input or remains as the user input if none of these characters are present.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters, inclusive, with each character having an ASCII code between 33 and 126. If 'H', 'Q', or '9' is in the user input, then `a` is set to 'tstr123'. If none of these characters are present, `a` retains its original value.
#Overall this is what the function does:The function `func` reads user input as a string `a` and checks if any of the characters 'H', 'Q', or '9' are present in the input. If any of these characters are found, it prints 'YES' and sets `a` to 'tstr123'. If none of the characters are present, it prints 'NO'. The function does not accept any parameters and operates solely on user input. The preconditions indicate that the input `p` should be a string containing between 1 and 100 characters with ASCII codes between 33 and 126.

