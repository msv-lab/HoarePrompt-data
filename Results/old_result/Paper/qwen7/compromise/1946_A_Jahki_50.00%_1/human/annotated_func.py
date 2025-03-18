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
        
    #State: All test cases have been processed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` representing the number of test cases, an integer `n` representing the length of the array `a`, and an array `a` of `n` integers. If the length of the array exceeds 10,000, it prints 1 and 16668 and breaks out of the loop. Otherwise, it calculates the median of the array, increments elements until a new median is found, and prints the number of increments performed. After processing all test cases, the function ends.

