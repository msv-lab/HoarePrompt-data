#State of the program right berfore the function call: c is a list of integers where 1 ≤ len(c) ≤ 18 and 0 ≤ c[i] ≤ 10^7 for each i in the range of the length of c.
def func_1(c):
    m = 0
    if (c == 2) :
        print(f'4 1')
        #This is printed: 4 1
        print(f'1 2')
        #This is printed: 1 2
    else :
        print(f'13 0')
        #This is printed: 13 0
    #State: `c` is a list of integers where 1 ≤ len(c) ≤ 18 and 0 ≤ c[i] ≤ 10^7 for each i in the range of the length of c; `m` is 0. If `c` is equal to 2, the current value of `c` is equal to 2. Otherwise, `c` is not equal to 2.
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function `func_1` accepts a list of integers `c` with a length between 1 and 18, where each integer is between 0 and 10^7. It prints either "4 1" followed by "1 2" if `c` is equal to 2 (which is not possible since `c` is a list), or "13 0" otherwise. The function does not return anything (None).

