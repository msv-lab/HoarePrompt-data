#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 50, x is a list of n non-negative integers where each integer is between 0 and 1000, and y is a list of n non-negative integers where each integer is between 0 and 1000.
def func():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    total_x = sum(x)
    total_y = sum(y)
    if (total_y > total_x) :
        print('No')
    else :
        print('Yes')
    #State of the program after the if-else block has been executed: *`y` is a list of `n` non-negative integers where each integer is between 0 and 1000; `n` is the length of `y`; `x` is a list of integers derived from the input; `total_x` is the sum of integers in `x`; `total_y` is the sum of the integers in `y`. If `total_y` is greater than `total_x`, the output is 'No'. Otherwise, the output is 'Yes', indicating that the sum of the integers in `y` is less than or equal to the sum of the integers in `x`.
#Overall this is what the function does:The function reads an integer `n` from input, followed by two lists of `n` non-negative integers (`x` and `y`). It calculates the sums of these lists (`total_x` and `total_y`) and prints 'No' if the sum of `y` is greater than the sum of `x`; otherwise, it prints 'Yes'. There are no parameters passed to the function, and it assumes valid input as specified in the comments.

