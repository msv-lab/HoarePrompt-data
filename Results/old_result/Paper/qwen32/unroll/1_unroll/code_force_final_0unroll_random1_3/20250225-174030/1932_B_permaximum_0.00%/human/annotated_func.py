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
        
    #State: For each test case, the variable `year` will hold the cumulative sum calculated by the inner loop, where for each integer `ai` in the list `a`, `year` is incremented by `year % ai` if `year % ai` is not zero, otherwise it is incremented by `ai`. The final value of `year` for each test case is printed. The variables `t`, `n`, and `a` will not retain their values after the loop completes the iteration for that test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a list of integers. For each test case, it calculates a cumulative sum based on the elements of the list and prints the result. Specifically, for each integer in the list, if the current cumulative sum modulo the integer is non-zero, the cumulative sum is incremented by that modulo value; otherwise, it is incremented by the integer itself.

