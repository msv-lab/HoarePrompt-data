#State of the program right berfore the function call: None of the variables in the function signature are used, as the function `func_1` does not take any parameters.
def func_1():
    return int(putin())
    #The program returns an integer value that is the result of calling the `putin()` function.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It returns an integer value that is the result of calling the `putin()` function.

#State of the program right berfore the function call: None of the variables in the function signature are used, as the function does not take any parameters.
def func_2():
    return map(int, putin().split())
    #The program returns a map object that converts the string returned by `putin()` into a list of integers, where `putin()` is expected to return a string of space-separated numbers.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a map object that converts a string of space-separated numbers, returned by the `putin()` function, into a sequence of integers. The final state of the program includes this map object, which can be iterated over to access the integers.

#State of the program right berfore the function call: main_ar and sec_arr are lists of tuples, where each tuple contains two integers. The integers in the tuples represent item prices for Alice and Bob, respectively.
def func_3(main_ar, sec_arr):
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: Output State: `main_ar` remains unchanged; `sec_arr` remains unchanged; `sub_summ` is the sum of the first elements of all tuples in `sec_arr`.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: Output State: `main_ar` remains unchanged; `sec_arr` remains unchanged; `sub_summ` is the sum of the first elements of all tuples in `sec_arr` plus the sum of the first and second elements of all tuples in `main_ar` where the sum of the first and second elements is non-negative.
    return sub_summ
    #The program returns the sum of the first elements of all tuples in `sec_arr` plus the sum of the first and second elements of all tuples in `main_ar` where the sum of the first and second elements is non-negative.
#Overall this is what the function does:The function `func_3` accepts two lists of tuples, `main_ar` and `sec_arr`, where each tuple contains two integers representing item prices for Alice and Bob, respectively. It returns the sum of the first elements of all tuples in `sec_arr` plus the sum of the first and second elements of all tuples in `main_ar` where the sum of these elements is non-negative. Both `main_ar` and `sec_arr` remain unchanged after the function execution.

