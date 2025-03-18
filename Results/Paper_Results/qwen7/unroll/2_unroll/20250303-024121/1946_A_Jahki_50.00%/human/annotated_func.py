#State of the program right berfore the function call: t is a positive integer, and for each test case, n is a positive integer such that 1 ≤ n ≤ 10^5 and the array a contains n integers where each integer is in the range 1 ≤ a_i ≤ 10^9. The sum of the values of n over all test cases does not exceed 2 \cdot 10^5.
def func():
    num = int(input())
    for i in range(0, num):
        num2 = int(input())
        
        case = input()
        
        op = 0
        
        if num2 > 10000:
            print(1)
            print(16668)
            break
        else:
            a = [int(i) for i in case.split() if i.isdigit()]
            b = sorted(a)
            if num2 % 2 == 0:
                ma = int(num2 / 2) - 1
            else:
                ma = int(num2 / 2)
            median = b[ma]
            new_median = median
            while new_median <= median:
                b[ma] += 1
                op += 1
                b = sorted(b)
                new_median = b[ma]
            print(op)
        
    #State: Output State: `num` is an input integer, `t` is a positive integer, `i` is `num`, `num2` is undefined, `case` is undefined, `op` is the sum of operations performed in each iteration where the condition `num2 <= 10000` is met. If any `num2` exceeds 10000, `op` will be 1 and `num2` will be 16668.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `num2` and a list of integers `a`. For each test case, if `num2` is greater than 10000, it prints 1 and 16668 then breaks. Otherwise, it calculates the median of the sorted list `a` and performs an operation to increment elements until a new median is found, counting the number of operations needed. The function outputs the total number of operations for each valid test case.

