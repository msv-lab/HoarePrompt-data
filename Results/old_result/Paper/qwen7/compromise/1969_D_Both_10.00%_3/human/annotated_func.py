#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9. b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_1():
    return int(putin())
    #The program returns an integer value obtained from the function putin() for each test case.
#Overall this is what the function does:The function processes multiple lists and integers within its scope and returns an integer value obtained from the function `putin()` for each test case.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9. b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_2():
    return map(int, putin().split())
    #The program returns a map object containing integers split from the input string.
#Overall this is what the function does:The function processes an input string, splits it into individual elements, converts these elements to integers, and returns a map object containing these integers.

#State of the program right berfore the function call: main_ar is a list of pairs (a_i, b_i), where a_i and b_i are integers representing the prices of items for Alice and Bob respectively; sec_arr is a list of integers representing additional values that are not used in the provided function.
def func_3(main_ar, sec_arr):
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: Output State: `sub_summ` is the sum of all `val_a[0]` values in `sec_arr`, `sec_arr` is a non-empty list, `val_a` is the last element in `sec_arr`.
    #
    #This means that after the loop has executed all its iterations, `sub_summ` will hold the sum of the first elements (`val_a[0]`) of all the tuples in `sec_arr`. The condition that `sec_arr` is a non-empty list remains unchanged, and `val_a` will be the last tuple in the original `sec_arr` that was processed by the loop.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: After the loop executes all iterations, `sub_summ` will be the sum of all `val_a[0]` values in `sec_arr`, `sec_arr` is a non-empty list, and `val_a` is the last tuple in `sec_arr`.
    return sub_summ
    #The program returns `sub_summ`, which is the sum of all `val_a[0]` values in `sec_arr`.
#Overall this is what the function does:The function `func_3` accepts two parameters: `main_ar`, a list of pairs where each pair consists of two integers representing prices for Alice and Bob; and `sec_arr`, a list of integers. It calculates and returns `sub_summ`, which is the sum of all first elements from the tuples in `sec_arr`. The function iterates over `sec_arr` to sum the first elements of its tuples and then iterates over `main_ar` to add the sum of each pair's elements (if their sum is non-negative) to `sub_summ`.

