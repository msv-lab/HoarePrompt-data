#State of the program right berfore the function call: n is a non-negative integer representing the number of players initially in the game, and p is a list of positive integers where each integer is unique and sorted in increasing order, representing the positions of players to be kicked out in each round.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: `n` is a non-negative integer and is less than `min(p)`, `p` remains a list of positive integers where each integer is unique and sorted in increasing order.
    return n
    #The program returns `n`, which is a non-negative integer and is less than the smallest positive integer in the list `p`.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and a list of positive integers `p` (where each integer is unique and sorted in increasing order). It decreases `n` by the number of elements in `p` that are less than or equal to `n` in each iteration until `n` is less than the smallest element in `p`. The function returns the final value of `n`, which is a non-negative integer and is guaranteed to be less than the smallest positive integer in the list `p`. The list `p` remains unchanged.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 250. k and q are positive integers such that 1 <= k, q <= 100. p is a list of k integers where 1 <= p[0] < p[1] < ... < p[k-1] <= 100. qs is a list of q integers where 1 <= qs[i] <= 100 for all 0 <= i < q.
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
        
    #State: `t` must be greater than 0, `k` and `q` are positive integers such that 1 <= k, q <= 100, `p` is a list of k integers where 1 <= p[0] < p[1] < ... < p[k-1] <= 100, `qs` is a list of q integers where 1 <= qs[i] <= 100 for all 0 <= i < q, `res` is a list containing the results of `func_1(n, p)` for each integer `n` in `qs` for all `t` iterations.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `k` and `q` from the input, followed by a list `p` of `k` integers and a list `qs` of `q` integers. It then processes each integer `n` in `qs` by calling `func_1(n, p)` and appends the result to a list `res`. After processing all integers in `qs`, it prints the contents of `res` as a space-separated string. The function does not return any value. After the function concludes, `t` is a positive integer, `k` and `q` are positive integers such that 1 <= k, q <= 100, `p` is a list of `k` integers in strictly increasing order, `qs` is a list of `q` integers, and `res` contains the results of `func_1(n, p)` for each integer `n` in `qs` for all `t` iterations.

