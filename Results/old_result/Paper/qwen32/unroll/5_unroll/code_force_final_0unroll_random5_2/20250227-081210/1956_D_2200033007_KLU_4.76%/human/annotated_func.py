#State of the program right berfore the function call: c is a list of integers where the length of c (denoted as n) satisfies 1 <= n <= 18, and each element in c satisfies 0 <= a_i <= 10^7.
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
    #State: `c` is a list of integers where the length of `c` (denoted as `n`) satisfies 1 <= `n` <= 18, and each element in `c` satisfies 0 <= `a_i` <= 10^7; `m` is 0. If `c` is equal to 2, the current value of `c` is 2. Otherwise, `c` is not equal to 2.
    return
    #The program returns None
#Overall this is what the function does:The function `func_1` accepts a parameter `c`, which is a list of integers with a length between 1 and 18, and each element in the list is between 0 and 10,000,000. The function prints specific lines based on whether `c` is equal to 2 (which is not possible as `c` is a list) or not, and always returns `None`.

