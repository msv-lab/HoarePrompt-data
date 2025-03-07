#State of the program right berfore the function call: The function should take two parameters, n and k, where n and k are positive integers such that 1 <= n <= 26 and 1 <= k <= 26.
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
        
    #State: `n` and `k` are positive integers provided by the user such that 1 <= `n` <= 26 and 1 <= `k` <= 26, `t` is greater than or equal to the number of iterations executed, `i` is `t` - 1, `s` is a string containing the first `k` lowercase letters of the English alphabet, `j` is `k` + 96. If `k` is 1, `k` remains 1. Otherwise, `k` is greater than 1.
#Overall this is what the function does:The function reads an integer `t` from the user, indicating the number of test cases. For each test case, it reads two integers `n` and `k` from the user, where `1 <= n <= 26` and `1 <= k <= 26`. It then generates a string `s` consisting of the first `k` lowercase letters of the English alphabet. If `k` is 1, it prints the string `s` repeated `n` times. Otherwise, it prints the string `s` repeated twice unless `n` is 1, in which case it prints `s` once. After processing all test cases, the function concludes.

