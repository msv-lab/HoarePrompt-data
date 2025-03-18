#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 2 <= n <= 50, and p is a list of n distinct integers where each p_i is an integer such that 1 <= p_i <= n, p_i != i for all i in [1, n].
def func():
    n = int(input())
    for i in range(n):
        x = int(input())
        
        l = list(map(int, input().strip().split()))
        
        for i in range(0, x):
            if l[l[i] - 1] == l[i] - 1:
                flag = True
                print(2)
                break
        else:
            print(3)
        
    #State: The loop has completed all `n` iterations, and for each iteration, it has printed `3`. The values of `t`, `n`, `p`, and `x` remain unchanged from their initial state; `l` remains unchanged from its initial state for each iteration.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `p` of `n` distinct integers. For each test case, it prints `2` if it is possible to rearrange the list `p` such that for each index `i`, `p_i` is not equal to `i` after a certain number of operations, otherwise it prints `3`. The function does not return a value; it only outputs the results for each test case.

