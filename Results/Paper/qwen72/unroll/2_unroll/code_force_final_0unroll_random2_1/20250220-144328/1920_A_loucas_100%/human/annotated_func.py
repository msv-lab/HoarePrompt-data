#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, representing the number of test cases. For each test case, n is an integer such that 2 <= n <= 100, representing the number of constraints. Each constraint is represented by a pair (a, x) where a is an integer in {1, 2, 3} indicating the type of constraint, and x is an integer such that 1 <= x <= 10^9. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2 in each test case, and no two constraints are the same.
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
        
    #State: The values of `t`, `n`, and `loop` remain unchanged. The variables `less`, `big`, and `no` are reset to empty lists for each iteration of the outer loop. The variable `num` is calculated and printed for each iteration, but its value is reset to 0 at the beginning of each iteration.
#Overall this is what the function does:The function `func` processes a series of test cases, each containing a set of constraints represented by pairs (a, x). For each test case, it calculates the number of integers that satisfy all the constraints and prints this number. The constraints are of three types: type 1 (big) specifies a maximum value, type 2 (less) specifies a minimum value, and type 3 (no) specifies values that must be excluded. The function prints 0 if no integers satisfy the constraints. The state of the program remains unchanged except for the printed output.

