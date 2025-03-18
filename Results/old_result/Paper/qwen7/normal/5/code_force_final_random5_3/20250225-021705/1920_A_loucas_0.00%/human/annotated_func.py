#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. There are n lines describing the constraints, where each line contains two integers a and x such that a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. Additionally, there is at least one constraint of type 1, at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: Output State: After the loop executes all its iterations, `iterable` will be equal to `loop`, `innerLoop` will be the value received as input for the last iteration of the outer loop, `x` will be the last input integer received during any iteration of the loop, and `a` will be the last input integer received during any iteration of the loop. The list `big` will contain all integers `a` where `x` was 1 during the corresponding iteration, the list `less` will contain all integers `a` where `x` was 2 during the corresponding iteration, and the list `no` will contain all integers `a` where `x` was neither 1 nor 2 during the corresponding iteration. The variable `num` will either be the smallest integer between the maximum of `big` and the minimum of `less` that is not in `no`, or it will remain 0 if no such integer exists.
    #
    #This means that after all iterations of the loop, `num` will hold the smallest integer within the specified range (between the maximum of `big` and the minimum of `less`) that does not appear in `no`, or it will remain 0 if no such integer is found.
#Overall this is what the function does:The function processes a series of constraints defined by pairs of integers (a, x). It categorizes these integers into three lists based on the value of x: `big` for x=1, `less` for x=2, and `no` for other values. After processing all constraints, it finds the smallest integer within the range between the maximum value in `big` and the minimum value in `less` that is not present in the `no` list. If such an integer exists, it prints it; otherwise, it prints 0.

