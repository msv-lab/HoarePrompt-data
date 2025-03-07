#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. There are n lines describing the constraints, where each line contains two integers a and x such that a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. Additionally, there is at least one constraint of type 1, at least one constraint of type 2, and all pairs (a, x) are distinct.
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
        
    #State: Output State: All elements in the list `no` have been processed, and `num` is equal to the initial value of `num` minus the total number of elements that satisfied the condition `i <= min(less) and i >= max(big)` across all iterations of the loop. The lists `big` and `less` contain all integers `a` where `x` was 1 or 2 during the loop iterations, respectively, and the list `no` is now empty. The variable `iterable2` retains its final value from the last iteration of the loop, and `x` and `a` hold the last values read from the loop, which are not 1 or 2 and not in `less` or `big`, respectively. If `num` is less than or equal to 0 after processing all elements in `no`, it will be printed as 0.
#Overall this is what the function does:The function processes a series of constraints defined across multiple test cases. For each test case, it categorizes integers into three lists based on their type (big, less, or no) and calculates the difference between the smallest integer in the 'less' list and the largest integer in the 'big' list, adjusted for any integers in the 'no' list that fall within the range of the 'big' and 'less' lists. If the resulting count is positive, it is printed; otherwise, 0 is printed.

