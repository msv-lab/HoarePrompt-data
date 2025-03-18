#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n is an integer such that 3 <= n <= 78.
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
        
    #State: `t` is unchanged, `n` is the value from the last iteration, `word` is the string constructed in the last iteration based on that value of `n`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` (where 3 <= n <= 78) and prints a specific string based on the value of `n`. The string is constructed using the lowercase English alphabet and follows a particular pattern depending on whether `n` is less than or equal to 26, between 27 and 52, or greater than 52. After processing all test cases, the function concludes without modifying the input values `t` and `n` from the last test case.

