#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n and k are integers such that 1 <= n <= 100 and 2 <= k <= 100. c is a list of n integers such that 1 <= c_i <= 100 for each i in the range 1 to n.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [l.count(j) for j in set(l)]
        
        if max(p) >= k:
            print(k - 1)
        else:
            print(n)
        
    #State: The loop has executed `t` times, where `t` is the input integer such that 1 <= `t` <= 500. For each of the `t` iterations, `n` and `k` are integers read from the input, and `l` is a list of `n` integers read from the input. The list `p` is created to represent the frequency of each unique element in `l`. If the maximum value in `p` is greater than or equal to `k`, the program prints `k - 1`; otherwise, it prints `n`. The state of variables `t`, `n`, `k`, `l`, and `p` is reset for each iteration, but the value of `t` remains unchanged as it determines the total number of iterations.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n` and `k`, and a list `c` of `n` integers. For each test case, it determines if any integer appears at least `k` times in the list `c`. If such an integer exists, it outputs `k - 1`; otherwise, it outputs `n`.

