#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, each test case contains an integer n such that 2 ≤ n ≤ 100, and for each constraint, a is an integer in {1, 2, 3} and x is an integer such that 1 ≤ x ≤ 10^9. Additionally, there is at least one constraint of type 1, at least one constraint of type 2, and all pairs (a, x) are distinct within each test case.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 500, `n` is an integer such that 2 ≤ n ≤ 100; `r` is a list containing integers where each integer is the result of the logic inside the loop based on the values of `ax`, `bx`, and `cx` for each iteration.
    print(*r, sep='\n')
    #This is printed: [elements of r printed on separate lines]
#Overall this is what the function does:The function processes multiple test cases, each containing an integer \( t \) and \( n \), along with constraints defined by integers \( a \) and \( x \). For each test case, it calculates a value based on the maximum and minimum values of \( x \) for types 1 and 2, and the count of \( x \) values in type 3 that fall within a specific range. If the maximum value of type 1 constraints is greater than or equal to the minimum value of type 2 constraints, it appends 0 to the result list. Otherwise, it calculates the difference between the minimum and maximum values of type 2 constraints, subtracts the count of overlapping \( x \) values in type 3, and appends this value to the result list. Finally, it prints the results for all test cases.

