#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and a list of n integers a_1, a_2, a_3, …, a_n where 1 ≤ a_i ≤ 10^6.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: Output State: The value of `year` will be the result of iteratively applying the operation `year += year % ai or ai` for each element `ai` in the list `a` for all iterations of the loop. This means that `year` will be updated in each iteration based on the current value of `year` and the current element from the list `a`. After all iterations, `year` will be the sum of the results of the operation applied to each element in the list `a`.
    #
    #In more detail, starting from the initial value of `year` (which is 0), the loop will go through each integer in the list `a` and update `year` as follows:
    #- For the first element `a[0]`, `year` becomes `year + (year % a[0] or a[0])`.
    #- For the second element `a[1]`, `year` becomes `(year + (year % a[0] or a[0])) + ((year + (year % a[0] or a[0])) % a[1] or a[1])`.
    #- This process continues for each subsequent element in the list `a`, updating `year` according to the same rule.
    #
    #The final value of `year` will be the sum of all such updates, reflecting the cumulative effect of the operation applied to each element in the list `a` for all iterations of the loop.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads a positive integer `n` and a list of `n` integers `a_1, a_2, ..., a_n` (each between 1 and 10^6). It then iteratively updates a variable `year` starting from 0, using the formula `year += year % ai or ai` for each integer `ai` in the list. After processing all integers in the list for all test cases, it prints the final value of `year` for each test case.

