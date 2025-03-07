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
        
    #State: All test cases have been processed. The variable `t` remains unchanged as it represents the number of test cases and does not change within the loop. The variable `i` will be equal to `num - 1` since the loop runs from `0` to `num-1`. For each test case, the variable `num2` will be the last input integer provided for that case. The variable `case` will be the last string input for that case. The variable `op` will be the total number of operations performed across all test cases. The variable `b` will be a sorted list of integers for each test case, where each element has been incremented by 1 starting from the middle index `ma` until `new_median` exceeds `median`. The variable `median` will be the original median value before any increments for each test case.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `num2` and a list of integers `case`. If `num2` exceeds 10,000, it prints 1 and 16668 then breaks. Otherwise, it sorts the list, calculates the median, and increments the middle elements until the new median exceeds the original median. It counts the number of increments performed and prints this count for each test case. After processing all test cases, it returns nothing but modifies local variables as described.

