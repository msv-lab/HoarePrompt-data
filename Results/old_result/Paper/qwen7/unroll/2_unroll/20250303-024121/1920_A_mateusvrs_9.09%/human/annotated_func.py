#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. There are n lines describing the constraints, where each line contains two integers a and x such that a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. The constraints guarantee that there is a finite number of integers satisfying all constraints, and no two constraints are the same.
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
        
    #State: Output State: `t` is an integer between 1 and 500 (inclusive); `r` is a list containing integers where each integer is either 0 or a positive value representing the count of elements in `cx` that fall within the range `[bx, ax]` adjusted by subtracting the count of such elements from `(ax - bx + 1)`.
    print(*r, sep='\n')
    #This is printed: 0 or a positive value (each on a new line, where each value is derived from the count of elements in `cx` that fall within the range `[bx, ax]` adjusted by subtracting the count of such elements from `(ax - bx + 1)`)
#Overall this is what the function does:The function processes multiple test cases, each involving a set of constraints defined by pairs of integers (a, x). It calculates and returns a list of integers. For each test case, it determines the count of integers in a set that fall within a specified range [bx, ax], adjusted by subtracting the count of such integers from (ax - bx + 1). If no integers fall within the range [bx, ax], it returns 0.

