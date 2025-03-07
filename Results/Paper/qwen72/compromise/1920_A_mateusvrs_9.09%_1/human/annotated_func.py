#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 100, representing the number of constraints. Each constraint is represented by a pair (a, x) where a is an integer in {1, 2, 3} indicating the type of constraint, and x is an integer where 1 ≤ x ≤ 10^9. There is at least one constraint of type 1 and at least one constraint of type 2 in each test case, ensuring a finite solution. No two constraints are the same within a test case.
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
        
    #State: `t` is 0, `r` is a list containing `t` elements, each element is either 0 if `bx` ≥ `ax` for the corresponding test case, or `ax - bx + 1 - tmp` if `bx` < `ax` for the corresponding test case. `n` is 0, `bx` is the maximum value encountered from the inputs with `a` being 1 for the last test case, `ax` is the minimum value encountered from the inputs with `a` being 2 for the last test case (or 1000000007 if no such input was given), `cx` is a set containing all unique values from the inputs with `a` being 3 for the last test case, and `tmp` is the number of elements in `cx` that are greater than or equal to `bx` and less than or equal to `ax` for the last test case.
    print(*r, sep='\n')
    #This is printed: (nothing is printed)
#Overall this is what the function does:The function `func` reads a series of test cases, each containing a set of constraints. It processes these constraints to determine the number of valid integers that satisfy the conditions defined by the constraints. Specifically, for each test case, it identifies the maximum lower bound (`bx`) and the minimum upper bound (`ax`) from the constraints of types 1 and 2, respectively. It then counts the number of unique integers from constraints of type 3 that fall within the range `[bx, ax]`. If `bx` is greater than or equal to `ax`, the function outputs 0 for that test case. Otherwise, it calculates the number of valid integers in the range `[bx, ax]` that are not excluded by the constraints of type 3 and outputs this count. The function prints the results for all test cases, one per line.

