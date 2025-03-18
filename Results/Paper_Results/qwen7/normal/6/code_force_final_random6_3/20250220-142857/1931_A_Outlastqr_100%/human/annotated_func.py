#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, n is an integer such that 3 ≤ n ≤ 78.
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
        
    #State: After all iterations of the loop have finished, the value of `i` will be equal to the total number of iterations, `word` will be one of the following strings based on the final value of `n`: 'zz', 'az', 'aay', or 'aaa', and `n` will be the last input integer provided during the loop's execution.
#Overall this is what the function does:The function reads a series of test cases and integers `n`. For each test case, it constructs a string `word` based on the value of `n` and prints it. The possible outputs for `word` are 'zz', 'az', 'aay', or 'aaa'. The function does not return any value but prints the constructed strings.

