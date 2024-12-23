#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 50, x is a list of n integers where each integer x_i satisfies 0 <= x_i <= 1000, and y is a list of n integers where each integer y_i satisfies 0 <= y_i <= 1000.
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
    #State of the program after the if-else block has been executed: *`n` is an input positive integer such that 1 <= `n` <= 50; `x` is a list of `n` integers as an input from the user; and `y` is a new list of `n` integers satisfying `0 <= y_i <= 1000`. If `total_y` (the sum of the integers in list `y`) is greater than `total_x` (the sum of the integers in list `x`), the output is 'No'. Otherwise, the output is 'Yes', indicating that `total_y` is less than or equal to `total_x`.
#Overall this is what the function does:The function reads an integer `n` representing the number of elements in two lists, `x` and `y`, from user input. It then reads the elements of these lists, both of which must contain `n` integers within specified bounds. The function calculates the sum of elements in both lists, `total_x` and `total_y`. If `total_y` is greater than `total_x`, it prints 'No'; otherwise, it prints 'Yes'. The function does not handle cases where the input format is incorrect (e.g., if the number of integers provided does not match `n`, or if non-integer values are given), nor does it provide any output or return value based on the user's input beyond the printed results. Therefore, the final state of the program includes the integer sums computed and the printed result based on their comparison.

