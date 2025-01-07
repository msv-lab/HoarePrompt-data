#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and x and y are lists of n integers each, where 0 ≤ x[i] ≤ 1000 and 0 ≤ y[i] ≤ 1000 for all 0 ≤ i < n.
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
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ n ≤ 50; `y` is a list of `n` integers (new values); `total_x` is the sum of all elements in the list `x`; `total_y` is the sum of all elements in the list `y`; if `total_y` is greater than `total_x`, the console prints 'No'. Otherwise, the console prints 'Yes'.
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 50) and two lists `x` and `y`, each containing `n` integers. It calculates the sum of elements in `x` and `y` and prints "No" if the sum of `y` is greater than the sum of `x`, otherwise it prints "Yes". Note that the function assumes `n` is within the valid range, but does not explicitly handle cases where `n` is outside this range.

