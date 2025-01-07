#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 50, x is a list of n integers where each integer x_i is non-negative and satisfies 0 <= x_i <= 1000, and y is a list of n integers where each integer y_i is non-negative and satisfies 0 <= y_i <= 1000.
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
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 <= `n` <= 50; `x` is a list of `n` non-negative integers each satisfying 0 <= `x_i` <= 1000; `y` is a list of `n` integers that are non-negative and are the result of mapping `int` over input values; `total_x` is equal to `sum(x)`; `total_y` is equal to `sum(y)`. If `total_y` is greater than `total_x`, 'No' has been printed. Otherwise, if `total_y` is less than or equal to `total_x`, 'Yes' is printed to the console.
#Overall this is what the function does:The function accepts a positive integer `n`, reads two lists of `n` non-negative integers from user input, calculates the sums of these lists (`total_x` for list `x` and `total_y` for list `y`), and prints 'No' if `total_y` is greater than `total_x`, or 'Yes' otherwise. It does not return any values. The function relies on user input and does not handle edge cases where the input is invalid or does not meet the specified constraints.

