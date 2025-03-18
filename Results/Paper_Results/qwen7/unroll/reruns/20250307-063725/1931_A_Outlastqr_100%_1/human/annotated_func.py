#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 3 ≤ n ≤ 78.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 100, alphabet is 'abcdefghijklmnopqrstuvwxyz', n varies based on user input during each iteration of the loop, word is a string constructed according to the conditions within the loop.
#Overall this is what the function does:The function processes a series of test cases defined by an integer `t`. For each test case, it reads an integer `n` and constructs a string `word` based on the value of `n`. If `n` is greater than 52, it appends a specific character followed by 'zz'. If `n` is between 28 and 52, it appends 'a', a specific character, and 'z'. If `n` is exactly 27, it sets `word` to 'aay'. Otherwise, it appends 'aa' followed by a specific character. The function prints the constructed string `word` for each test case. After processing all test cases, it outputs a series of strings corresponding to the given conditions.

