#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. Each constraint is described by a pair of integers (a, x) where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. There is at least one constraint of type 1 and at least one constraint of type 2 in each test case. All pairs (a, x) are distinct within a test case.
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
        
    #State: `r` contains `t` integers, each derived from the constraints of one test case as described above.
    print(*r, sep='\n')
    #This is printed: Each integer in the list `r` on a new line (where `r` is a list of `t` integers)
#Overall this is what the function does:The function processes multiple test cases, each consisting of several constraints defined by pairs (a, x). It calculates and outputs an integer for each test case based on the constraints, specifically focusing on the relationship between the maximum value of type 1 constraints (`bx`) and the minimum value of type 2 constraints (`ax`). If `bx` is greater than or equal to `ax`, it outputs 0. Otherwise, it counts how many type 3 constraints fall within the range [bx, ax] and outputs the difference between the range size and this count.

