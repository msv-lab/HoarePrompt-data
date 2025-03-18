#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and test_cases is a list of t test cases where each test case is a tuple (n, a) with n being an integer such that 1 <= n <= 100 and a being a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^6.
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
        
    #State: `results` is a list containing the Least Common Multiple (LCM) of the list `a` for each test case in `test_cases`.
    return results
    #The program returns the list `results` which contains the Least Common Multiple (LCM) of the list `a` for each test case in `test_cases`.
#Overall this is what the function does:The function accepts an integer `t` representing the number of test cases and a list `test_cases` containing `t` test cases. Each test case consists of an integer `n` and a list `a` of `n` integers. The function calculates the Least Common Multiple (LCM) of the integers in each list `a` and returns a list of these LCM values corresponding to each test case.

