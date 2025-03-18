#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100. Each of the following n lines contains two integers a and x, where a is an integer in {1, 2, 3} and 1 <= x <= 10^9. a denotes the type of constraint: if a=1, k must be greater than or equal to x; if a=2, k must be less than or equal to x; if a=3, k must be not equal to x. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
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
        
        for i in range(max(big), min(less)):
            if i not in no:
                num = i
                break
        
        print(num)
        
    #State: t is an integer such that 1 <= t <= 500.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a set of constraints on an integer `k`. For each test case, it determines and prints an integer `k` that satisfies all the given constraints. Specifically, it finds an integer `k` that is greater than or equal to the maximum value specified by constraints of type 1, less than or equal to the minimum value specified by constraints of type 2, and not equal to any value specified by constraints of type 3.

