#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 100, representing the number of constraints. Each constraint is represented by a pair of integers (a, x) where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. a denotes the type of constraint: a=1 means k must be greater than or equal to x, a=2 means k must be less than or equal to x, and a=3 means k must be not equal to x. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: `r` is a list containing the number of valid integers `k` for each test case, where `k` satisfies all the given constraints. Each element in `r` corresponds to a test case and represents the count of integers `k` that meet the conditions: `k` is greater than or equal to the maximum of all type 1 constraints, less than or equal to the minimum of all type 2 constraints, and not equal to any of the type 3 constraints within the range. If no valid `k` exists for a test case, the corresponding element in `r` is 0.
    print(*r, sep='\n')
    #This is printed: [r[0]]  
    #[r[1]]  
    #[r[2]]  
    #...  
    #[r[n-1]] (where each [r[i]] is the count of valid integers `k` for the corresponding test case, and n is the number of test cases)
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` representing the number of constraints. Each constraint is a pair of integers (a, x) where `a` indicates the type of constraint and `x` is the value. The function calculates the number of valid integers `k` for each test case that satisfy the following conditions: `k` must be greater than or equal to the maximum of all type 1 constraints, less than or equal to the minimum of all type 2 constraints, and not equal to any of the type 3 constraints within the range. The function returns a list `r` where each element corresponds to a test case and represents the count of valid integers `k`. If no valid `k` exists for a test case, the corresponding element in `r` is 0. The function then prints each element of `r` on a new line.

