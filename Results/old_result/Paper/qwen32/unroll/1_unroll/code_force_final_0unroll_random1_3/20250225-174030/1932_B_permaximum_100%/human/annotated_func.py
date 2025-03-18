#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and test_cases is a list of t test cases where each test case consists of an integer n such that 1 <= n <= 100, followed by a list of n integers a_1, a_2, ..., a_n such that 1 <= a_i <= 10^6 for each i.
def func_1(t, test_cases):
    results = []
    for test in test_cases:
        n, a = test
        
        current_year = 0
        
        for ai in a:
            if current_year % ai == 0:
                next_year = current_year + ai
            else:
                next_year = (current_year // ai + 1) * ai
            current_year = next_year
        
        results.append(current_year)
        
    #State: `t` is an integer such that 1 <= t <= 1000, and `test_cases` is a list of `t` test cases where each test case consists of an integer `n` such that 1 <= `n` <= 100, followed by a list of `n` integers `a_1, a_2, ..., a_n` such that 1 <= `a_i` <= 10^6 for each `i`; `results` is a list of `t` integers where each integer is the smallest year that is a multiple of all the integers in the corresponding test case's list.
    return results
    #The program returns `results`, which is a list of `t` integers where each integer is the smallest year that is a multiple of all the integers in the corresponding test case's list.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases and a list `test_cases` containing `t` test cases. Each test case consists of an integer `n` followed by a list of `n` integers. The function returns a list of `t` integers, where each integer is the smallest year that is a multiple of all the integers in the corresponding test case's list.

