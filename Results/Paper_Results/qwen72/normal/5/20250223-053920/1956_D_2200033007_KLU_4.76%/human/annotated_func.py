#State of the program right berfore the function call: c is a list of integers of length n where 1 ≤ n ≤ 18 and 0 ≤ c_i ≤ 10^7 for all 1 ≤ i ≤ n.
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
    #State: *c is a list of integers of length n where 1 ≤ n ≤ 18 and 0 ≤ c_i ≤ 10^7 for all 1 ≤ i ≤ n, and m is 0. If c is equal to 2, the current value of c is 2. Otherwise, c is not equal to 2.
    return
    #The program returns None.
#Overall this is what the function does:The function `func_1` accepts a list `c` of integers, where the list length is between 1 and 18, and each integer is between 0 and 10^7. It prints either "4 1" and "1 2" if the list `c` contains exactly one element and that element is 2, or it prints "13 0" if the list `c` does not meet this condition. The function returns `None`.

