#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. Each test case consists of two lines: the first line contains a single integer n such that 2 ≤ n ≤ 10^5, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        if n == 2:
            print(min(a))
            continue
        
        max = 0
        
        for i in range(n - 2):
            temp = a[i:i + 3]
            temp.sort()
            if temp[1] > max:
                max = temp[1]
        
        print(max)
        
    #State: Output State: t is an input integer, and for each iteration of the loop, given an integer n and a list of n integers, if n is 2, the minimum of the list is printed. Otherwise, a variable max is set to 0, and for each group of three consecutive numbers in the list (except the last two if n is not divisible by 3), the second smallest number is found and compared with max. The final max value is then printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer n followed by n integers. For each test case, if n is 2, it prints the minimum of the two integers. Otherwise, it finds the second smallest number among every group of three consecutive numbers (excluding the last two if n is not divisible by 3) and prints the maximum of these second smallest numbers across all groups.

