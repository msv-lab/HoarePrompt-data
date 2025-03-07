#State of the program right berfore the function call: None, as the function `func_1` does not take any parameters.
def func_1():
    return int(putin())
    #The program returns an integer value that is input by the user when the `putin()` function is called.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It returns an integer value that is input by the user when the `putin()` function is called. The final state of the program after the function concludes is that an integer value provided by the user is returned.

#State of the program right berfore the function call: None, as the function does not take any arguments.
def func_2():
    return map(int, putin().split())
    #The program returns an iterator that will convert each string in the input provided by the `putin()` function (after splitting the input by spaces) into an integer.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns an iterator that converts each string from the input (split by spaces) provided by the `putin()` function into an integer.

#State of the program right berfore the function call: main_ar and sec_arr are lists of tuples, where each tuple contains two integers. The integers in the tuples represent item prices for Alice and Bob, respectively.
def func_3(main_ar, sec_arr):
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: `sub_summ` is the sum of the first elements of all tuples in `sec_arr`, `sec_arr` remains unchanged, `val_a` is the last tuple in `sec_arr`.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: `sub_summ` is the sum of the first elements of all tuples in `sec_arr` plus the sum of the first and second elements of all tuples in `main_ar` where the sum of the first and second elements is greater than or equal to 0. `sec_arr` remains unchanged, and `val_a` is the last tuple in `sec_arr`.
    return sub_summ
    #The program returns the value of `sub_summ`, which is the sum of the first elements of all tuples in `sec_arr` plus the sum of the first and second elements of all tuples in `main_ar` where the sum of the first and second elements is greater than or equal to 0.
#Overall this is what the function does:The function `func_3` accepts two lists of tuples, `main_ar` and `sec_arr`, and returns a single integer. The integer is the sum of the first elements of all tuples in `sec_arr` plus the sum of the first and second elements of all tuples in `main_ar` where the sum of the first and second elements is greater than or equal to 0. The input lists `main_ar` and `sec_arr` remain unchanged after the function call.

