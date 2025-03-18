#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, representing the number of test cases. Each test case contains an integer n such that 2 <= n <= 100, representing the number of constraints. Each of the n lines contains two integers a and x, where a is in {1, 2, 3} and 1 <= x <= 10^9, representing the type of constraint and the value x, respectively. It is guaranteed that there is at least one constraint of type 1 and at least one constraint of type 2 in each test case, and no two constraints are the exact same.
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
        
    #State: The loop will execute `loop` times, and for each iteration, it will read `innerLoop` lines of input, process the constraints, and print a number `num` that satisfies the constraints (if such a number exists). The variables `t`, `n`, `a`, and `x` remain unchanged as they are not directly modified within the loop.
#Overall this is what the function does:The function processes `t` test cases, where each test case contains an integer `n` and a list of `n` constraints. Each constraint is represented by two integers `a` and `x`, where `a` is in {1, 2, 3} and `1 <= x <= 10^9`. For each test case, the function reads the constraints, categorizes them into three lists (`big`, `less`, `no`), and then finds the smallest integer `num` that is greater than all values in `big`, less than all values in `less`, and not in `no`. If such an integer exists, it prints `num`; otherwise, it prints `0`. The function does not return any value, but it prints the result for each test case. The variables `t`, `n`, `a`, and `x` are not modified by the function.

