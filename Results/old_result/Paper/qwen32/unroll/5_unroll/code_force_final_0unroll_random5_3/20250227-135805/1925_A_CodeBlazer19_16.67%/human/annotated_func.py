#State of the program right berfore the function call: t is an integer such that 1 <= t <= 676, and for each test case, n and k are integers such that 1 <= n <= 26 and 1 <= k <= 26.
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
        
    #State: The output consists of `t` lines, each being the string `s` repeated a certain number of times based on the values of `n` and `k` for each test case.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `k`. For each test case, it constructs a string `s` of length `k` using the first `k` lowercase letters of the alphabet. It then prints the string `s` repeated a number of times based on the values of `n` and `k`: if `k` is 1, it prints `s` repeated `n` times; otherwise, it prints `s` repeated `1` time if `n` is 1, or `2` times if `n` is greater than 1.

