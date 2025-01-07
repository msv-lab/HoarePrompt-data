#State of the program right berfore the function call: n is an integer such that 1 <= n <= 50; x is a list of n integers where each integer x_i is in the range 0 <= x_i <= 1000; y is a list of n integers where each integer y_i is in the range 0 <= y_i <= 1000.
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
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 <= `n` <= 50; `x` is a list of `n` integers where each integer `x_i` is in the range 0 <= `x_i` <= 1000; `y` is a list of `n` integers where each integer `y_i` is in the range 0 <= `y_i` <= 1000; `total_x` is the sum of the integers in `x`; `total_y` is the sum of the integers in `y`. If `total_y` is greater than `total_x`, the output is 'No'. Otherwise, if `total_y` is less than or equal to `total_x`, 'Yes' has been printed.
#Overall this is what the function does:The function reads an integer `n` and two lists of integers `x` and `y`, each containing `n` integers. It calculates the total sum of the integers in both lists. If the sum of the integers in list `y` is greater than that in list `x`, the function prints 'No'; otherwise, it prints 'Yes'. The function does not return a value but provides output based on the comparison of the sums.

