#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 50, x is a list of n integers where each integer x[i] satisfies 0 <= x[i] <= 1000, and y is a list of n integers where each integer y[i] satisfies 0 <= y[i] <= 1000.
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
        #State of the program after the if-else block has been executed: *`n` is the input integer such that 1 <= `n` <= 50; `x` is a list of `n` integers sorted in ascending order, where each integer satisfies 0 <= `x[i]` <= 1000; `y` is a list of `n` integers sorted in ascending order, where each integer satisfies 0 <= `y[i]` <= 1000; the sum of the elements in `x` is equal to the sum of the elements in `y`. If `x` is equal to `y`, the output is 'Yes'. Otherwise, if `x` is not equal to `y`, the output is 'No'.
    #State of the program after the if-else block has been executed: *`n` is the input integer such that 1 <= `n` <= 50; `x` is a list of `n` integers derived from the input where each integer satisfies 0 <= `x[i]` <= 1000; `y` is a list of `n` integers derived from input, each satisfying 0 <= `y[i]` <= 1000. If the sum of the integers in `x` is not equal to the sum of the integers in `y`, the output is 'No'. Otherwise, if the sums are equal and `x` is equal to `y`, the output is 'Yes'; if the sums are equal but `x` is not equal to `y`, the output is 'No'.
#Overall this is what the function does:The function accepts a positive integer `n` (1 <= n <= 50) and two lists of `n` integers (`x` and `y`), where each integer in `x` and `y` is within the range 0 to 1000. It checks if the sums of the integers in `x` and `y` are equal. If the sums are not equal, it prints 'No'. If the sums are equal, it sorts both lists and checks if the sorted lists are identical; it prints 'Yes' if they are the same and 'No' if they are not. The function has no return value but prints the result based on the comparisons.

