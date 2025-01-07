#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50, and x and y are lists of integers such that len(x) == len(y) == n and 0 ≤ x[i] ≤ 1000 and 0 ≤ y[i] ≤ 1000 for all i in range(n).
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
        #State of the program after the if-else block has been executed: `n` is an integer between 1 and 50; `x` is a list of integers with length `n`, sorted in ascending order; `y` is a list of integers with length `n`, containing integers entered by the user and sorted in ascending order; the sum of elements in `x` is equal to the sum of elements in `y`; if `x` is equal to `y`, then 'Yes' is printed to the console; otherwise, 'No' is printed to the console.
    #State of the program after the if-else block has been executed: *`n` is an integer between 1 and 50; `x` is a list of integers with length `n`; `y` is a list of integers with length `n`, containing integers entered by the user. If the sum of elements in `x` is not equal to the sum of elements in `y`, the output is 'No'. Otherwise, `x` and `y` are both sorted in ascending order and their sums are equal. If `x` equals `y`, the output is 'Yes'; otherwise, the output is 'No'.
#Overall this is what the function does:The function reads three inputs: an integer `n` and two lists of integers `x` and `y`. It checks if the sum of elements in `x` is equal to the sum of elements in `y`. If not, it prints 'No'. If the sums are equal, it sorts both lists and checks if they are identical. If they are, it prints 'Yes'; otherwise, it prints 'No'.

