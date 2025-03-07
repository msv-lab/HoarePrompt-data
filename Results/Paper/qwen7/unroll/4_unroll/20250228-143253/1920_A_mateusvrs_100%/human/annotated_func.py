#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, each test case contains n constraints where 2 ≤ n ≤ 100, and each constraint is represented by a pair (a, x) where a is an integer in {1, 2, 3} and x is an integer such that 1 ≤ x ≤ 10^9. Additionally, there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: Output State: `t` is the integer input value, `r` is a list containing integers calculated based on the conditions inside the loop for each input value of `t`.
    print(*r, sep='\n')
    #This is printed: the elements of the list r, each on a new line
#Overall this is what the function does:The function processes multiple test cases, each containing a number of constraints. For each test case, it calculates a value based on the constraints and stores these values in a list. Specifically, it finds the maximum value of type 1 constraints and the minimum value of type 2 constraints. If the maximum value of type 1 constraints is greater than the minimum value of type 2 constraints, it appends 0 to the list. Otherwise, it counts how many values in the third type of constraints fall within the range defined by the other two types and subtracts this count from the length of the range, then appends the result to the list. Finally, it prints the list of results, each element on a new line.

