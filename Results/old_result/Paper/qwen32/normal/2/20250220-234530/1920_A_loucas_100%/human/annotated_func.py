#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100. Each constraint is represented by a pair (a, x) where a is an integer in {1, 2, 3} and x is an integer such that 1 <= x <= 10^9. There is at least one constraint of type 1 and at least one constraint of type 2 in each test case. All pairs (a, x) are distinct within a test case.
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
        
    #State: num = min(less) - max(big) + 1 - count_in_range for the last iteration
#Overall this is what the function does:The function processes multiple test cases, each consisting of a set of constraints. For each test case, it calculates and prints the number of integers that satisfy certain conditions derived from the constraints. Specifically, it computes how many integers lie between the minimum value of type 2 constraints and the maximum value of type 1 constraints, excluding any values that are explicitly listed in type 3 constraints. If no such integers exist, it prints 0.

