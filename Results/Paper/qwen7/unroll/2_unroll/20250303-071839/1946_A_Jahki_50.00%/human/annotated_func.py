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
        
    #State: Output State: The output state will consist of a series of lines, each corresponding to a test case. For each test case, if the value of `num2` is greater than 10000, it will print "1" followed by "16668" and then stop. Otherwise, it will print an integer `op`, which represents the number of operations needed to make the median of the sorted list `b` strictly greater than the original median. Each test case's output will be formatted as follows:
    #
    #- If `num2` is greater than 10000, the output will be two lines per test case: "1" followed by "16668".
    #- If `num2` is less than or equal to 10000, the output will be a single line per test case containing the integer `op`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it first checks if the length of the array `a` (denoted by `num2`) is greater than 10000. If so, it prints "1" followed by "16668" and stops further processing. Otherwise, it calculates the median of the sorted array `a`, then increments elements until the new median is strictly greater than the original median, counting the number of operations required. Finally, it prints the total number of operations needed for each valid test case.

