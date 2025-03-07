#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100. c is a list of n integers such that 1 ≤ c_i ≤ 100 for each i from 1 to n.
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
        
    #State: The loop has executed `t` times, where `t` is the initial input integer. For each of the `t` iterations, the program reads integers `n` and `k`, a list `l` of `n` integers, and then calculates the list `p` where each element is the count of a unique integer from `l`. The program then checks if the maximum value in `p` is greater than or equal to `k`. If true, it prints `k - 1`; otherwise, it prints `n`. The variables `n`, `k`, `l`, and `p` change with each iteration according to the input, but `t` remains unchanged.
#Overall this is what the function does:The function processes `t` test cases, each consisting of integers `n` and `k`, and a list `c` of `n` integers. For each test case, it determines if the highest frequency of any integer in `c` is at least `k`. If so, it outputs `k - 1`; otherwise, it outputs `n`.

