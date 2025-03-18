#State of the program right berfore the function call: n is a non-negative integer, p is a list of integers such that 1 <= p[i] <= 100 and p is sorted in increasing order.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: n is less than the minimum value in the list p.
    return n
    #The program returns the value of `n`, which is less than the minimum value in the list `p`.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and a sorted list of integers `p` (where each element is between 1 and 100). It repeatedly subtracts the count of elements in `p` that are less than or equal to `n` from `n` until `n` is less than the minimum value in `p`. The function then returns the modified value of `n`, which is guaranteed to be less than the smallest element in the list `p`.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 250. k and q are positive integers such that 1 <= k, q <= 100. p is a list of k positive integers where 1 <= p[0] < p[1] < ... < p[k-1] <= 100. qs is a list of q positive integers where 1 <= qs[i] <= 100 for all 0 <= i < q.
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
        
    #State: The loop has completed all iterations. `t` is an input integer such that 1 <= t <= 250, `k` and `q` are positive integers such that 1 <= k, q <= 100, `p` is a list of `k` positive integers where 1 <= p[0] < p[1] < ... < p[k-1] <= 100, `qs` is a list of `q` positive integers where 1 <= qs[i] <= 100 for all 0 <= i < q. The variable `res` is a list of results from the function `func_1` applied to each element in `qs` with the list `p` as the second argument, and this list is printed for each iteration of the loop.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, where `1 <= t <= 250`. For each of the `t` test cases, it reads two integers `k` and `q` (both between 1 and 100), followed by a list `p` of `k` strictly increasing positive integers (each between 1 and 100), and a list `qs` of `q` positive integers (each between 1 and 100). For each integer `n` in `qs`, it calls `func_1(n, p)` and appends the result to a list `res`. After processing all integers in `qs`, it prints the list `res` as a space-separated string. The function does not return any value.

