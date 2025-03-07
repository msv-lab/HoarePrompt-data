#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and test_cases is a list of t elements, where each element is a tuple (n, a) where n is a positive integer such that 1 <= n <= 100, and a is a list of n positive integers such that 1 <= a_i <= 10^6.
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
        
    #State: `results` is a list of t elements, where each element is the smallest positive integer that is a multiple of all the integers in the corresponding list `a` from `test_cases`.
    return results
    #The program returns the list `results`, where each element in `results` is the smallest positive integer that is a multiple of all the integers in the corresponding list `a` from `test_cases`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `t` and a list `test_cases` of `t` tuples, each containing a positive integer `n` and a list `a` of `n` positive integers. It returns a list `results` where each element is the smallest positive integer that is a multiple of all the integers in the corresponding list `a` from `test_cases`. The input `test_cases` remains unchanged after the function call.

