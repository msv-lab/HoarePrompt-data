#State of the program right berfore the function call: None, as the function `func_1` does not take any parameters.
def func_1():
    return int(putin())
    #The program returns an integer value that is input by the user when the `putin()` function is called.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It returns an integer value that is input by the user when the `putin()` function is called.

#State of the program right berfore the function call: No variables are passed to the function.
def func_2():
    return map(int, putin().split())
    #The program returns an iterator that will convert each element from the input string, obtained by calling `putin().split()`, into an integer.
#Overall this is what the function does:The function `func_2` takes no parameters and returns an iterator that converts each element from the input string, obtained by calling `putin().split()`, into an integer. The input string is split into substrings based on whitespace, and each substring is then converted to an integer. The function does not modify any external variables or state.

#State of the program right berfore the function call: main_ar and sec_arr are lists of tuples, where each tuple contains two integers.
def func_3(main_ar, sec_arr):
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: `main_ar` and `sec_arr` remain unchanged, and `sub_summ` is the sum of the first integers of all tuples in `sec_arr`.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: `main_ar` and `sec_arr` remain unchanged, and `sub_summ` is the sum of the first integers of all tuples in `sec_arr` plus the sum of the first and second elements of all tuples in `main_ar` where the sum is greater than or equal to 0.
    return sub_summ
    #The program returns the sum of the first integers of all tuples in `sec_arr` plus the sum of the first and second elements of all tuples in `main_ar` where the sum is greater than or equal to 0.
#Overall this is what the function does:The function `func_3` takes two parameters, `main_ar` and `sec_arr`, which are lists of tuples containing two integers each. It calculates the sum of the first integers of all tuples in `sec_arr` and adds to it the sum of the first and second elements of all tuples in `main_ar` where the sum of the elements is greater than or equal to 0. The function returns this total sum. The input lists `main_ar` and `sec_arr` remain unchanged.

