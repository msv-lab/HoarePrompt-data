#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 2 ≤ n ≤ 100. Each constraint is represented by a pair of integers (a, x) where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9, indicating the type of constraint and the value x respectively. There is at least one constraint of type 1 and one constraint of type 2, and no two constraints are the same.
def func():
    t = int(input())
    r = []
    for _ in range(t):
        n = int(input())
        
        cx = set()
        
        ax = int(1000000000.0 + 7)
        
        bx = -1
        
        for _ in range(n):
            a, x = map(int, input().split())
            if a == 1:
                bx = max(x, bx)
            elif a == 2:
                ax = min(x, ax)
            else:
                cx.add(x)
        
        if bx >= ax:
            r.append(0)
        else:
            tmp = 0
            for i in cx:
                if i >= bx and i <= ax:
                    tmp += 1
            r.append(ax - bx + 1 - tmp)
        
    #State: Output State: After all iterations, `t` will be 0, indicating that the loop has completed all its iterations. `r` will be a list containing the cumulative results from each iteration of the loop. For each iteration, if `bx` is greater than or equal to `ax`, the corresponding entry in `r` will be 0. Otherwise, it will be `ax - bx + 1 - tmp`, where `tmp` is the count of elements in `cx` that fall within the range `[bx, ax]`. The variables `n`, `cx`, `ax`, and `bx` will no longer be used and can be considered as having been processed and reset within each iteration.
    print(*r, sep='\n')
    #This is printed: 0\n[r[1]\n...\nr[n]] (where r[i] is either 0 or ax[i] - bx[i] + 1 - tmp[i] for each iteration, with tmp[i] being the count of elements in cx[i] that fall within the range [bx[i], ax[i]])
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t` representing the number of constraints, followed by `t` pairs of integers `(a, x)` representing different types of constraints. It then calculates and stores a result for each test case based on the maximum and minimum values of `x` for types 1 and 2, and the count of unique values of `x` for type 3 within a specified range. Finally, it prints a list of these results, where each result is either 0 or the difference between `ax` and `bx` adjusted by the count of values in `cx` within the range `[bx, ax]`.

