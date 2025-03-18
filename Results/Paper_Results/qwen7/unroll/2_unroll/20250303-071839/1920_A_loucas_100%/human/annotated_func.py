#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. There are n lines describing constraints, where each line contains two integers a and x such that a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. There is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: Output State: The output state depends on the specific values of `loop` and the inputs provided within each iteration of the loop. After executing all iterations, `loop` integers will be processed, and for each integer, a value of `num` will be calculated based on the elements in `big`, `less`, and `no`. The final output will be a series of values printed for each iteration, with each value representing `num` for that particular iteration. Each `num` is calculated as the difference between the minimum of `less` and the maximum of `big`, adjusted by the number of elements in `no` that fall within the range defined by `min(less)` and `max(big)`, ensuring this difference is at least 1. If the difference is less than 1, the output is 0.
#Overall this is what the function does:The function processes a series of constraints involving integers \( t \) and \( n \). For each of the \( n \) lines, it reads two integers \( a \) and \( x \), categorizing them into three lists based on the value of \( a \): `big`, `less`, and `no`. It then calculates the difference between the minimum value in `less` and the maximum value in `big`, adjusting this difference by subtracting the count of elements in `no` that fall within the range defined by `min(less)` and `max(big)`. If this difference is less than 1, the output is 0; otherwise, the adjusted difference is printed. This process is repeated for each of the \( t \) test cases.

