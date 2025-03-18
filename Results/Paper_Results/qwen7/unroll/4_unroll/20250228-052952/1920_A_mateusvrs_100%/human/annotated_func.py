#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 2 ≤ n ≤ 100. Each constraint is represented by a pair of integers (a, x) where a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9, indicating the type of constraint and the value x respectively. There is at least one constraint of type 1 and one constraint of type 2, and no two constraints are the same.
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
    #This is printed: the elements of the list r, each on a new line
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `t` and `n` integers representing constraints. For each test case, it calculates a value based on the constraints and stores these values in a list `r`. Finally, it prints the elements of `r`, each on a new line. The values in `r` are determined by comparing the maximum value of type 1 constraints (`bx`) with the minimum value of type 2 constraints (`ax`), and counting the number of type 3 constraints within this range. If `bx` is greater than `ax`, the result is 0; otherwise, it calculates the difference between `ax` and `bx` and subtracts the count of type 3 constraints within this range.

