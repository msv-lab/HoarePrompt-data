#State of the program right berfore the function call: No variables are present in the function signature of `func_1()`.
def func_1():
    return int(putin())
    #The program returns the integer value of `putin()`
#Overall this is what the function does:The function `func_1` accepts no parameters and returns the integer value returned by the function `putin()`.

#State of the program right berfore the function call: No variables are present in the function signature of `func_2`.
def func_2():
    return map(int, putin().split())
    #The program returns a map object that contains integers converted from the elements of a string split by whitespace, which is obtained from the `putin()` function.
#Overall this is what the function does:The function `func_2` does not accept any parameters and returns a map object containing integers. These integers are derived from splitting a string obtained from the `putin()` function by whitespace and converting each element to an integer.

#State of the program right berfore the function call: main_ar and sec_arr are lists of tuples, where each tuple contains two integers. main_ar and sec_arr are such that the first element of each tuple in main_ar is the difference between the corresponding b_i and a_i values, and sec_arr contains tuples where the first element is the a_i value.
def func_3(main_ar, sec_arr):
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: `main_ar` and `sec_arr` are lists of tuples, where each tuple contains two integers. `main_ar` and `sec_arr` are such that the first element of each tuple in `main_ar` is the difference between the corresponding `b_i` and `a_i` values, and `sec_arr` contains tuples where the first element is the `a_i` value. `sub_summ` is the sum of all `a_i` values from the tuples in `sec_arr`.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: `main_ar` and `sec_arr` remain unchanged. `sub_summ` is the initial sum of all `a_i` values plus the sum of `(b_i - a_i) + x_i` for all tuples in `main_ar` where `(b_i - a_i) + x_i >= 0`.
    return sub_summ
    #The program returns `sub_summ`, which is the initial sum of all `a_i` values plus the sum of `(b_i - a_i) + x_i` for all tuples in `main_ar` where `(b_i - a_i) + x_i >= 0`.
#Overall this is what the function does:The function calculates the sum of all `a_i` values from `sec_arr` and adds to it the sum of `(b_i - a_i) + x_i` for all tuples in `main_ar` where `(b_i - a_i) + x_i` is greater than or equal to 0. The function returns this calculated sum.

