#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and x and y are lists of integers such that the length of x and y is n, and 0 ≤ x[i] ≤ 1000 and 0 ≤ y[i] ≤ 1000 for all i in range(n).
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
        #State of the program after the if-else block has been executed: *`n` is an integer input from the user, `x` is a sorted list of integers of length `n`, `y` is a list of length `n` with elements converted from the input integers, the sum of the elements in `x` is equal to the sum of the elements in `y`, and `y` is sorted. If `x` is equal to `y`, the console displays 'Yes'. Otherwise, the console displays 'No'.
    #State of the program after the if-else block has been executed: *`n` is an integer input from the user, `x` is a list of integers of length `n`, and `y` is a list of length `n` with elements converted from the input integers. If the sum of elements in list `x` is not equal to the sum of elements in list `y`, the console prints 'No'. Otherwise, `x` is sorted, and `y` is also sorted. If `x` equals `y`, the console displays 'Yes'. Otherwise, the console displays 'No'.
#Overall this is what the function does:The function `func()` takes no explicit parameters but reads three inputs from the user: an integer `n` and two lists of integers `x` and `y` of length `n`. It first checks if the sums of the elements in `x` and `y` are equal. If they are not equal, it prints 'No'. If they are equal, it sorts both `x` and `y` and then checks if the sorted lists are identical. If the sorted lists are identical, it prints 'Yes'; otherwise, it prints 'No'. The function does not return anything but modifies and prints the results based on the comparison of the lists and their sums. Potential edge cases include when `n` is less than 1 or greater than 50, which is not checked within the function, and the possibility of empty lists or non-integer inputs, which could cause issues with the input parsing.

