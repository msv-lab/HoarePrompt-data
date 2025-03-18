#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a_1, a_2, a_3, \dots, a_n are integers such that 1 ≤ a_i ≤ 10^6.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: Output State: After the loop executes all its iterations, `t` remains an integer such that 1 ≤ `t` ≤ 1000, `n` is the last input integer received, `a` is an empty list, and `year` is the cumulative result of applying the operation `year += year % ai or ai` for each element `ai` in the list `a` for all iterations. The value of `year` is the final computed value after processing all elements in all lists `a` for each iteration specified by `t`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer t indicating the number of subsequent test cases, followed by an integer n and a list of n integers. For each test case, it calculates a cumulative value `year` by iterating through the list of integers and applying the operation `year += year % ai or ai`. Finally, it prints the computed `year` value for each test case.

