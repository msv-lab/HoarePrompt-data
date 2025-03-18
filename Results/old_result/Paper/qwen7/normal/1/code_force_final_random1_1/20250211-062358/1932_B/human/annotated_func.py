#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n is a positive integer such that 1 ≤ n ≤ 100, and a_1, a_2, ..., a_n are positive integers such that 1 ≤ a_i ≤ 10^6.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: Output State: The list `a` is empty, `year` is the sum of all elements in the original list `a`, and `n` is the original input integer.
    #
    #In simpler terms, after the loop has executed all its iterations, the list `a` will be empty because all elements have been processed. The variable `year` will hold the cumulative sum of all elements in the original list `a`, as each element `ai` in `a` contributed to `year` in each iteration. The variable `n` remains unchanged as it was not affected by the loop.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer \( t \) indicating the number of sub-cases, then for each sub-case, it reads a positive integer \( n \) and a list of \( n \) positive integers \( a_1, a_2, \ldots, a_n \). It calculates a value `year` by iterating through the list \( a \) and updating `year` based on the current element. Finally, it prints the calculated `year` for each sub-case. After processing all test cases, the list `a` is empty, and the variable `year` holds the cumulative sum of all elements from the original lists across all sub-cases.

