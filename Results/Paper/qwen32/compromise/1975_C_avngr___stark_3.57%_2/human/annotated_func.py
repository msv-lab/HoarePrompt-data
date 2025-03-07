#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. Each test case consists of an integer n such that 2 <= n <= 10^5, followed by a list of n integers a where each a_i satisfies 1 <= a_i <= 10^9. The sum of n across all test cases does not exceed 10^5.
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
        
    #State: `t` is decremented to 0, `n` is the input integer from the last test case, `a` is the input list of integers from the last test case, and `max` is the maximum value among all the minimum pairs of consecutive elements in the list `a` from the last test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it determines the maximum value among the minimum values of all consecutive pairs in the list and prints this value.

