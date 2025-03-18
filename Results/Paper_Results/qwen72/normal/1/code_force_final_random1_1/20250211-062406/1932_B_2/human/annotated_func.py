#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 100, representing the number of signs. a is a list of n integers where 1 ≤ a_i ≤ 10^6, representing the periodicities of the signs.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: After all iterations of the loop, `t` is 0, `n` has been an input integer for each test case, `a` has been a list of integers from user input with `n` elements for each test case, and `year` is the sum of `(year % ai or ai)` for each `ai` in `a` for each test case.
#Overall this is what the function does:The function reads multiple test cases from the input. For each test case, it reads an integer `n` and a list `a` of `n` integers. It calculates a value `year` by summing up `(year % ai or ai)` for each element `ai` in `a`. The function prints the calculated `year` for each test case. After processing all test cases, the function completes, and no further state is maintained.

