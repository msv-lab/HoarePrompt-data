#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. There are n lines describing the constraints, where each line contains two integers a and x such that a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. Additionally, there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: All elements from `no` have been iterated over, and for each iteration, the condition `i <= min(less) and i >= max(big)` was satisfied, leading to `num` being decremented by 1 for each such element. Therefore, `num` is now equal to zero since all elements in `no` that met the condition have been processed. The variables `innerLoop` is now 0, `iterable2` is equal to `innerLoop - 1` (which is -1), `big` contains all integers `a` for which `x` was 1 during the iterations, `less` contains all integers `a` for which `x` was 2 during the iterations, and `no` is empty as all its elements have been processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t and an integer n. For each test case, it reads n lines of input, where each line contains two integers a and x. Based on the value of x, it categorizes a into three lists: `big`, `less`, and `no`. After processing all inputs, it calculates the difference between the minimum value in `less` and the maximum value in `big`, adjusting this difference by subtracting one for each element in `no` that falls within the range defined by `min(less)` and `max(big)`. If the resulting value is less than 1, it prints 0; otherwise, it prints the adjusted difference.

