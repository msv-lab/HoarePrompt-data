#State of the program right berfore the function call: No variables in the function signature. The function `func_1` does not take any parameters.
def func_1():
    return int(putin())
    #The program returns the integer value of whatever `putin()` returns
#Overall this is what the function does:The function `func_1` does not accept any parameters and returns the integer value returned by the function `putin()`.

#State of the program right berfore the function call: No variables are present in the function signature.
def func_2():
    return map(int, putin().split())
    #The program returns a map object containing integers derived from splitting the user's input string and converting each split substring to an integer.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It prompts the user for input, splits the input string into substrings, converts each substring to an integer, and returns a map object containing these integers.

#State of the program right berfore the function call: main_ar and sec_arr are lists of tuples, where each tuple contains two integers. Specifically, main_ar contains tuples (a_i, b_i) representing the prices of items for Alice and Bob, and sec_arr also contains tuples (a_i, b_i) representing the prices of items for Alice and Bob.
def func_3(main_ar, sec_arr):
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: `main_ar` and `sec_arr` are lists of tuples, where each tuple contains two integers; `sub_summ` is the sum of the first elements of all tuples in `sec_arr`.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: `sub_summ` is the sum of the initial `sub_summ` and the sums of the elements of each tuple in `main_ar` where the sum of the elements is non-negative. The lists `main_ar` and `sec_arr` remain unchanged.
    return sub_summ
    #The program returns `sub_summ` which is the sum of the initial `sub_summ` and the sums of the elements of each tuple in `main_ar` where the sum of the elements is non-negative.
#Overall this is what the function does:The function takes two lists of tuples, `main_ar` and `sec_arr`, where each tuple contains two integers. It calculates the sum of the first elements of all tuples in `sec_arr` and adds to this the sum of the elements of each tuple in `main_ar` where the sum of the elements is non-negative. The function returns this calculated sum.

