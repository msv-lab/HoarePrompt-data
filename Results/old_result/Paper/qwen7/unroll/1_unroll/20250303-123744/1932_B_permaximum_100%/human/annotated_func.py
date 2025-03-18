#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and test_cases is a list of test case descriptions. Each test case description is a tuple containing an integer n (1 ≤ n ≤ 100) and a list of n integers a_1, a_2, a_3, …, a_n (1 ≤ a_i ≤ 10^6).
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
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 1000, `test_cases` is a list of test case descriptions, `results` is a list of integers where each integer represents the final value of `current_year` after executing the inner loop for each test case.
    return results
    #The program returns a list of integers where each integer represents the final value of `current_year` after executing the inner loop for each test case.
#Overall this is what the function does:The function accepts two parameters: `t`, a positive integer between 1 and 1000, and `test_cases`, a list of tuples. Each tuple contains an integer `n` (between 1 and 100) and a list of `n` integers (each between 1 and 10^6). It processes each test case by iterating over the list of integers and updating a variable `current_year` based on certain conditions. After processing all test cases, it returns a list of integers where each integer represents the final value of `current_year` for each test case.

