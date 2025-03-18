#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, representing the number of test cases. Each test case consists of an integer n such that 2 <= n <= 100, representing the number of constraints. Each constraint is represented by a pair of integers (a, x) where a is in {1, 2, 3} and 1 <= x <= 10^9, and no two constraints are the same.
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
        
    #State: The variable `num` will contain the first integer that is greater than or equal to the maximum value in `big` and less than the minimum value in `less`, and is not in `no`. If no such integer exists, `num` will be 0. The values of `t`, `n`, and `loop` remain unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads a number of constraints, categorizes them into three lists (`big`, `less`, `no`), and finds the first integer that is greater than or equal to the maximum value in `big`, less than the minimum value in `less`, and not present in `no`. If no such integer exists, it prints 0. The function does not return any value; it only prints the result for each test case. The input variables `t` and `n` are not modified by the function.

