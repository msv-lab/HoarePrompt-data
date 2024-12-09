#State of the program right berfore the function call: n is a positive integer (1 <= n <= 50), x is a list of n non-negative integers where each integer x[i] (0 <= x[i] <= 1000) represents the number of stones in the i-th pile during the first visit, and y is a list of n non-negative integers where each integer y[i] (0 <= y[i] <= 1000) represents the number of stones in the i-th pile during the second visit.
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
        #State of the program after the if-else block has been executed: *`n` is an input integer; `x` is a sorted list of integers from input; `y` is a sorted list of non-negative integers derived from input (where each y[i] satisfies 0 <= y[i] <= 1000) and the sum of the elements in `x` is equal to the sum of the elements in `y`. If `x` is equal to `y`, 'Yes' has been printed. Otherwise, if `x` is not equal to `y`, the output is 'No'.
    #State of the program after the if-else block has been executed: *`n` is an input integer; `x` is a list of integers from input; `y` is a sorted list of non-negative integers derived from input (where each y[i] satisfies 0 <= y[i] <= 1000). If the sum of the elements in `x` is not equal to the sum of the elements in `y`, the program prints 'No'. Otherwise, if the sums are equal, the program checks if `x` is equal to `y`: if they are equal, it prints 'Yes'; if they are not equal, it prints 'No'.
#Overall this is what the function does:The function accepts two lists of non-negative integers, `x` and `y`, which represent the number of stones in piles during two visits. It first checks if the total number of stones in both lists is equal; if not, it prints 'No'. If the totals are equal, it sorts both lists and checks if they are identical. If they are, it prints 'Yes'; otherwise, it prints 'No'. The function does not explicitly take `n` as a parameter, and there is no validation for the input values beyond ensuring they are non-negative integers within specified bounds.

