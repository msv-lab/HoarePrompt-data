#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The sum of all n values across all test cases does not exceed 2 * 10^5.
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
        
    #State: num is unchanged; num2, case, op, a, b, median, new_median are undefined or based on the last iteration's values if the loop did not break.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list `a` of `n` integers. For each test case, it calculates and prints the number of operations required to increase the median of the list `a` such that the new median is greater than the original median. If `n` is greater than 10000, it directly prints 1 followed by 16668 and stops processing further test cases.

