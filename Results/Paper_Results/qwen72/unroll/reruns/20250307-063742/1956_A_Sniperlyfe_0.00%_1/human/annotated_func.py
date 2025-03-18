#State of the program right berfore the function call: n is a non-negative integer, and p is a list of integers such that 1 <= p[i] <= 100 and p is sorted in increasing order.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: n is less than the minimum value in the list p, and p remains unchanged.
    return n
    #The program returns the value of `n`, which is less than the minimum value in the list `p`.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and a sorted list of integers `p` (where each element is between 1 and 100). It repeatedly decreases `n` by the count of elements in `p` that are less than or equal to `n` until `n` is less than the minimum value in `p`. The function then returns the updated value of `n`, which is guaranteed to be less than the minimum value in the list `p`. The list `p` remains unchanged throughout the function's execution.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 250, k and q are positive integers such that 1 <= k, q <= 100, p is a list of k unique positive integers in increasing order where 1 <= p[i] <= 100, and qs is a list of q positive integers where 1 <= qs[i] <= 100.
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
        
    #State: t is an input integer such that 1 <= t <= 250, k and q are positive integers such that 1 <= k, q <= 100, p is a list of k unique positive integers in increasing order where 1 <= p[i] <= 100, and qs is a list of q positive integers where 1 <= qs[i] <= 100. The loop has printed the results of `func_1(n, p)` for each `n` in `qs` for each iteration of `t`. The variables `k`, `q`, `p`, and `qs` are redefined in each iteration of the loop, and the final values of these variables will be the ones from the last iteration.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `k` and `q` from the input, followed by a list `p` of `k` unique positive integers in increasing order, and a list `qs` of `q` positive integers. It then processes each integer `n` in `qs` by calling `func_1(n, p)` and appends the result to a list `res`. After processing all integers in `qs`, it prints the results in `res` as a space-separated string. This process is repeated for each of the `t` test cases. The function does not return any value; it only prints the results. After the function concludes, the variables `t`, `k`, `q`, `p`, and `qs` will hold the values from the last test case.

