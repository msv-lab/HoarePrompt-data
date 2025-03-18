#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, n is an integer such that 1 <= n <= 100, and a_i are integers such that 1 <= a_i <= 10^6 for each i from 1 to n.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: The value of `t` is 0, `n` is the last input integer received (1 <= n <= 100), and `a` is the last list of integers received (1 <= a_i <= 10^6 for each i from 1 to n). The variable `year` is the sum of the values `year % ai or ai` for each `ai` in the last list `a`.
#Overall this is what the function does:The function `func` reads an integer `t` (1 <= t <= 1000) from the input, indicating the number of test cases. For each test case, it reads an integer `n` (1 <= n <= 100) and a list of `n` integers `a_i` (1 <= a_i <= 10^6). It then calculates a value `year` by summing `year % ai or ai` for each `ai` in the list `a`. The function prints the calculated `year` for each test case. After processing all test cases, the value of `t` is 0, `n` is the last input integer received, and `a` is the last list of integers received. The variable `year` holds the final calculated value for the last test case.

