#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 100, and a list of integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 <= a_i <= 10^6.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: t printed values of year, one for each iteration of the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then calculates a value `year` for each test case based on the list of integers and prints this value. The final state of the program is that it has printed `t` values, one for each test case.

