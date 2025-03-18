#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 100) representing the number of constraints. Following this, there are n lines, each containing two integers a (a ∈ {1, 2, 3}) and x (1 ≤ x ≤ 10^9). If a=1, k must be greater than or equal to x. If a=2, k must be less than or equal to x. If a=3, k must be not equal to x. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same. The first line of the input contains an integer t (1 ≤ t ≤ 500) representing the number of test cases.
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
        
    #State: `t` is 0, `r` is a list containing the results of all test cases.
    print(*r, sep='\n')
    #This is printed: Each element of the list `r` printed on a new line (where `r` is a list containing the results of all test cases)
#Overall this is what the function does:The function processes multiple test cases, each consisting of constraints that define valid ranges for an integer `k`. For each test case, it determines the number of integers `k` that satisfy all given constraints and outputs this count. If no such integer exists, it outputs 0.

