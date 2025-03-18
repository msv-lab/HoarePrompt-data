#State of the program right berfore the function call: Each test case consists of an integer n (2 ≤ n ≤ 100) representing the number of constraints, followed by n lines where each line contains two integers a (a ∈ {1, 2, 3}) and x (1 ≤ x ≤ 10^9). Here, a = 1 means k must be greater than or equal to x, a = 2 means k must be less than or equal to x, and a = 3 means k must not be equal to x. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same. The input starts with an integer t (1 ≤ t ≤ 500) representing the number of test cases.
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
        
    #State: less = [], big = [], no = [], num = 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a set of constraints on an integer `k`. For each test case, it determines the number of valid integers `k` that satisfy all the given constraints and prints this number. If no such integer exists, it prints `0`.

