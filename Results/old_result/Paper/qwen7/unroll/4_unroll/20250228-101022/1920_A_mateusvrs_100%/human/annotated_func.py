#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 2 ≤ n ≤ 100. The following n lines contain pairs of integers (a, x) where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9, representing the constraints on the integer k. There is at least one constraint of type 1 and one constraint of type 2, and no two constraints are the same.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 500, and `n` is an integer such that 2 ≤ n ≤ 100; `r` is a list containing integers calculated based on the conditions inside the loop for each iteration.
    print(*r, sep='\n')
    #This is printed: each element of the list r on a new line
#Overall this is what the function does:The function processes multiple test cases, each with a specified number of constraints. For each test case, it calculates a value based on the given constraints and stores these values in a list. Specifically, it finds the maximum value `bx` for constraints of type 1 and the minimum value `ax` for constraints of type 2. If `bx` is greater than `ax`, it appends 0 to the result list. Otherwise, it counts how many values in the set `cx` fall within the range `[bx, ax]` and subtracts this count from the length of the range `[ax - bx + 1]`, then appends the result to the list. Finally, it prints each element of the result list on a new line.

