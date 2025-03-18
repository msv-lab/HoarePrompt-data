#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 100, and for each test case, n is an integer such that 3 <= n <= 78.
def func():
    alphabet = string.ascii_lowercase
    for i in range(int(input())):
        n = int(input())
        
        word = ''
        
        if n > 52:
            word += alphabet[n - 53] + 'zz'
        elif n > 27:
            word += 'a' + alphabet[n - 28] + 'z'
        elif n == 27:
            word = 'aay'
        else:
            word += 'aa' + alphabet[n - 3]
        
        print(word)
        
    #State: Output State: t is a positive integer such that 1 <= t <= 100, alphabet is 'abcdefghijklmnopqrstuvwxyz', and n is an integer such that 3 <= n <= 78 after the loop has executed all its iterations. The value of `word` is determined based on the conditions inside the loop for each iteration of `i`.
#Overall this is what the function does:The function processes a series of test cases, each defined by a positive integer `t` (1 to 100) and an integer `n` (3 to 78). For each test case, it generates a string `word` based on the value of `n` and prints it. If `n` is greater than 52, `word` consists of the character corresponding to `n - 53` followed by 'zz'. If `n` is between 28 and 52, `word` starts with 'a', followed by the character corresponding to `n - 28`, and ends with 'z'. If `n` is exactly 27, `word` is set to 'aay'. Otherwise, `word` is 'aa' followed by the character corresponding to `n - 3'. After processing all test cases, the function prints each generated `word`.

