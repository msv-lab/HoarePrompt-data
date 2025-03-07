#State of the program right berfore the function call: t is an integer such that 1 <= t <= 676, and for each of the t test cases, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26.
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
        
    #State: `t` is unchanged, and `n`, `k`, and `s` do not retain any specific values after the loop as they are overwritten in each iteration.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `k`. For each test case, it constructs a string `s` of length `k` using the first `k` lowercase letters of the alphabet. If `k` is 1, it prints the string `s` repeated `n` times. Otherwise, it prints the string `s` repeated either once or twice, depending on whether `n` is 1 or greater than 1.

