#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. Each test case consists of two lines: the first line contains a single integer n such that 2 ≤ n ≤ 10^5, and the second line contains n integers a_1, a_2, ..., a_n such that 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        max = 0
        
        for i in range(1, n):
            if min(a[i], a[i - 1]) > max:
                max = min(a[i], a[i - 1])
        
        print(max)
        
    #State: Output State: After the loop executes all the iterations, `t` is an integer between 1 and 500, `i` is equal to `n`, `n` is the input integer for each iteration, `a` is a list of integers obtained from splitting the input string and converting each element to an integer for each iteration, and `max` is the maximum value found among the minimum values of any two consecutive elements in the list `a` across all iterations of the loop. This means `max` will hold the highest minimum value between any two consecutive elements observed in the lists `a` for all iterations of the loop.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer \( n \) and a list of \( n \) integers. It then finds the maximum value among the minimum values of any two consecutive elements in the list for each test case. Finally, it prints this maximum value for each test case.

