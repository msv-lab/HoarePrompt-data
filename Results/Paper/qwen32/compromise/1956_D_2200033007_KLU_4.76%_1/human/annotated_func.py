#State of the program right berfore the function call: c is a list of integers where 1 <= len(c) <= 18 and 0 <= c[i] <= 10^7 for each i in the range of the length of c.
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
    #State: `c` is a list of integers where 1 <= len(c) <= 18 and 0 <= c[i] <= 10^7 for each i in the range of the length of c. If `c` is a list containing a single integer 2, then `m` remains 0. Otherwise, `m` remains 0 and `c` is not equal to 2.
    return
    #The program returns nothing.
#Overall this is what the function does:The function `func_1` accepts a list of integers `c` with a length between 1 and 18, where each integer is between 0 and 10^7. It prints specific lines based on whether the list `c` is exactly `[2]` or not. If `c` is `[2]`, it prints "4 1" followed by "1 2". Otherwise, it prints "13 0". The function does not return any value.

