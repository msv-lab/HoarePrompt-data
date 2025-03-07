#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. There are n lines describing constraints, where each line contains two integers a and x such that a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. Additionally, there is at least one constraint of type 1 and at least one constraint of type 2, and no two constraints are the same.
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
        
    #State: Output State: After the loop executes all the iterations, `i` will be `min(less) + (loop * (innerLoop - 1))`, `max(big)` will remain less than `min(less)`, and `num` will be equal to `max(big) + (loop * (innerLoop - 1))`. `big` will be a list containing all integers `a` for which `x == 1` was true across all iterations, `no` will be a list containing all integers `a` for which `x == 3` was true across all iterations, and `less` will be a list containing all integers `a` for which `x == 2` was true across all iterations. The variable `iterable2` will be equal to `innerLoop` for each iteration, and `x` and `a` will hold the last input values provided by the user during the final iteration of the loop. The variable `innerLoop` will remain unchanged from its initial value.
#Overall this is what the function does:The function processes a series of constraints defined by the user. For each test case, it categorizes integers into three lists based on their type (1, 2, or 3). After processing all constraints, it finds and prints the smallest integer greater than all integers in the 'big' list and less than all integers in the 'less' list, excluding integers in the 'no' list. If no such integer exists, it prints the maximum integer in the 'big' list.

