#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. There are n lines describing the constraints, where each line contains two integers a and x such that a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. Additionally, there is at least one constraint of type 1, at least one constraint of type 2, and all pairs (a, x) are distinct.
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
        
    #State: Output State: `t` must be 0, `r` is a list containing 0, 0, and 0, `cx` is a set containing all unique `x` values provided as inputs across all iterations, `ax` is the minimum of all the `x` values provided, `bx` is -1, `a` and `x` are the last input integers provided before the loop terminates, `n` is 0, and `tmp` reflects the count of `x` values in `cx` that fall within the range defined by `bx` and `ax` if `bx` is greater than `ax`; otherwise, `r` is [0, 0, 0].
    #
    #This means that after all iterations of the loop have finished, if there were any valid inputs (where `t` was greater than 0), the final result will be stored in the list `r`. The loop processes each input `t` times, updating `ax`, `bx`, and `cx` based on the operations specified. If `bx` is greater than `ax` at any point, `r` appends 0. Otherwise, it calculates `ax - bx + 1 - tmp` and appends this value to `r`. Since the loop runs for all given `t` values, and assuming no further inputs change the values of `ax`, `bx`, or `cx` once the loop starts, the final state of `r` will contain the results of each iteration. Given the conditions provided, if `t` is 0 initially and remains 0 after processing, `r` will be a list of zeros.
    print(*r, sep='\n')
    #This is printed: 0
    #0
    #0
#Overall this is what the function does:The function processes multiple test cases, each with a set of constraints. For each test case, it determines the minimum (`ax`) and maximum (`bx`) values of `x` for certain types of constraints. If `bx` is greater than `ax`, it appends 0 to the result list. Otherwise, it calculates the number of `x` values in a set (`cx`) that fall within the range `[bx, ax]` and appends the difference between `ax - bx + 1` minus the count of these values to the result list. Finally, it prints the result list, which contains either 0s or calculated differences for each test case.

