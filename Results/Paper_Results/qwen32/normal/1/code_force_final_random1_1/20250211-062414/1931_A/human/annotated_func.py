#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 3 ≤ n ≤ 78.
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
        
    #State: The loop has executed `t` times, printing a `word` for each input `n` according to the specified conditions. The variable `t` is now 0, and `i` is equal to the initial value of `t`. The `alphabet` string remains unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads another integer `n` and prints a specific string based on the value of `n`. The printed string is determined by whether `n` is greater than 52, between 27 and 52, or between 3 and 26. After processing all test cases, the function completes its execution.

