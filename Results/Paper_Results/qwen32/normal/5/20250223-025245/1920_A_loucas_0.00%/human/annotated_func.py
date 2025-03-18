#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100. Each of the following n lines contains two integers a and x where a is an integer in {1, 2, 3} and 1 <= x <= 10^9. a = 1 indicates k must be greater than or equal to x, a = 2 indicates k must be less than or equal to x, and a = 3 indicates k must not be equal to x. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: The program will have printed the value of `num` for each of the `loop` iterations, where `num` is the first integer in the range `[max(big), min(less))` that is not in `no`, or `0` if no such integer exists. The state of `iterable`, `big`, `less`, `no`, and `innerLoop` will be as defined by the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a set of constraints on an integer `k`. For each test case, it determines and prints a value of `k` that satisfies all the constraints, where constraints can specify that `k` must be greater than or equal to a value, less than or equal to a value, or not equal to a value. If no such `k` exists, it prints `0`.

