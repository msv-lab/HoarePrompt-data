#State of the program right berfore the function call: No variables are present in the function signature.
def func_1():
    return int(putin())
    #The program returns the integer value obtained from the `putin()` function
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns an integer value obtained from the `putin()` function.

#State of the program right berfore the function call: No variables are present in the function signature, so there are no preconditions related to variables.
def func_2():
    return map(int, putin().split())
    #The program returns a map object that applies the int function to each element of the input string, which is split by spaces. The input string is obtained from the function `putin()`.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It retrieves a string from the `putin()` function, splits this string into substrings separated by spaces, converts each substring to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: main_ar and sec_arr are lists of tuples where each tuple contains two integers. Each tuple in main_ar and sec_arr represents the prices (a_i, b_i) for Alice and Bob respectively for a particular item.
def func_3(main_ar, sec_arr):
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: `main_ar` and `sec_arr` are lists of tuples where each tuple contains two integers representing the prices (a_i, b_i) for Alice and Bob respectively for a particular item; `sub_summ` is the sum of the first elements of all tuples in `sec_arr`.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: sub_summ is the sum of the first elements of all tuples in sec_arr plus the sum of (a_i + b_i) for each tuple (a_i, b_i) in main_ar where (a_i + b_i) >= 0.
    return sub_summ
    #The program returns `sub_summ`, which is the sum of the first elements of all tuples in `sec_arr` plus the sum of `(a_i + b_i)` for each tuple `(a_i, b_i)` in `main_ar` where `(a_i + b_i) >= 0`.
#Overall this is what the function does:The function takes two lists of tuples, `main_ar` and `sec_arr`, where each tuple contains two integers representing prices for Alice and Bob. It calculates the sum of the first elements of all tuples in `sec_arr` and adds to it the sum of the sums of the elements in each tuple from `main_ar` where the sum of the elements is non-negative. The function returns this calculated sum.

