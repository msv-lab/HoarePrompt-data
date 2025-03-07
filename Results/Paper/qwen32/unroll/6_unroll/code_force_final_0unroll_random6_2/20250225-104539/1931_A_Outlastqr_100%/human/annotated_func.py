#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n is an integer such that 3 <= n <= 78.
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
        
    #State: `word` is the final constructed word based on the value of `n` in the last iteration, `t` is the same as the initial value, `n` is the value of `n` in the last iteration, and `alphabet` is `'abcdefghijklmnopqrstuvwxyz'`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and prints a constructed word based on the value of `n`. The constructed word is determined by specific rules that depend on whether `n` is less than or equal to 27, between 28 and 52, or greater than 52.

