#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and test_cases is a list of t test cases where each test case is represented as a tuple (n, a_list). Here, n is an integer such that 1 <= n <= 100, and a_list is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6.
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
        
    #State: t is an integer such that 1 <= t <= 1000, test_cases is a list of t test cases where each test case is represented as a tuple (n, a_list). Here, n is an integer such that 1 <= n <= 100, and a_list is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6, results is a list of t integers where each integer is the smallest year that is a multiple of all the integers in the corresponding a_list.
    return results
    #The program returns a list `results` where each element is the smallest year that is a multiple of all the integers in the corresponding `a_list` from `test_cases`.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases and a list `test_cases` containing `t` test cases. Each test case consists of an integer `n` and a list `a_list` of `n` integers. The function returns a list `results` where each element is the smallest year that is a multiple of all the integers in the corresponding `a_list` from `test_cases`.

