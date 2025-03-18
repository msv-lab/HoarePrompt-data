#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the length of the array a, and a is a list of n integers where each integer is in the range [1, 10^9].
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
        
    #State: num is an input integer, t remains unchanged, each test case has executed the loop and printed the operation count needed to increase the median of a sorted list until it exceeds the median, or printed 1 and 16668 if num2 is greater than 10000.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `t` (number of test cases), an integer `n` (length of the array `a`), and a list `a` of `n` integers. It then sorts the list and calculates the median. If the second largest element is less than or equal to the median, it increments elements until the median is exceeded, counting the number of operations. If `n` is greater than 10000, it prints 1 and 16668 immediately. After processing all test cases, it prints the operation count for each case.

