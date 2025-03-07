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
        
    #State: After the loop executes all its iterations, `i` will be equal to the total number of iterations, which is provided as input to the loop. The value of `n` will be the last input integer provided within the loop. The variable `word` will be determined based on the value of `n` in the final iteration: if `n` is greater than 52, `word` will be 'zz'; otherwise, if `n` is greater than 26, `word` will be 'az'; otherwise, `word` will be 'aaa'.
#Overall this is what the function does:The function processes multiple test cases, each involving an integer `n` (where 3 ≤ n ≤ 78). For each `n`, it constructs a string `word` based on the value of `n`. If `n` is greater than 52, `word` is set to 'zz'; if `n` is greater than 26, `word` is set to 'az'; otherwise, `word` is set to 'aaa'. The function prints `word` for each test case. After processing all test cases, the function has no return value.

