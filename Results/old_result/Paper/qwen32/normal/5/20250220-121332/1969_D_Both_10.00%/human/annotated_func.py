#State of the program right berfore the function call: The function `func_1` does not have any parameters.
def func_1():
    return int(putin())
    #The program returns the integer value of whatever `putin()` returns.
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns the integer value that the function `putin()` returns.

#State of the program right berfore the function call: No variables are present in the function signature. Therefore, no precondition can be derived from the variables in the function signature alone.
def func_2():
    return map(int, putin().split())
    #The program returns a map object that applies the `int` function to each element of the list obtained by splitting the string input from `putin()`.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads a string input from `putin()`, splits the string into a list of substrings, converts each substring to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: main_ar and sec_arr are lists of tuples, where each tuple contains two integers. Each tuple in main_ar and sec_arr represents the prices (a_i, b_i) of an item for Alice and Bob, respectively.
def func_3(main_ar, sec_arr):
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: `main_ar` is a list of tuples, `sec_arr` is a list of tuples, `sub_summ` is the sum of the first elements of all tuples in `sec_arr`.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: main_ar
    return sub_summ
    #The program returns `sub_summ`
#Overall this is what the function does:The function `func_3` takes two lists of tuples, `main_ar` and `sec_arr`, where each tuple contains two integers representing prices for Alice and Bob. It calculates a sum, `sub_summ`, by adding the first element of each tuple in `sec_arr` and the sum of both elements of each tuple in `main_ar` where the sum of the tuple's elements is non-negative. The function returns this calculated sum.

