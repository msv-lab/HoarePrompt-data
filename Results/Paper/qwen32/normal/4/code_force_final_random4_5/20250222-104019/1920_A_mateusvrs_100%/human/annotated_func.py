#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. Each of the t test cases starts with an integer n such that 2 ≤ n ≤ 100. Following n lines describe the constraints for each test case, where each line contains two integers a and x, where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. a=1 means k must be greater than or equal to x, a=2 means k must be less than or equal to x, and a=3 means k must be not equal to x. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2 in each test case, and no two constraints are the same.
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
        
    #State: r contains the final results for all t test cases.
    print(*r, sep='\n')
    #This is printed: each element of the list `r` printed on a new line
#Overall this is what the function does:The function processes multiple test cases, each consisting of constraints on an integer `k`. For each test case, it determines the number of valid integers `k` that satisfy all given constraints and outputs the result for each test case.

