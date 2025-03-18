#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 100. There are n lines describing constraints, where each line contains two integers a and x such that a ∈ {1, 2, 3} and 1 ≤ x ≤ 10^9. Constraints of type 1 and type 2 always exist, and no two constraints are the same.
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
        
    #State: Output State: The output state depends on the inputs provided during the execution of the loop. The final value of `num` after all iterations is printed, which represents the count of numbers in the `no` list that fall within the range between `max(big)` and `min(less)`, adjusted for any overlaps.
#Overall this is what the function does:The function processes a series of constraints defined by the number of test cases and their respective conditions. For each test case, it categorizes integers into three lists based on their types (big, less, and no). It then calculates the count of integers in the 'no' list that fall within the range between the maximum value in the 'big' list and the minimum value in the 'less' list, adjusting for any overlaps. Finally, it prints the result for each test case.

