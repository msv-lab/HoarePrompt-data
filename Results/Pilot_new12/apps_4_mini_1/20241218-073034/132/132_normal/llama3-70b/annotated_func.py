#State of the program right berfore the function call: n is an integer such that 1 <= n <= 50, x is a list of integers of length n where each element represents the number of stones in the first visit (0 <= x_i <= 1000), and y is a list of integers of length n where each element represents the number of stones in the second visit (0 <= y_i <= 1000).
def func():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if (sum(x) != sum(y)) :
        print('No')
    else :
        x.sort()
        y.sort()
        if (x == y) :
            print('Yes')
        else :
            print('No')
        #State of the program after the if-else block has been executed: *`n` is an input integer where 1 <= n <= 50; `x` is a sorted list of integers based on input; `y` is a sorted list of integers of length `n` containing the integer inputs after executing the code; the sum of the elements in `x` is equal to the sum of the elements in `y`. If `x` is equal to `y`, the output is 'Yes'. If `x` is not equal to `y`, the output is 'No'.
    #State of the program after the if-else block has been executed: *`n` is an integer where 1 <= `n` <= 50; `x` is a list of integers based on input and `y` is a list of integers of length `n` containing the integer inputs. If the sum of the elements in `x` is not equal to the sum of the elements in `y`, the program prints 'No'. If the sums are equal, then `x` is a sorted list of integers and `y` is also a sorted list of integers; if `x` is equal to `y`, the output is 'Yes'. If `x` is not equal to `y`, the output is 'No'.
#Overall this is what the function does:The function accepts an integer `n` (where 1 <= n <= 50) and two lists of integers `x` and `y`, each of length `n`. The values in `x` represent the number of stones in the first visit, and the values in `y` represent the number of stones in the second visit. It first checks if the sums of the elements in `x` and `y` are equal. If they are not equal, the function outputs 'No'. If the sums are equal, the function then sorts both lists and checks if the sorted lists are identical. If they are the same, it outputs 'Yes'; otherwise, it outputs 'No'. The program does not handle any exceptions or cases where the inputs may not conform to the specified ranges. Moreover, it relies on user input without validating that the inputs are integers or within the expected size limits, which could lead to runtime errors.

