#State of the program right berfore the function call: n and k are positive integers such that 1 <= n <= 26 and 1 <= k <= 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        s = ''
        
        for j in range(97, k + 97):
            s += chr(j)
        
        if k == 1:
            print(n * s)
        else:
            print((2 - (n == 1)) * s)
        
    #State: The values of `n` and `k` are updated based on the input provided during each iteration of the loop, and `t` remains unchanged. The loop prints a string `s` for each iteration, where `s` is a sequence of characters from 'a' to the character corresponding to `k` (inclusive). If `k` is 1, it prints `n` times the string `s`. If `k` is greater than 1, it prints `s` twice unless `n` is 1, in which case it prints `s` once.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads two integers `n` and `k` (both between 1 and 26, inclusive) from the user. The function constructs a string `s` consisting of the first `k` lowercase letters of the English alphabet. If `k` is 1, it prints the string `s` repeated `n` times. If `k` is greater than 1, it prints the string `s` twice unless `n` is 1, in which case it prints `s` once. After processing all test cases, the function concludes, and the state of the program is unchanged except for the output printed to the console.

