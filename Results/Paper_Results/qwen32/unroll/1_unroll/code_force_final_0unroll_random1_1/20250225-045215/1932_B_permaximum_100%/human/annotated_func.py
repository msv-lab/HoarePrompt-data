#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and test_cases is a list of t test cases. Each test case is a tuple (n, a), where n is an integer such that 1 <= n <= 100, and a is a list of n integers representing the periodicities of the signs, with each integer a_i satisfying 1 <= a_i <= 10^6.
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
        
    #State: `results` is a list of `t` integers, where each integer is the first common year when all signs change for the corresponding test case.
    return results
    #The program returns a list of `t` integers, where each integer is the first common year when all signs change for the corresponding test case.
#Overall this is what the function does:The function calculates the first common year when all signs change for each test case, given the periodicities of the signs, and returns a list of these years.

