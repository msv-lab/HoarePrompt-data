#State of the program right berfore the function call: c is a list of integers of length n (1 ≤ n ≤ 18), where each element a_i in c satisfies 0 ≤ a_i ≤ 10^7.
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
    #State: *`c` is a list of integers of length n (1 ≤ n ≤ 18), where each element a_i in `c` satisfies 0 ≤ a_i ≤ 10^7; `m` is 0. If the length of `c` is exactly 2, the list `c` has exactly two elements. Otherwise, the list `c` has a length different from 2.
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_1` accepts a list `c` of integers, where the length of the list is between 1 and 18, and each element in the list is between 0 and 10,000,000. The function prints either "4 1" and "1 2" if the length of `c` is exactly 2, or "13 0" otherwise. The function does not return any value. After the function concludes, the list `c` remains unchanged, and the variable `m` is still 0.

