#State of the program right berfore the function call: c is a list of integers where 1 <= len(c) <= 18 and 0 <= c[i] <= 10^7 for all i in the range of the length of c.
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
    #State: `c` is a list of integers where 1 <= len(c) <= 18 and 0 <= c[i] <= 10^7 for all i in the range of the length of c; `m` is 0. If `c` contains exactly one element and that element is 2, then `c` is a list containing a single element, 2. Otherwise, `c` is not equal to 2.
    return
    #The program returns nothing (None)
#Overall this is what the function does:The function accepts a list `c` of integers with a length between 1 and 18, where each integer is between 0 and 10,000,000. It prints specific lines based on whether the list `c` contains exactly one element with the value 2 or not. The function does not return any value (None).

