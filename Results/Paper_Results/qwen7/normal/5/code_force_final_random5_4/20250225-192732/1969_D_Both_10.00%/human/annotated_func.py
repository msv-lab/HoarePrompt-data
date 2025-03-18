#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2 \cdot 10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, and b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_1():
    return int(putin())
    #The program returns an integer value obtained from the function putin() for each test case.
#Overall this is what the function does:The function processes multiple test cases defined by the integer `t`. For each test case, it uses the `putin()` function to calculate an integer value based on lists `a` and `b`, and integers `n` and `k`. It returns this calculated integer value for each test case.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a and b are lists of integers such that 1 ≤ a_i ≤ 10^9 and 1 ≤ b_i ≤ 10^9 for all i in range n.
def func_2():
    return map(int, putin().split())
    #The program returns a map object containing integers split from a string input.
#Overall this is what the function does:The function processes a string input obtained from `putin().split()` and returns a map object containing the integers split from this string.

#State of the program right berfore the function call: main_ar is a list of pairs (a_i, b_i), where a_i and b_i are integers representing the prices for Alice and Bob respectively; sec_arr is a list of pairs (val_a, val_b) where val_a and val_b are integers.
def func_3(main_ar, sec_arr):
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: Output State: `sub_summ'` is the sum of all elements `[val_a[0]]` in `sec_arr`, `sec_arr` is a non-empty list, `val_a` is the last element in `sec_arr`.
    #
    #This means that after the loop has executed all its iterations, `sub_summ` will hold the sum of the first elements of all the sub-arrays (or lists) in `sec_arr`. The condition that `sec_arr` is a non-empty list remains true, and `val_a` will be the last sub-array processed in `sec_arr`.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: `sub_summ` is the sum of `val_b[0] + val_b[1]` for all `val_b` in `main_ar` where `val_b[0] + val_b[1] >= 0`. `sec_arr` is a non-empty list, `val_a` is the last sub-array in `sec_arr`, and `main_ar` is empty.
    return sub_summ
    #The program returns sub_summ, which is the sum of val_b[0] + val_b[1] for all val_b in main_ar where val_b[0] + val_b[1] >= 0.
#Overall this is what the function does:The function `func_3` takes two parameters: `main_ar`, a list of pairs where each pair consists of two integers representing prices for Alice and Bob; and `sec_arr`, a list of pairs where each pair consists of two integers. It calculates and returns `sub_summ`, which is the sum of the first elements of all pairs in `main_ar` where the sum of the first and second elements of the pairs is greater than or equal to 0.

