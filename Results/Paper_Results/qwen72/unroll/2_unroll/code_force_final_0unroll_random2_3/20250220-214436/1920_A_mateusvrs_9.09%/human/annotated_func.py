#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, representing the number of test cases. For each test case, n is an integer such that 2 <= n <= 100, representing the number of constraints. Each constraint is represented by a pair (a, x) where a is an integer in {1, 2, 3} indicating the type of constraint, and x is an integer such that 1 <= x <= 10^9. There is at least one constraint of type 1 and at least one constraint of type 2 in each test case, and no two constraints are the same.
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
        
    #State: `r` is a list of integers, each representing the number of valid integers between the maximum of type 1 constraints and the minimum of type 2 constraints, excluding any type 3 constraints, for each test case. The length of `r` is equal to `t`.
    print(*r, sep='\n')
    #This is printed: [r[0]]
    #[r[1]]
    #...
    #[r[t-1]] (where each r[i] is the number of valid integers for the i-th test case)
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` representing the number of constraints. Each constraint is a pair (a, x) where `a` is an integer in {1, 2, 3} and `x` is an integer. The function processes these constraints to determine the number of valid integers for each test case. A valid integer is one that lies between the maximum of type 1 constraints (`bx`) and the minimum of type 2 constraints (`ax`), excluding any type 3 constraints (`cx`). The function then prints these results, one per test case, each on a new line. The final state of the program is that `r` is a list of integers, each representing the number of valid integers for the corresponding test case, and `r` has a length equal to `t`.

