#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. Each constraint is described by a pair of integers (a, x) where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. There is at least one constraint of type 1 and at least one constraint of type 2 in each test case. No two constraints are the same (all pairs (a, x) are distinct).
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
        
    #State: t is 0, n is the number of constraints in the last iteration, cx is a set of unique x values from the last iteration where a == 3, ax is the minimum x from the last iteration where a == 2, bx is the maximum x from the last iteration where a == 1, and r is a list of results from each iteration.
    print(*r, sep='\n')
    #This is printed: each element of the list `r` on a new line
#Overall this is what the function does:The function processes multiple test cases, each defined by a number of constraints. For each test case, it calculates and returns a value based on the constraints of types 1, 2, and 3. Specifically, it determines the difference between the smallest value of type 2 and the largest value of type 1, adjusting for any values of type 3 that fall within this range. The results for all test cases are printed, each on a new line.

