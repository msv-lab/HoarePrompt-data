#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains an integer n (2 ≤ n ≤ 100) representing the number of constraints. The following n lines each contain two integers a and x (a ∈ {1, 2, 3}, 1 ≤ x ≤ 10^9) representing the type and value of the constraint. There is at least one constraint of type 1 (k must be greater than or equal to x) and at least one constraint of type 2 (k must be less than or equal to x). No two constraints are the same (all pairs (a, x) are distinct).
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
        
    #State: `r` is a list containing the results for each test case.
    print(*r, sep='\n')
    #This is printed: Each element of the list `r` will be printed on a new line.
#Overall this is what the function does:The function processes multiple test cases, each consisting of constraints on a value `k`. For each test case, it calculates and returns the number of integers `k` that satisfy all the given constraints. If no such integers exist, it returns 0.

