#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 100) representing the number of constraints, followed by n lines where each line contains two integers a and x (a ∈ {1, 2, 3}, 1 ≤ x ≤ 10^9). The integer a denotes the type of constraint: if a=1, k must be greater than or equal to x; if a=2, k must be less than or equal to x; if a=3, k must be not equal to x. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same. The input starts with an integer t (1 ≤ t ≤ 500) indicating the number of test cases.
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
        
    #State: `loop` is the total number of test cases, `iterable` is `loop - 1`, `less`, `big`, and `no` are lists from the last test case, `num` is the result of the last test case, and `innerLoop` is the number of constraints in the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of constraints on an integer `k`. For each test case, it determines the number of possible integer values for `k` that satisfy all the given constraints. It then prints this count for each test case. If no such integer `k` exists, it prints `0`.

