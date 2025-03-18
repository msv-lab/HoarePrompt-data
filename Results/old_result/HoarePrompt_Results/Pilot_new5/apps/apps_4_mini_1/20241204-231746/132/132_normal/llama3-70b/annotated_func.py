#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 50, x is a list of n non-negative integers where each integer x_i is in the range 0 <= x_i <= 1000, and y is a list of n non-negative integers where each integer y_i is also in the range 0 <= y_i <= 1000.
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
        #State of the program after the if-else block has been executed: *`n` is an input positive integer such that 1 <= `n` <= 50; `x` is a sorted list of `n` non-negative integers; `y` is a sorted list of `n` non-negative integers where each integer `y_i` is in the range 0 <= `y_i` <= 1000; the sum of the elements in `x` is equal to the sum of the elements in `y`. If the lists `x` and `y` are equal, 'Yes' has been printed. If the lists `x` and `y` are not equal, 'No' has been printed.
    #State of the program after the if-else block has been executed: *`n` is an input positive integer such that 1 <= `n` <= 50; `x` is a list of `n` non-negative integers; `y` is a list of `n` non-negative integers where each integer `y_i` is in the range 0 <= `y_i` <= 1000. If the sum of the elements in `x` is not equal to the sum of the elements in `y`, 'No' has been printed. If the sum of the elements in `x` is equal to the sum of the elements in `y`, then if the lists `x` and `y` are equal, 'Yes' has been printed; otherwise, 'No' has been printed.
#Overall this is what the function does:The function accepts a positive integer `n` and two lists `x` and `y`, each containing `n` non-negative integers. It checks if the sums of the elements in `x` and `y` are equal. If the sums are not equal, it prints 'No'. If the sums are equal, it then checks if the sorted versions of `x` and `y` are identical, printing 'Yes' if they are and 'No' if they are not. The function does not return any value; it simply prints the results based on the comparisons.

