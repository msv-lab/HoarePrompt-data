#State of the program right berfore the function call: There are multiple test cases, each starting with an integer n (2 ≤ n ≤ 100) representing the number of constraints. Each constraint is described by two integers a and x, where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. If a=1, k must be greater than or equal to x. If a=2, k must be less than or equal to x. If a=3, k must be not equal to x. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: [result1, result2, ..., resultt]
    print(*r, sep='\n')
    #This is printed: result1
    #result2
    #...
    #resultt (where each resulti is an element of the list r)
#Overall this is what the function does:The function processes multiple test cases, each consisting of a set of constraints on an integer `k`. For each test case, it determines the number of possible integer values `k` can take that satisfy all given constraints and outputs this count. If no such `k` exists, it outputs 0.

