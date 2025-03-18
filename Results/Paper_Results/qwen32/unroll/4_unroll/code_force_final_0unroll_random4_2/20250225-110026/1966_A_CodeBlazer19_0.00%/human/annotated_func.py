#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n and k are integers such that 1 <= n <= 100 and 2 <= k <= 100. The list c contains n integers where each integer c_i satisfies 1 <= c_i <= 100.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: The value of `t` remains unchanged, and for each of the `t` test cases, the output will be `k - 1`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`, and a list `c` of `n` integers. It then outputs `k - 1` for each test case.

