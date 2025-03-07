#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a is a list of n integers such that 1 ≤ a_i ≤ 10^9, and b is a list of n integers such that 1 ≤ b_i ≤ 10^9.
def func_1():
    return int(putin())
    #The program returns an integer value obtained from the function putin() for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( t \), \( n \), and \( k \), along with two lists \( a \) and \( b \). For each test case, it calls another function `putin()` to obtain an integer value. The function returns a list of these integer values, one for each test case.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are integers such that 1 ≤ n ≤ 2⋅10^5 and 0 ≤ k ≤ n. a and b are lists of integers such that 1 ≤ a_i ≤ 10^9 and 1 ≤ b_i ≤ 10^9 for all i in range n.
def func_2():
    return map(int, putin().split())
    #The program returns a map object containing integers split from the input string.
#Overall this is what the function does:The function processes an input string by splitting it and converting the resulting substrings into integers, returning a map object containing these integers.

#State of the program right berfore the function call: main_ar is a list of tuples, where each tuple contains two integers (a_i, b_i). sec_arr is a list of integers. The length of main_ar is n, and the length of sec_arr is also n.
def func_3(main_ar, sec_arr):
    sub_summ = 0
    for val_a in sec_arr:
        sub_summ += val_a[0]
        
    #State: Output State: `sub_summ` is the sum of the first element of each sublist in `sec_arr`.
    for val_b in main_ar:
        if val_b[0] + val_b[1] >= 0:
            sub_summ += val_b[0] + val_b[1]
        
    #State: `sub_summ` is the sum of the first and second elements of each sublist in `main_ar` where their sum is greater than or equal to 0.
    return sub_summ
    #The program returns `sub_summ`, which is the sum of the first and second elements of each sublist in `main_ar` where their sum is greater than or equal to 0.
#Overall this is what the function does:The function accepts two parameters: `main_ar`, a list of tuples where each tuple contains two integers, and `sec_arr`, a list of integers, both of the same length. It calculates the sum of the first and second elements of each tuple in `main_ar` where their sum is greater than or equal to 0, and returns this sum.

