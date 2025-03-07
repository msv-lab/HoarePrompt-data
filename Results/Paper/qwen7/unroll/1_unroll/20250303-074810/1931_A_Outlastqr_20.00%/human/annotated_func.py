#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 100, and for each test case, n is an integer such that 3 <= n <= 78.
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
        
    #State: Output State: t is a positive integer such that 1 <= t <= 100, alphabet is a string containing all lowercase letters from 'a' to 'z', n is an integer such that 3 <= n <= 78, each iteration of the loop modifies the variable `word` based on the value of `n`, resulting in a sequence of strings printed where each string follows specific rules depending on the value of `n`.
#Overall this is what the function does:The function reads a series of integers `n` (where 3 ≤ n ≤ 78) and generates a corresponding string `word` based on the value of `n`. If `n` is greater than 52, it appends 'zz' to a character derived from the alphabet; if `n` is greater than 26, it appends 'z' to two characters derived from the alphabet; otherwise, it appends three characters derived from the alphabet. The function prints these strings for each input `n` and does not return any value.

