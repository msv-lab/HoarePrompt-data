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
        
    #State: After the loop executes all the iterations, `t` is 0, `n` has been an input integer for each iteration, `a` has been a new list of integers provided by the user for each iteration, and `year` has been calculated as the sum of `(year % ai or ai)` for each `ai` in the list `a` for each iteration.
#Overall this is what the function does:The function reads a series of test cases, each consisting of a number of signs and their periodicities. For each test case, it calculates a specific value (`year`) based on the periodicities and prints this value. The function does not return any values; instead, it outputs the results directly to the console. After processing all test cases, the function completes its execution.

