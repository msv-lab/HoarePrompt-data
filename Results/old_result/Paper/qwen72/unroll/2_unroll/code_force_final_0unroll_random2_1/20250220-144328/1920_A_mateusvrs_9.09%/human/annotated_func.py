#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, representing the number of test cases. Each test case consists of an integer n such that 2 <= n <= 100, representing the number of constraints. Each of the n constraints is represented by a pair of integers (a, x) where a is in {1, 2, 3} and 1 <= x <= 10^9, and all pairs (a, x) are distinct within a test case. There is at least one constraint of type 1 and at least one constraint of type 2 in each test case.
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
        
    #State: `r` is a list of integers where each integer represents the number of valid integers in the range [bx, ax] that are not in the set `cx` for each test case. The length of `r` is equal to `t`, the number of test cases.
    print(*r, sep='\n')
    #This is printed: [r[0]]
    #[r[1]]
    #...
    #[r[t-1]] (where each r[i] is the number of valid integers in the range [bx, ax] that are not in the set `cx` for the i-th test case)
#Overall this is what the function does:The function `func` reads an integer `t` from the input, where `1 <= t <= 500`, representing the number of test cases. For each test case, it reads an integer `n` (2 <= n <= 100) representing the number of constraints, and then reads `n` pairs of integers (a, x) where `a` is in {1, 2, 3} and `1 <= x <= 10^9`. The function calculates the number of valid integers in the range [bx, ax] that are not in the set `cx` for each test case, where `bx` is the maximum value of `x` for constraints of type 1, `ax` is the minimum value of `x` for constraints of type 2, and `cx` is a set of values for constraints of type 3. The function prints the results for each test case, one per line. The length of the printed results is equal to `t`.

