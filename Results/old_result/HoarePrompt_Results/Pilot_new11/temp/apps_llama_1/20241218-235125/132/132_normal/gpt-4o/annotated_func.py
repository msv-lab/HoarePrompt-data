#State of the program right berfore the function call: The input consists of a positive integer n, two lists of non-negative integers x and y, each of length n, where 1 <= n <= 50 and 0 <= x_i, y_i <= 1000 for all i.
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
    #State of the program after the if-else block has been executed: *`n` is a positive integer between 1 and 50, `x` is a list of `n` integers between 0 and 1000 (inclusive), `y` is a list of integers with each integer between 0 and 1000 (inclusive), `total_x` is an integer between 0 and 50000 (inclusive) equal to the sum of all elements in `x`, and `total_y` is an integer equal to the sum of all elements in `y`. If `total_y` is greater than `total_x`, 'No' has been printed. Otherwise, 'Yes' has been printed.
#Overall this is what the function does:The function determines whether the sum of elements in list `y` is less than or equal to the sum of elements in list `x` for two input lists `x` and `y` of the same length `n`, where `n` is a positive integer between 1 and 50, and each element in both lists is a non-negative integer between 0 and 1000 (inclusive). It accepts no parameters but instead reads `n`, `x`, and `y` directly from the input. The function then prints 'Yes' if the sum of `y` is less than or equal to the sum of `x`, and 'No' otherwise, after which the program concludes, leaving the input variables in their initial state. The function does not modify the input lists or `n`. It handles all potential edge cases as specified by the input constraints, including when the sums of `x` and `y` are equal, or when one is greater than the other. The function does not handle cases where `n` is outside the specified range or where the lists `x` and `y` are not of the correct length or contain invalid values, as these cases are not explicitly addressed in the provided code.

