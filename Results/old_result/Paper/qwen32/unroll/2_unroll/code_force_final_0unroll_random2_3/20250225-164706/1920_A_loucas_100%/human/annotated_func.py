#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100. Each constraint is represented by a pair (a, x) where a is an integer in {1, 2, 3} and x is an integer such that 1 <= x <= 10^9. There is at least one constraint of type 1 and at least one constraint of type 2 in each test case. No two constraints are the same (all pairs (a, x) are distinct).
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
        
    #State: The output state consists of `loop` printed values of `num`, each representing the number of integers that satisfy the constraints for that iteration. The variables `t` and `loop` remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a set of constraints. For each test case, it calculates and prints the number of integers that satisfy all given constraints. Constraints are categorized into three types: type 1 specifies an upper bound, type 2 specifies a lower bound, and type 3 specifies an integer that cannot be included. The function ensures that the calculated number is non-negative, printing 0 if no integers satisfy the constraints.

