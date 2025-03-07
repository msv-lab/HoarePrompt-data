#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100. Each constraint is described by a pair of integers (a, x) where a is an integer in {1, 2, 3} and x is an integer such that 1 <= x <= 10^9. There is at least one constraint of type 1 and at least one constraint of type 2. No two constraints are the same (all pairs (a, x) are distinct).
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
        
    #State: r is a list of t integers, where each integer is determined by the constraints processed in each iteration of the loop. Specifically, each element is 0 if the maximum value from type 1 constraints (bx) is greater than the minimum value from type 2 constraints (ax); otherwise, it is ax - bx + 1 minus the count of values in the set cx that are within the range [bx, ax].
    print(*r, sep='\n')
    #This is printed: Each element of the list `r` is printed on a new line, where each element is either 0 (if `bx > ax`) or `ax - bx + 1` minus the count of values in the set `cx` within the range `[bx, ax]` (otherwise)
#Overall this is what the function does:The function processes multiple test cases, each consisting of a set of constraints. For each test case, it calculates and returns an integer based on the constraints: if the maximum value from type 1 constraints is greater than the minimum value from type 2 constraints, it returns 0; otherwise, it returns the count of integers within the range defined by these constraints, excluding those specified in type 3 constraints.

