#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and n is an integer such that 1 <= n <= 2 * 10^5 for each test case.
def func():
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: `pd` is a list where each element `pd[i]` for `1 <= i < N` is the sum of all previous elements in the list plus the sum of the digits of the integer `i`. The variable `t` and `n` remain unchanged.
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: The list `pd` remains unchanged, and the variable `t` and `n` remain unchanged. The loop prints the value of `pd[n]` for each iteration, where `n` is the integer input provided by the user during each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, where `1 <= t <= 10^4`, and then for each of the `t` test cases, reads an integer `n` (where `1 <= n <= 2 * 10^5`). It precomputes a list `pd` of length `200001`, where each element `pd[i]` for `1 <= i < 200001` is the sum of all previous elements in the list plus the sum of the digits of the integer `i`. For each test case, it prints the value of `pd[n]`. The function does not return any value, and the variables `t` and `n` remain unchanged after the function concludes.

