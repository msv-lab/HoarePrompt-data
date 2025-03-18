#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 2 ≤ n ≤ 100. Each constraint is represented by a pair of integers (a, x) where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. There is at least one constraint of type 1 and one constraint of type 2, and no two constraints are the same.
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
        
    #State: Output State: `t` is an input integer such that 1 ≤ `t` ≤ 500; `r` is a list containing up to `t` integers, where each integer is calculated based on the conditions inside the loop.
    print(*r, sep='\n')
    #This is printed: the integers in the list r, each on a new line
#Overall this is what the function does:The function reads a series of test cases, each containing an integer `n` followed by `n` pairs of integers `(a, x)`. For each pair, it updates variables `ax`, `bx`, and `cx` based on the value of `a`. After processing all pairs for each test case, it calculates a result based on the values of `ax`, `bx`, and `cx` and appends this result to a list `r`. Finally, it prints the list `r` containing the calculated results for each test case.

