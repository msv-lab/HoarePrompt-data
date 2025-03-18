#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and test_cases is a list of test case descriptions. Each test case description is a tuple where the first element is an integer n such that 1 ≤ n ≤ 100, and the second element is a list of n integers a_1, a_2, a_3, \dots, a_n such that 1 ≤ a_i ≤ 10^6.
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
        
    #State: Output State: `results` is a list containing the final year `current_year` for each test case after executing the loop. For each test case `(n, a)`, `current_year` is updated based on the conditions inside the inner loop, starting from `0` and iterating through each `ai` in `a`. The final value of `current_year` for each test case is appended to `results`.
    return results
    #The program returns a list `results` containing the final year `current_year` for each test case after executing the loop. For each test case `(n, a)`, `current_year` is updated based on the conditions inside the inner loop, starting from `0` and iterating through each `ai` in `a`. The final value of `current_year` for each test case is appended to `results`.
#Overall this is what the function does:The function `func_1` accepts two parameters: `t`, a positive integer between 1 and 1000, and `test_cases`, a list of test case descriptions. Each test case description consists of an integer `n` (1 ≤ n ≤ 100) and a list of `n` integers `a_1, a_2, ..., a_n` (1 ≤ a_i ≤ 10^6). It returns a list `results` containing the final year `current_year` for each test case after executing a loop. For each test case `(n, a)`, `current_year` starts at 0 and iterates through each `ai` in `a`, updating `current_year` based on specific conditions. The final value of `current_year` for each test case is appended to `results`.

