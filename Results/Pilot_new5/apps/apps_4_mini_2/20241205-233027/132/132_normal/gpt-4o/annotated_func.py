#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 50, x is a list of n non-negative integers where each element x_i satisfies 0 <= x_i <= 1000, and y is a list of n non-negative integers where each element y_i satisfies 0 <= y_i <= 1000.
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
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that 1 <= n <= 50; `x` is a list of `n` non-negative integers derived from input where each element `x_i` satisfies 0 <= `x_i` <= 1000; `y` is a list of `n` non-negative integers derived from input; `total_x` is the sum of the elements in `x`; `total_y` is the sum of the elements in `y`. If `total_y` is greater than `total_x`, then 'No' is printed. Otherwise, if `total_y` is less than or equal to `total_x`, then 'Yes' is printed.
#Overall this is what the function does:The function accepts a positive integer `n` (1 <= n <= 50) and two lists `x` and `y`, each containing `n` non-negative integers (0 <= x_i, y_i <= 1000). It calculates the sum of the integers in both lists and prints 'No' if the sum of list `y` is greater than the sum of list `x`, otherwise it prints 'Yes'. There are no return values, and the function relies on user input for the lists.

