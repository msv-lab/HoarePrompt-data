#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100. Each constraint is described by a pair (a, x) where a is an integer in {1, 2, 3} and x is an integer such that 1 <= x <= 10^9. There is at least one constraint of type 1 and at least one constraint of type 2. No two constraints are the same (all pairs (a, x) are distinct).
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
        
    #State: r is a list of integers where each integer is determined by the constraints provided in each iteration of the outer loop.
    print(*r, sep='\n')
    #This is printed: each element of the list `r` on a new line (where `r` is a list of integers determined by the constraints provided in each iteration of the outer loop)
#Overall this is what the function does:The function processes multiple test cases, each consisting of a set of constraints. For each test case, it calculates and returns the number of integers within a specified range that are not explicitly listed as constraints of type 3. The range is determined by the maximum value of constraints of type 1 and the minimum value of constraints of type 2.

