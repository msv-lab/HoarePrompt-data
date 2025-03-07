#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 10^5, representing the length of the array a. The array a consists of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 10^5.
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
        
    #State: `t` is 0, `n` is the last input integer, `a` is the last list of integers input by the user, and `max` is the maximum value among the minimum pairs of consecutive elements in the last list `a`.
#Overall this is what the function does:The function `func` reads a series of test cases from the input. Each test case consists of an integer `n` followed by an array `a` of `n` integers. For each test case, the function finds the maximum value among the minimum pairs of consecutive elements in the array `a`. The function prints this maximum value for each test case. After processing all test cases, the function terminates. The final state of the program includes the processed test cases, with the last processed values of `n`, `a`, and the maximum value found for the last test case.

