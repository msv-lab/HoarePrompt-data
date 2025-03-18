#State of the program right berfore the function call: t is an integer where 1 <= t <= 500, representing the number of test cases. Each test case contains an integer n where 2 <= n <= 100, representing the number of constraints. Each constraint is represented by a pair of integers (a, x) where a is in {1, 2, 3} and 1 <= x <= 10^9, and all pairs (a, x) within a test case are distinct.
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
        
    #State: The loop has finished executing all iterations, and the final state of the variables `less`, `big`, `no`, and `num` will be different for each test case based on the inputs provided. However, the variables `t`, `n`, and `loop` will remain unchanged. The output of the loop will be the number of valid integers that satisfy the constraints for each test case, or 0 if no such integers exist.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by an integer `n` and a set of `n` constraints. Each constraint is a pair `(a, x)` where `a` is 1, 2, or 3, and `x` is an integer. For each test case, the function calculates the number of valid integers that satisfy the constraints and prints this number. Specifically, it counts the integers that are greater than or equal to the maximum value in the `big` list, less than or equal to the minimum value in the `less` list, and not in the `no` list. If no such integers exist, it prints 0. The function does not return any values, and the state of the input variables `t` and `n` remains unchanged after the function completes.

