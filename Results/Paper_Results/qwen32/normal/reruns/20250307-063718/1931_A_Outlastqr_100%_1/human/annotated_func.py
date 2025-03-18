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
        
    #State: `t` is an integer such that 1 <= t <= 100, `i` equals `t`, `n` is the last input integer, `alphabet` is 'abcdefghijklmnopqrstuvwxyz', and `word` is the last constructed word based on the value of `n`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and prints a specific string based on the value of `n`. The printed string is constructed using lowercase English letters and follows specific rules depending on whether `n` is less than or equal to 27, between 28 and 52, or greater than 52.

