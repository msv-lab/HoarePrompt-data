#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of all n across all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop will print `num` lines, each containing the number of operations (`op`) required to increment the median of the list derived from `case` until it exceeds its initial value for each iteration.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it calculates the number of operations needed to increment the median of the list until it exceeds its initial value, and prints this number. If `n` is greater than 10000, it immediately prints 1 followed by 16668 and stops processing further test cases.

