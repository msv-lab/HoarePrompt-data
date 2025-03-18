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
        
    #State: The variable `loop` is decremented by the number of iterations executed, and the variable `num` holds the first integer that satisfies the conditions for each test case (i.e., it is greater than or equal to the maximum value in `big`, less than the minimum value in `less`, and not in `no`). The lists `big`, `less`, and `no` are reset to empty for each iteration of the outer loop. The initial state of `t`, `n`, and the constraints remain unchanged.
#Overall this is what the function does:The function `func` processes a set of test cases, each defined by a number of constraints. For each test case, it reads an integer `n` representing the number of constraints, and then reads `n` pairs of integers (a, x). It categorizes these constraints into three lists: `big` for constraints where x == 1, `less` for constraints where x == 2, and `no` for constraints where x == 3. The function then finds the first integer `num` that is greater than or equal to the maximum value in `big`, less than the minimum value in `less`, and not present in `no`. If such an integer is found, it prints `num`; otherwise, it prints 0. The function does not return any value. After processing all test cases, the lists `big`, `less`, and `no` are reset to empty for the next test case, and the variable `loop` is decremented by the number of test cases processed. The initial state of the input variables `t`, `n`, and the constraints remains unchanged.

