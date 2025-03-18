#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 1 <= n <= 100, and a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 <= a_i <= 10^6.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: a series of t printed values of year, each derived from the respective list a provided in each iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it calculates a value `year` based on the provided integers and prints this value. Specifically, for each integer in the list, it updates `year` by adding either the integer itself or the remainder of `year` divided by the integer, whichever is non-zero.

