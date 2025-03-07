#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, and b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_1():
    return int(putin())
    #The program returns an integer value obtained from the function putin() for each test case.
#Overall this is what the function does:The function processes multiple lists and integers (n, k, a, b) for each test case where 1 ≤ t ≤ 10^4. It returns an integer value obtained from the function `putin()` for each test case.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9. b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_2():
    return map(int, putin().split())
    #The program returns a map object containing integers split from the input string.
#Overall this is what the function does:The function accepts an input string, splits it into individual integer values, and returns a map object containing these integers.

#State of the program right berfore the function call: main_ar is a list of tuples, where each tuple contains two integers (a_i, b_i); sec_arr is a list of integers.
def func_3(main_ar, sec_arr):
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: Output State: `main_ar` is a list of tuples, where each tuple contains two integers (a_i, b_i); `sec_arr` is a list of integers; `sub_summ` is the sum of the first elements of all tuples in `sec_arr`.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: `main_ar` is a list of tuples, where each tuple contains two integers (a_i, b_i); `sec_arr` is a list of integers; `sub_summ` is the sum of the first elements of all tuples in `main_ar` if their first and second elements' sum is greater than or equal to 0.
    return sub_summ
    #The program returns the sum of the first elements of all tuples in `main_ar` where the sum of the first and second elements of each tuple is greater than or equal to 0.
#Overall this is what the function does:Functionality: The function accepts two parameters: `main_ar`, a list of tuples where each tuple contains two integers, and `sec_arr`, a list of integers. It calculates and returns the sum of the first elements of all tuples in `main_ar` where the sum of the first and second elements of each tuple is greater than or equal to 0.

