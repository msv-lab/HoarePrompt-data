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
        
    #State: After the loop has executed all `t` iterations, the variables `n`, `k`, `l`, and `p` will hold the values from the last iteration of the loop. The variable `i` will be equal to `t`. The program will have printed the appropriate output for each of the `t` iterations based on the condition `max(p) >= k`.
#Overall this is what the function does:The function processes `t` test cases, each consisting of integers `n` and `k`, and a list `c` of `n` integers. For each test case, it determines and prints a value: `k - 1` if any integer appears at least `k` times in the list `c`, otherwise it prints `n`.

