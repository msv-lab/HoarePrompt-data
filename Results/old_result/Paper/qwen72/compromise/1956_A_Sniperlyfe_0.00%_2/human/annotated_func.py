#State of the program right berfore the function call: n is a non-negative integer, p is a list of integers such that 1 <= p[i] <= 100 and p is sorted in increasing order.
def func_1(n, p):
    while n >= min(p):
        n -= sum(1 for x in p if x <= n)
        
    #State: `n` is a non-negative integer that is less than `min(p)`, `p` remains a sorted list of integers such that 1 <= p[i] <= 100.
    return n
    #The program returns `n`, which is a non-negative integer that is less than the smallest integer in the sorted list `p`.
#Overall this is what the function does:The function `func_1` accepts a non-negative integer `n` and a sorted list of integers `p` (where each element is between 1 and 100). It modifies `n` by repeatedly subtracting the count of elements in `p` that are less than or equal to `n` until `n` becomes less than the smallest integer in `p`. The function returns the modified `n`, which is a non-negative integer that is less than the smallest integer in the list `p`. The list `p` remains unchanged.

#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 250, k and q are positive integers such that 1 <= k, q <= 100, p is a list of k positive integers in strictly increasing order such that 1 <= p[0] < p[1] < ... < p[k-1] <= 100, qs is a list of q positive integers such that 1 <= qs[i] <= 100 for all 0 <= i < q.
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
        
    #State: `t` is an input integer such that 1 <= t <= 250, `k` and `q` are updated to their final input values such that 1 <= k, q <= 100, `p` is a list of integers provided by the user, `qs` is a list of q positive integers such that 1 <= qs[i] <= 100 for all 0 <= i < q, `res` is a list containing the results of `func_1(n, p)` for each element `n` in `qs`, and the loop has executed `t` times, processing all `t` sets of inputs.
#Overall this is what the function does:The function `func_2` reads an integer `t` from user input, indicating the number of test cases. For each test case, it reads two integers `k` and `q` from user input, followed by a list `p` of `k` strictly increasing positive integers and a list `qs` of `q` positive integers. It then processes each element `n` in `qs` by calling `func_1(n, p)` and appends the result to a list `res`. After processing all elements in `qs`, it prints the results in `res` for that test case. This process repeats for all `t` test cases. The function does not return any value, but it prints the results of `func_1` for each element in `qs` for each test case.

