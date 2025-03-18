#State of the program right berfore the function call: The function should take two parameters: t (1 ≤ t ≤ 1000), the number of test cases, and a list of lists, where each inner list contains n (1 ≤ n ≤ 100) integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6), representing the periodicities of the signs for each test case.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: The loop will print the value of `year` for each test case, where `year` is the sum of the smallest non-zero remainder of `year` when divided by each `ai` in the list `a`, or `ai` itself if the remainder is zero. After all iterations, the variables `t` and the list of lists remain unchanged.
#Overall this is what the function does:The function `func` takes no parameters and reads input from the standard input. It processes `t` test cases, where `t` is an integer (1 ≤ t ≤ 1000). For each test case, it reads an integer `n` (1 ≤ n ≤ 100) and a list of `n` integers (1 ≤ a_i ≤ 10^6) representing periodicities. The function calculates the sum of the smallest non-zero remainder of `year` when divided by each periodicity in the list, or the periodicity itself if the remainder is zero. It prints this sum for each test case. The function does not return any value. After the function concludes, the input variables `t` and the list of periodicities are consumed and not retained.

