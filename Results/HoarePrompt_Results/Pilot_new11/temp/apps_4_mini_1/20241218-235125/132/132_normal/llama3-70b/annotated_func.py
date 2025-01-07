#State of the program right berfore the function call: n is an integer such that 1 <= n <= 50, x is a list of n integers where each integer is within the range 0 <= x[i] <= 1000, and y is a list of n integers where each integer is within the range 0 <= y[i] <= 1000.
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
        #State of the program after the if-else block has been executed: *`n` is an input integer, `x` and `y` are sorted lists of `n` integers based on user input with their sums equal. If `x` is equal to `y`, then both lists are identical. Otherwise, `x` and `y` are distinct sorted lists of `n` integers but still have equal sums.
    #State of the program after the if-else block has been executed: *`n` is an input integer, `x` is a list of `n` integers, and `y` is a list of `n` integers. If the sum of `x` is not equal to the sum of `y`, 'No' is printed. Otherwise, if the sums are equal, `x` and `y` are sorted lists of `n` integers, and if `x` is equal to `y`, then both lists are identical. If `x` is not equal to `y`, then they are distinct sorted lists of `n` integers but still have equal sums.
#Overall this is what the function does:The function accepts no parameters directly; instead, it takes user input to read an integer `n`, followed by two lists `x` and `y`, each containing `n` integers. If the sums of the lists `x` and `y` are not equal, it prints 'No'. If the sums are equal, it proceeds to sort both lists. It then checks if the sorted lists `x` and `y` are identical. If they are, it prints 'Yes'; if not, it prints 'No'. After completion, the state of the program includes the input integer `n`, and two sorted lists `x` and `y`, provided both lists originally had equal sums. Edge cases where either `x` or `y` contains distinct values with the same sum are considered, and in such cases, 'No' will be printed, confirming the lists are not identical despite equal sums. The overall functionality does not return any values; it solely outputs result strings based on comparisons.

