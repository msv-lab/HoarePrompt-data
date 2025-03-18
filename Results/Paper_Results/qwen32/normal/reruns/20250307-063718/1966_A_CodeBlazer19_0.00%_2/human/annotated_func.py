#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n and k are integers such that 1 <= n <= 100 and 2 <= k <= 100. c is a list of n integers such that 1 <= c_i <= 100 for each c_i in c.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: t is an integer such that 1 <= t <= 500; n and k are the integers read from the input; i is t-1; l is a list of integers read from the input.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`, and a list `c` of `n` integers. It then prints `k - 1` for each test case.

