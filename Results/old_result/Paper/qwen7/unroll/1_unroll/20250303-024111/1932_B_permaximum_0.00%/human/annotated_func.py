#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n is an integer such that 1 ≤ n ≤ 100, and a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 10^6.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: Output State: `t` integers representing the value of `year` calculated from the given loop for each input test case. Each integer corresponds to the sum of the series where each term is the minimum of the previous term and the current element in the list `a`. The value of `n` and the list `a` change with each iteration based on user input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers `a`. For each test case, it calculates a value `year` based on the input list `a`, where `year` is incremented by the minimum of itself and each element in the list `a`. Finally, it prints the calculated `year` for each test case.

