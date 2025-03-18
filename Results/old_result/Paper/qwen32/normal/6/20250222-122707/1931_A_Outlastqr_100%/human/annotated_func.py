#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, n is an integer such that 3 <= n <= 78.
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
        
    #State: `t` is an integer such that 1 <= t <= 100, `n` is an input integer, `alphabet` is a string containing the lowercase English letters 'abcdefghijklmnopqrstuvwxyz', `i` is `t - 1`. For each of the `t` test cases, `word` is determined based on the value of `n`. If `n` > 52, `word` is `alphabet[n - 53] + 'zz'`. If `n` is 27, `word` is `'aay'`. If 28 <= `n` <= 52, `word` is `'a' + alphabet[n - 28] + 'z'`. If `n` is less than or equal to 26, `word` is `'aa' + alphabet[n - 3]`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` where 3 <= n <= 78 and prints a specific string based on the value of `n`. The printed string is determined by specific rules: if `n` > 52, the string is `alphabet[n - 53] + 'zz'`; if `n` is 27, the string is `'aay'`; if 28 <= `n` <= 52, the string is `'a' + alphabet[n - 28] + 'z'`; if `n` is less than or equal to 26, the string is `'aa' + alphabet[n - 3]`.

