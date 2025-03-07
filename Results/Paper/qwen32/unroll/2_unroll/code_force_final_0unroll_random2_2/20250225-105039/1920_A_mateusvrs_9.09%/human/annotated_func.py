#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100. Each of the following n lines contains two integers a and x, where a is an integer in {1, 2, 3} and 1 <= x <= 10^9. a denotes the type of constraint: if a=1, k must be greater than or equal to x; if a=2, k must be less than or equal to x; if a=3, k must be not equal to x. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: After processing all `t` test cases, the list `r` will contain the results for each test case. The state of all other variables will remain unchanged.
    #
    #Output State:
    print(*r, sep='\n')
    #This is printed: Each element of the list `r` printed on a new line (where `r` contains the results for each test case)
#Overall this is what the function does:The function processes multiple test cases, each consisting of a set of constraints on an integer `k`. It calculates and returns the number of valid integers `k` that satisfy all given constraints for each test case.

