#State of the program right berfore the function call: The function should accept two parameters: a list of integers `a` representing the periodicities of the signs, and an integer `n` representing the number of signs. The list `a` should have a length of `n` and each element `a_i` should satisfy 1 ≤ a_i ≤ 10^6. Additionally, the function should be able to handle multiple test cases, where the number of test cases `t` satisfies 1 ≤ t ≤ 1000.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: The variable `year` will be the sum of the smallest non-zero multiples of each element in the list `a` for each test case, and the result will be printed for each test case. The variables `t`, `n`, and `a` will retain their values as they were at the end of the last iteration of the loop.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers `a`. It calculates the smallest non-zero multiple of each element in `a` and sums these values to produce a result `year`. The function prints `year` for each test case. After processing all test cases, the variables `t`, `n`, and `a` retain their values from the last iteration, and the function does not return any value.

