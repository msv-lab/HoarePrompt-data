#State of the program right berfore the function call: n is a non-negative integer, p is a list of integers such that 1 <= p[i] <= 100 and p is sorted in strictly increasing order.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: `n` is a non-negative integer less than the smallest element in `p`, `p` remains a list of integers such that 1 <= p[i] <= 100 and `p` is sorted in strictly increasing order.
    return n
    #The program returns `n`, a non-negative integer that is less than the smallest element in the list `p`.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and a sorted list of integers `p` where each element is between 1 and 100. It modifies `n` by repeatedly subtracting the count of elements in `p` that are less than or equal to `n` until `n` is less than the smallest element in `p`. The function then returns `n`, which is a non-negative integer that is less than the smallest element in `p`. The list `p` remains unchanged.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 250. k and q are positive integers such that 1 <= k, q <= 100. p is a list of k positive integers where 1 <= p[i] <= 100 and p[i] < p[i+1] for all 0 <= i < k-1. qs is a list of q positive integers where 1 <= qs[i] <= 100 for all 0 <= i < q.
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
        
    #State: `t` is 0, `_` is `t` (the total number of iterations), `k` and `q` are input integers, `p` is a list of integers provided by the user, `qs` is a list of integers provided by the user, `n` is the last element in `qs` for the last iteration, `res` is a list containing the results of `func_1(n, p)` for each element `n` in `qs` for each iteration of the loop.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the user input, which represents the number of test cases. For each test case, it reads two integers `k` and `q` from the user input, followed by a list `p` of `k` positive integers and a list `qs` of `q` positive integers. It then processes each element `n` in `qs` by calling `func_1(n, p)` and appends the result to a list `res`. After processing all elements in `qs`, it prints the results of `res` for that test case. The function does not return any value. After the function concludes, `t` is 0, and the results for each test case have been printed.

