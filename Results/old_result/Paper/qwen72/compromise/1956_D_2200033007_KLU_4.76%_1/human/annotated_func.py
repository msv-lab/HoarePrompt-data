#State of the program right berfore the function call: c is a list of integers of length n (1 ≤ n ≤ 18) where each element a_i in c satisfies 0 ≤ a_i ≤ 10^7.
def func_1(c):
    m = 0
    if (c == 2) :
        print(f'4 1')
        #This is printed: Output:
        print(f'1 2')
        #This is printed: 1 2
    else :
        print(f'13 0')
        #This is printed: 13 0
    #State: *`c` is a list of integers of length n (1 ≤ n ≤ 18) where each element a_i in `c` satisfies 0 ≤ a_i ≤ 10^7, and `m` is 0. If `c` is equal to 2, the current value of `c` is 2. Otherwise, `c` is not equal to 2.
    return
    #The program does not return any value.
#Overall this is what the function does:The function `func_1` accepts a list `c` of integers, where the list has a length between 1 and 18, and each integer is between 0 and 10,000,000. It prints either "4 1" followed by "1 2" if the length of `c` is 2, or "13 0" if the length of `c` is not 2. The function does not return any value.

