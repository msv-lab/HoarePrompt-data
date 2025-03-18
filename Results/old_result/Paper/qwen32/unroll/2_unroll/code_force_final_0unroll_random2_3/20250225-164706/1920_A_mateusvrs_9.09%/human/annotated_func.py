#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 100) representing the number of constraints, followed by n lines where each line contains two integers a and x (a ∈ {1, 2, 3}, 1 ≤ x ≤ 10^9). The integer a denotes the type of constraint: if a=1, k must be greater than or equal to x; if a=2, k must be less than or equal to x; if a=3, k must be not equal to x. There is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: [result1, result2, ..., result_t]
    print(*r, sep='\n')
    #This is printed: result1
    #result2
    #...
    #result_t (where result1, result2, ..., result_t are the elements of the list `r`)
#Overall this is what the function does:The function reads multiple test cases, each consisting of a number of constraints. For each test case, it determines the number of integers `k` that satisfy all the given constraints and prints the result for each test case. The constraints specify that `k` must be greater than or equal to some values, less than or equal to some values, and not equal to some values. If no such `k` exists, the result is 0.

