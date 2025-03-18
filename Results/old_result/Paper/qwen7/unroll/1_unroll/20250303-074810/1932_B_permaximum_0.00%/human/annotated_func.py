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
        
    #State: The value of `year` after processing each list `a` for every iteration of the outer loop, with `t` being the number of such iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers `a`. For each test case, it calculates a value `year` based on the elements of the list `a` and prints the result. The calculation involves summing up values derived from each element in the list, specifically `year + (year % ai or ai)` for each element `ai`. This process is repeated for `t` test cases, where `t` is the number of test cases provided.

