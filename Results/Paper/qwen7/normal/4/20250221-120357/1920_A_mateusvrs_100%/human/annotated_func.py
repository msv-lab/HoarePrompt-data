#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, each test case contains an integer n such that 2 ≤ n ≤ 100, and for each constraint, a is an integer in {1, 2, 3} and x is an integer such that 1 ≤ x ≤ 10^9. Additionally, there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: Output State: `t` is 0, `r` is a list containing either one element which is 0 or `ax - bx + 1 - tmp`, `n` is the total number of iterations executed, `cx` is a set containing all unique `x` values where `a` was not 1, `ax` is the minimum value among all `x` where `a` was 2, `bx` is the maximum value among all `x` where `a` was 1, and `r` is calculated based on whether `bx` is greater than `ax`. If `bx` is greater than `ax`, then `r` is [0]. Otherwise, `r` is `ax - bx + 1 - tmp`, where `tmp` is the count of elements in `cx` that are within the range `[bx, ax]`.
    #
    #In simpler terms, after all iterations of the loop have finished:
    #- `t` is set to 0 since the initial value of `t` has been exhausted.
    #- `r` will contain either 0 or the calculated value `ax - bx + 1 - tmp` based on the conditions inside the loop.
    #- `n` will be the total number of iterations that were executed.
    #- `cx` will contain all unique `x` values for which `a` was not 1.
    #- `ax` will be the smallest `x` value for which `a` was 2.
    #- `bx` will be the largest `x` value for which `a` was 1.
    #- `r` will be 0 if `bx` is greater than `ax`; otherwise, it will be `ax - bx + 1 - tmp`, where `tmp` counts how many elements in `cx` fall within the range `[bx, ax]`.
    print(*r, sep='\n')
    #This is printed: 0 or ax - bx + 1 - tmp (where ax is the minimum value of x where a was 2, bx is the maximum value of x where a was 1, and tmp is the count of elements in cx that are within the range [bx, ax])
#Overall this is what the function does:The function processes multiple test cases, each containing an integer `n` and a series of constraints involving integers `a` and `x`. For each constraint, it updates variables `ax` and `bx` based on the value of `a`. After processing all constraints for each test case, it calculates a result stored in a list `r` based on the values of `ax`, `bx`, and a set `cx`. Finally, it prints the results for all test cases.

