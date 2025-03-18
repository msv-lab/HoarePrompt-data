#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100. Each constraint is represented by a pair (a, x) where a is an integer in {1, 2, 3} and x is an integer such that 1 <= x <= 10^9. There is at least one constraint of type 1 and at least one constraint of type 2 in each test case. No two constraints are the same (all pairs (a, x) are distinct).
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
        
    #State: `r` is a list containing the results of processing each test case as described, with each test case contributing either a 0 (if `bx > ax`) or the count of integers in the range `[bx, ax]` excluding those in `cx` (if `bx <= ax`).
    print(*r, sep='\n')
    #This is printed: Each element of the list `r` on a new line, where each element is either 0 or the count of integers in the range `[bx, ax]` excluding those in `cx` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of constraints of three types. For each test case, it calculates the count of integers within a specific range that are not listed in a set of excluded integers. The result for each test case is either 0 if the range is invalid, or the count of integers within the range that are not excluded.

