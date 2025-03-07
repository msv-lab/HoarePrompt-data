#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 100, representing the number of signs. a is a list of n integers, where each integer a_i satisfies 1 ≤ a_i ≤ 10^6, representing the periodicity of each sign.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: `t` is an integer such that 0 ≤ t ≤ 0, `n` is an input integer within the range 1 to 1000, `a` is a list of integers with exactly `n` elements, `year` is the sum of the elements in the list `a` where each element `ai` contributes either `ai` or `year % ai` if `year % ai` is non-zero for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers. It calculates a value `year` by iterating over the list `a`, adding either the current element `ai` or the remainder of `year` divided by `ai` (if non-zero) to `year`. The function prints the calculated `year` for each test case. After processing all test cases, the function completes, and the final state includes `t` being reduced to 0, `n` and `a` being updated for each test case, and `year` being the calculated value for each test case.

