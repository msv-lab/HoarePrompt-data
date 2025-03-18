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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 100, n is an integer such that 1 ≤ n ≤ 78, alphabet is a string containing all lowercase letters from 'a' to 'z'. After the loop executes all iterations, the value of `word` depends on the input values provided during each iteration.
#Overall this is what the function does:The function reads multiple integers `n` (where 1 ≤ n ≤ 78) from the user, constructs a string `word` based on the value of `n`, and prints the resulting string. The function processes up to 100 test cases. After processing all test cases, it outputs a series of strings `word` generated according to specific rules based on the input values.

