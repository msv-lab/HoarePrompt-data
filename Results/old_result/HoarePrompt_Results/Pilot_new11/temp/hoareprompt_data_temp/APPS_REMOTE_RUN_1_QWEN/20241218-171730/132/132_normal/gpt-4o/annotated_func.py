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
    #State of the program after the if-else block has been executed: *`n` is the length of the list `x`, `x` is a list of integers each between 0 and 1000 (inclusive), `y` is a list of integers each between 0 and 1000 (inclusive) with the same length as `x`, `total_x` is the sum of the elements in the list `x`, and `total_y` is the sum of the elements in the list `y`. If `total_y` is greater than `total_x`, 'No' is printed to the console. Otherwise, 'Yes' is printed to the console.
#Overall this is what the function does:The function reads an integer `n` and two lists `x` and `y` from standard input, where `n` is between 1 and 50, and each element in `x` and `y` is between 0 and 1000. It calculates the sums of the elements in `x` and `y`, and prints 'Yes' if the sum of `y` is less than or equal to the sum of `x`, otherwise it prints 'No'. The function does not return any value. There are no edge cases mentioned in the annotations or the code that need special handling.

