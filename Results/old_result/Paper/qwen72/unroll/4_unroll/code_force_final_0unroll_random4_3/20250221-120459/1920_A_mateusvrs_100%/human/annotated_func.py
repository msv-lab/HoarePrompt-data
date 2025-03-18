#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, representing the number of test cases. Each test case consists of an integer n such that 2 <= n <= 100, representing the number of constraints. Each constraint is represented by a pair of integers (a, x) where a is in {1, 2, 3} and 1 <= x <= 10^9. a=1 means k must be greater than or equal to x, a=2 means k must be less than or equal to x, and a=3 means k must not be equal to x. It is guaranteed that there is at least one constraint of type 1 and one of type 2 in each test case, and no two constraints are the same.
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
        
    #State: `r` is a list of integers, each representing the number of valid values for `k` for each test case, after processing all `t` test cases. The length of `r` is equal to `t`. Each element in `r` is calculated based on the constraints provided for each test case. If no valid `k` exists for a test case, the corresponding element in `r` is 0.
    print(*r, sep='\n')
    #This is printed: Each element of the list `r` printed on a new line, where each element represents the number of valid values for `k` for each test case, and is 0 if no valid `k` exists for that test case.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` representing the number of constraints, and then reads `n` pairs of integers `(a, x)` where `a` is in {1, 2, 3} and `1 <= x <= 10^9`. The function calculates and returns a list `r` of integers, each representing the number of valid values for `k` that satisfy all constraints for each test case. If no valid `k` exists for a test case, the corresponding element in `r` is 0. The function prints each element of `r` on a new line.

