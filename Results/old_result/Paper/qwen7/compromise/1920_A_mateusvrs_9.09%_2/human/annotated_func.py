#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. There are n lines describing the constraints, where each line contains two integers a and x such that a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. There is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: After all iterations, `n` will be the total number of iterations performed, `a` will be the last integer input provided during the loop's final iteration, and `x` will be the last integer input provided during the loop's final iteration. `ax` will be the smallest integer input provided as `x` when `a` was 2, `bx` will be the largest integer input provided as `x` when `a` was 1, and `cx` will be a set containing all integers provided as `x` when `a` was neither 1 nor 2. If `bx` is greater than or equal to `ax`, then `r` is a list containing the value 0. Otherwise, `tmp` will be 4, `n` will be the total number of iterations performed, `a` will be the last integer input provided during the loop's final iteration, `x` will be the last integer input provided during the loop's final iteration, `ax` will be the smallest integer input provided as `x` when `a` was 2, `bx` will be the largest integer input provided as `x` when `a` was 1, `cx` will be an empty set, and `r` will be a list with one element which is `ax - bx + 1 - tmp`.
    print(*r, sep='\n')
    #This is printed: [0] if bx >= ax, otherwise [ax - bx - 3]
#Overall this is what the function does:The function processes a series of constraints defined by pairs of integers (a, x), where a can be 1, 2, or 3, and x ranges from 1 to 10^9. For each test case, it calculates a result based on the maximum and minimum values of x for types 1 and 2, respectively, and the count of x values that fall within the range [bx, ax]. If the maximum value for type 1 constraints (bx) is greater than or equal to the minimum value for type 2 constraints (ax), the result is 0. Otherwise, the result is the difference between ax and bx, adjusted by subtracting the count of x values within the range [bx, ax] from this difference. The function returns a list of results, one for each test case.

