#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and x and y are lists of n integers each, where 0 ≤ x[i] ≤ 1000 and 0 ≤ y[i] ≤ 1000 for all i in range(n).
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
        #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 50 (inclusive), `x` is a list of `n` integers sorted in ascending order, and `y` is a list of `n` integers sorted in ascending order (potentially different from the original order). If `x` is equal to `y`, the function continues without any change. If `x` is not equal to `y`, the console prints 'No'.
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 50 (inclusive), `x` is a list of `n` integers, and `y` is a list of `n` integers. If the sum of elements in `x` is not equal to the sum of elements in `y`, the function prints 'No'. Otherwise, `x` is sorted in ascending order and `y` is sorted in ascending order. If the sorted `x` is equal to the sorted `y`, the function continues without any change. If `x` is not equal to `y`, the console prints 'No'.
#Overall this is what the function does:The function accepts an integer `n` and two lists `x` and `y`, each containing `n` integers. It first checks if the sum of elements in `x` is equal to the sum of elements in `y`. If not, it prints 'No' and exits. If the sums are equal, it sorts both lists `x` and `y` in ascending order. After sorting, it checks if the sorted lists are equal. If they are equal, it prints 'Yes'; otherwise, it prints 'No'. The final state of the program after the function concludes is that `x` and `y` are either printed as 'Yes' or 'No', and the input values are no longer modified within the function. Potential edge cases include when `n` is at its boundaries (1 or 50), and when the lists `x` and `y` contain identical elements in different orders.

