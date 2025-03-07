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
        
    #State: i is equal to t, n and k are the values from the last iteration, s is the string of the first k letters of the alphabet constructed in the last iteration.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of two integers `n` and `k`. It constructs a string `s` containing the first `k` letters of the alphabet and prints the string `n` times if `k` is 1, or prints the string twice if `n` is greater than 1 and once if `n` is 1.

