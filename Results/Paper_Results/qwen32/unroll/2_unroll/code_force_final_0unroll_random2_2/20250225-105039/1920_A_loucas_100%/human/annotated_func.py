#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100. Each constraint is represented by a pair (a, x) where a is an integer in {1, 2, 3} and x is an integer such that 1 <= x <= 10^9. There is at least one constraint of type 1 and at least one constraint of type 2 in each test case. All pairs (a, x) are distinct.
def func():
    loop = int(input())
    for iterable in range(loop):
        less = []
        
        big = []
        
        no = []
        
        num = 0
        
        innerLoop = int(input())
        
        for iterable2 in range(innerLoop):
            x, a = map(int, input().split())
            if x == 1:
                big.append(a)
            elif x == 2:
                less.append(a)
            else:
                no.append(a)
        
        num = min(less) - max(big) + 1
        
        if num < 1:
            print(0)
            continue
        
        for i in no:
            if i <= min(less) and i >= max(big):
                num -= 1
        
        print(num)
        
    #State: The printed values of `num` for each iteration of the outer loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of constraints. For each test case, it calculates and prints the number of integers that satisfy all the given constraints. Constraints are categorized into three types: those that specify upper bounds, those that specify lower bounds, and those that specify exact values. The function ensures that the calculated number is non-negative, printing 0 if no integers satisfy the constraints.

