#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, there is an integer n such that 3 <= n <= 78.
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
        
    #State: The loop has completed all `t` iterations, and for each iteration, a `word` has been constructed and printed based on the value of `n`. The variable `i` has reached the value of `t`, and `alphabet` remains unchanged as 'abcdefghijklmnopqrstuvwxyz'.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and prints a specific string based on the value of `n`. The printed string is constructed using lowercase English letters and follows specific rules depending on whether `n` is greater than 52, between 28 and 52, equal to 27, or between 3 and 27.

