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
        
    #State: After all iterations of the loop, the list `no` will be empty, and the variable `num` will be the final value it reaches after all possible decrements based on the conditions given. The lists `less` and `big` will remain unchanged from their initial states.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a series of constraints. For each test case, it separates the constraints into three lists based on their types (big, less, no). It then calculates the difference between the minimum value in the 'less' list and the maximum value in the 'big' list, adjusting this difference by subtracting one for each value in the 'no' list that falls within the calculated range. Finally, it prints the adjusted difference for each test case.

