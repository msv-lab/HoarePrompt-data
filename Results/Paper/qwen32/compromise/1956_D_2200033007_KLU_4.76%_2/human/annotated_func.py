#State of the program right berfore the function call: c is a list of integers where the length of c is between 1 and 18 inclusive, and each integer in c is between 0 and 10^7 inclusive.
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
    #State: `c` is a list of integers where the length of `c` is between 1 and 18 inclusive, and each integer in `c` is between 0 and 10^7 inclusive; `m` is 0. If `c` is equal to 2, the condition is evaluated based on the assumption that `c` is a list, so this part of the condition will never be true. Otherwise, `c` is not equal to 2.
    return
    #The program returns None
#Overall this is what the function does:The function `func_1` accepts a parameter `c`, which is a list of integers with a length between 1 and 18 inclusive, and each integer in the list is between 0 and 10^7 inclusive. The function prints either "13 0" or two lines "4 1" followed by "1 2", depending on the value of `c`. However, due to the incorrect condition checking, it will always print "13 0" for any valid input list. The function returns `None`.

