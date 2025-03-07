#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. There are n lines describing constraints, where each line contains two integers a and x such that a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. Additionally, there is at least one constraint of type 1, at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: `r` is a list containing the final result after processing all inputs, `t` is 0, `_` is `n-1`, `n` is the input integer provided initially, `cx` is a set containing all the unique `x` values that were added during the loop iterations, `ax` is the minimum of all the `x` values that were processed, `bx` is the maximum of all the `x` values that were processed, and `r` contains the value `ax - bx + 1 - tmp` if `bx <= ax`, otherwise it contains 0.
    print(*r, sep='\n')
    #This is printed: [ax - bx + 1 - tmp] if bx <= ax, otherwise [0]
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a series of constraints defined by integers \(a\) and \(x\). It calculates and stores the difference between the minimum and maximum \(x\) values that meet specific conditions (type 1 and type 2 constraints), adjusting this difference based on the count of additional \(x\) values within a certain range. Finally, it prints a list of results, one for each test case, indicating the calculated differences or zero if no valid \(x\) values meet the conditions.

