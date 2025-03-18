#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 3 ≤ n ≤ 78.
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
        
    #State: After all iterations of the loop have finished, `t` is a positive integer such that 1 ≤ t ≤ 100, `n` is an integer (the last input provided by the user during the loop's execution), and `word` is determined based on the final value of `n`.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `n` (where 3 ≤ n ≤ 78). Based on the value of `n`, it constructs and prints a specific string `word`. The function does not return any value but prints the constructed string for each test case.

