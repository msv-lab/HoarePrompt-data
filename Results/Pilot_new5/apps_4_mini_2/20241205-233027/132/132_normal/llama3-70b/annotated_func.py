#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 50; x is a list of integers where each element x_i (0 <= x_i <= 1000) represents the number of stones in pile i during the first visit; y is a list of integers where each element y_i (0 <= y_i <= 1000) represents the number of stones in pile i during the second visit, and both x and y have length n.
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
        #State of the program after the if-else block has been executed: *`n` is a positive integer such that `1 <= n <= 50`; `x` is a sorted list of integers representing the number of stones in pile `i` during the first visit; `y` is a sorted list of integers such that the sum of the elements in `x` is equal to the sum of the elements in `y`. If `x` is equal to `y`, 'Yes' has been printed. Otherwise, the lists `x` and `y` are not equal.
    #State of the program after the if-else block has been executed: *`n` is a positive integer such that `1 <= n <= 50`. If the sum of the elements in list `x` is not equal to the sum of the elements in list `y`, then 'No' is printed. Otherwise, if the sums are equal and lists `x` and `y` are identical, 'Yes' is printed. If the sums are equal but the lists are not identical, no specific output is stated, but the sum condition is satisfied.
#Overall this is what the function does:The function accepts two lists of integers, `x` and `y`, representing the number of stones in corresponding piles during two visits. It checks if the sum of the stones in `x` is equal to the sum of the stones in `y`. If the sums are not equal, it prints 'No'. If the sums are equal, it then checks if the sorted lists `x` and `y` are identical; if they are, it prints 'Yes', otherwise, it prints 'No'. However, if the sums are equal but the lists are not identical, no output is specified, which is a missing functionality in the annotations.

