#State of the program right berfore the function call: c is a list of integers where the length of the list n satisfies 1 ≤ n ≤ 18, and each element a_i in the list satisfies 0 ≤ a_i ≤ 10^7.
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
    #State: Postcondition: `c` is a list of integers where the length of the list n satisfies 1 ≤ n ≤ 18, and each element a_i in the list satisfies 0 ≤ a_i ≤ 10^7; `m` is 0, and if the list `c` is equal to [2], then no change is made to `m`; otherwise, no change is made to `m` as well.
    return
    #The program returns 0
#Overall this is what the function does:The function accepts a list of integers `c`. It checks if the length of the list `c` is exactly 2. If true, it prints "4 1" followed by "1 2". Otherwise, it prints "13 0". Regardless of the condition, the value of `m` remains unchanged and is set to 0 initially. The function returns 0.

