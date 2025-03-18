#State of the program right berfore the function call: The function should take an integer t (1 ≤ t ≤ 100) as the number of test cases, and for each test case, an integer n (3 ≤ n ≤ 78) representing the encoded word.
def func():
    alphabet = string.ascii_lowercase
    for i in range(int(input())):
        n = int(input())
        
        word = ''
        
        if n > 52:
            word += alphabet[n - 53] + 'zz'
        elif n > 26:
            word += 'a' + alphabet[n - 28] + 'z'
        else:
            word += 'aa' + alphabet[n - 3]
        
        print(word)
        
    #State: The `alphabet` remains 'abcdefghijklmnopqrstuvwxyz', `t` is an integer between 1 and 100, `n` is an integer between 3 and 78. The loop prints a series of strings based on the value of `n` for each iteration, but the variables `alphabet`, `t`, and `n` are not modified by the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the user input, which represents the number of test cases. For each test case, it reads another integer `n` from the user input, where `3 ≤ n ≤ 78`. It then constructs and prints a string based on the value of `n`:
- If `n > 52`, the string is formed by appending the character at position `n - 53` in the alphabet followed by 'zz'.
- If `26 < n ≤ 52`, the string is formed by appending 'a', the character at position `n - 28` in the alphabet, and 'z'.
- If `3 ≤ n ≤ 26`, the string is formed by appending 'aa' and the character at position `n - 3` in the alphabet.
The function does not return any value; it only prints the constructed strings to the console. The `alphabet` string remains unchanged, and the variables `t` and `n` are not modified after their initial assignment.

