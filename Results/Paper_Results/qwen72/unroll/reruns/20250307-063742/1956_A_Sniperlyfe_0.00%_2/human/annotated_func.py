#State of the program right berfore the function call: n is a non-negative integer, p is a list of integers where 1 <= p[i] <= 100 and p is sorted in increasing order.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: n is less than the minimum value in p, and p remains unchanged.
    return n
    #The program returns the value of `n`, which is less than the minimum value in the list `p`.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and a sorted list of integers `p` where each element is between 1 and 100. It repeatedly decreases `n` by the count of elements in `p` that are less than or equal to `n` until `n` is less than the minimum value in `p`. The function then returns the modified value of `n`, which is guaranteed to be less than the smallest element in `p`. The list `p` remains unchanged throughout the function's execution.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 250, k and q are positive integers such that 1 <= k, q <= 100, p is a list of k integers where 1 <= p[0] < p[1] < ... < p[k-1] <= 100, and qs is a list of q integers where 1 <= qs[i] <= 100 for all 0 <= i < q.
def func_2():
    t = int(input())
    for _ in range(t):
        k, q = map(int, input().split())
        
        p = list(map(int, input().split()))
        
        qs = list(map(int, input().split()))
        
        res = []
        
        for n in qs:
            res.append(func_1(n, p))
            print(' '.join(map(str, res)))
        
    #State: t is an input integer such that 1 <= t <= 250, k and q are positive integers such that 1 <= k, q <= 100, p is a list of k integers where 1 <= p[0] < p[1] < ... < p[k-1] <= 100, and qs is a list of q integers where 1 <= qs[i] <= 100 for all 0 <= i < q. The loop has printed the results of `func_1(n, p)` for each `n` in `qs` for `t` iterations.
#Overall this is what the function does:The function `func_2` reads an integer `t` (1 <= t <= 250) from user input, and for each of the `t` test cases, it reads two integers `k` and `q` (1 <= k, q <= 100) and two lists `p` and `qs` from user input. The list `p` contains `k` strictly increasing integers (1 <= p[0] < p[1] < ... < p[k-1] <= 100), and the list `qs` contains `q` integers (1 <= qs[i] <= 100 for all 0 <= i < q). For each integer `n` in `qs`, the function calls `func_1(n, p)` and appends the result to a list `res`. After processing all integers in `qs`, it prints the list `res` as a space-separated string. The function does not return any value.

