#State of the program right berfore the function call: t is an integer where 1 <= t <= 500, representing the number of test cases. Each test case contains an integer n where 2 <= n <= 100, representing the number of constraints. Each constraint is represented by a pair of integers (a, x) where a is in {1, 2, 3} and 1 <= x <= 10^9. a=1 indicates k must be greater than or equal to x, a=2 indicates k must be less than or equal to x, and a=3 indicates k must be not equal to x. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2 in each test case, and no two constraints are the same.
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
        
        if bx > ax:
            r.append(0)
        else:
            tmp = 0
            for i in cx:
                if i >= bx and i <= ax:
                    tmp += 1
            r.append(ax - bx + 1 - tmp)
        
    #State: `r` is a list containing `t` integers, where each integer represents the number of valid integers `k` that satisfy all the constraints for each test case.
    print(*r, sep='\n')
    #This is printed: [r[0]]
    #[r[1]]
    #...
    #[r[t-1]] (where each [r[i]] is the number of valid integers `k` that satisfy all the constraints for the i-th test case)
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads an integer `n` and then `n` pairs of integers (a, x) from the input, where `a` indicates the type of constraint (1 for k ≥ x, 2 for k ≤ x, and 3 for k ≠ x) and `x` is the value for the constraint. The function processes these constraints to determine the number of valid integers `k` that satisfy all the constraints for each test case. The function prints a list of `t` integers, where each integer represents the number of valid integers `k` that meet the constraints for the corresponding test case. If no valid `k` exists for a test case, the function prints 0 for that test case.

