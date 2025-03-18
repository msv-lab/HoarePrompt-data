#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, each test case contains n constraints where 2 ≤ n ≤ 100, and each constraint is represented by a pair (a, x) where a is an integer in {1, 2, 3} and 1 ≤ x ≤ 10^9. There is at least one constraint of type 1 and one constraint of type 2, and no two constraints are the same.
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
        
    #State: Output State: The value of `num` after all iterations of the loop have been executed, which is calculated based on the logic inside the loop. This value represents the count of elements in `no` that fall within the range between `min(less)` and `max(big)`, adjusted by subtracting 1 for each such element. If `num` is less than 1 after adjustments, it will be printed as 0.
#Overall this is what the function does:The function processes multiple test cases, each containing a set of constraints. For each test case, it categorizes integers into three lists based on their types (big, less, no). It then calculates the number of integers in the 'no' list that fall within the range defined by the minimum of the 'less' list and the maximum of the 'big' list, adjusting this count by subtracting one for each such integer. If the resulting count is less than 1, it prints 0; otherwise, it prints the count. The function does not accept any parameters and returns nothing explicitly, but its output is printed during execution.

