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
        
    #State: After the loop executes all its iterations, the variable `i` will be equal to the total number of iterations, which is the input value provided to the loop. The variable `n` will be the last integer input provided to the loop. The variable `word` will be determined based on the value of `n` as follows: if `n` is greater than 52, `word` will be the character from the `alphabet` list at index `n - 53` followed by 'zz'. If `n` is between 27 and 52 (inclusive), `word` will be 'a' followed by the character from the `alphabet` list at index `n - 28` followed by 'z'. If `n` is less than or equal to 26, `word` will be 'aa' followed by the character from the `alphabet` list at index `n - 3`.
#Overall this is what the function does:The function reads an integer `t` and then `t` pairs of integers `n`. For each `n`, it constructs a string `word` based on the value of `n`. If `n` is greater than 52, `word` is set to the character from the alphabet at index `n - 53` followed by 'zz'. If `n` is between 27 and 52, inclusive, `word` is set to 'a' followed by the character from the alphabet at index `n - 28` followed by 'z'. If `n` is less than or equal to 26, `word` is set to 'aa' followed by the character from the alphabet at index `n - 3`. The function prints `word` for each `n`. After processing all inputs, the function has no output but modifies the printed strings.

