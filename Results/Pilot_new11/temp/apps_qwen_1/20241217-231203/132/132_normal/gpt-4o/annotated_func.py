#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, x is a list of n integers where each integer is between 0 and 1000 inclusive, and y is a list of n integers where each integer is between 0 and 1000 inclusive.
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
    #State of the program after the if-else block has been executed: *`n` is an input integer, `y` is a list of `n` integers where each integer is between 0 and 1000 inclusive, `x` is a list of `n` integers where each integer is between 0 and 1000 inclusive, `total_x` is the sum of all elements in the list `x`, and `total_y` is the sum of all elements in the list `y`. If the total value of `total_y` is greater than the total value of `total_x`, the function does not change the state. Otherwise, 'Yes' is printed to the console.
#Overall this is what the function does:The function `func()` accepts no explicit parameters but reads two lists of integers `x` and `y` from the standard input, where each list contains `n` integers (1 ≤ n ≤ 50) and each integer is between 0 and 1000 inclusive. The function calculates the sum of the elements in both lists (`total_x` for `x` and `total_y` for `y`). After calculating these sums, the function checks if `total_y` is greater than `total_x`. If `total_y` is greater, the function prints "No" to the console; otherwise, it prints "Yes". The final state of the program includes the input integer `n`, the lists `x` and `y`, and the sums `total_x` and `total_y`. There are no explicit outputs returned by the function, but it modifies the standard output based on the comparison of `total_x` and `total_y`.

