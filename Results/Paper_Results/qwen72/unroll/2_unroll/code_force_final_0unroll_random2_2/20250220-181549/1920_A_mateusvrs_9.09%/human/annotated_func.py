#State of the program right berfore the function call: t is an integer where 1 <= t <= 500, representing the number of test cases. Each test case consists of an integer n where 2 <= n <= 100, representing the number of constraints. Each constraint is represented by a pair of integers (a, x) where a is in {1, 2, 3} and 1 <= x <= 10^9, and no two constraints are the same.
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
        
    #State: `r` is a list of integers, each representing the number of valid integers between `bx` and `ax` (inclusive) that are not in the set `cx` for each test case. The length of `r` is equal to `t`.
    print(*r, sep='\n')
    #This is printed: Each integer in the list `r` printed on a new line (where each integer represents the number of valid integers between `bx` and `ax` (inclusive) that are not in the set `cx` for each test case)
#Overall this is what the function does:The function `func` processes a series of test cases, where each test case consists of a set of unique constraints. For each test case, it determines the number of valid integers between `bx` and `ax` (inclusive) that are not in the set `cx`. The function then prints each result on a new line. The final state of the program is that `r` is a list of integers, each representing the number of valid integers for the corresponding test case, and the length of `r` is equal to the number of test cases `t`.

