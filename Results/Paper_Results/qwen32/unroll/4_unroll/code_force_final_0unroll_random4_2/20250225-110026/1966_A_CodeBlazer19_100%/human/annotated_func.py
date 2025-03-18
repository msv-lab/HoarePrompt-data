#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n and k are integers such that 1 <= n <= 100 and 2 <= k <= 100. c is a list of n integers where each integer c_i satisfies 1 <= c_i <= 100.
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
        
    #State: the result of the last iteration, which is either `k - 1` or `n`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `k`, and a list `c` of `n` integers. For each test case, it determines and prints either `k - 1` or `n` based on the frequency of integers in the list `c`. Specifically, it prints `k - 1` if any integer appears at least `k` times in the list; otherwise, it prints `n`.

