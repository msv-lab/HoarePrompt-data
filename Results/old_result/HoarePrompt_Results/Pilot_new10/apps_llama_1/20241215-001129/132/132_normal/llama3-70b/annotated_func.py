#State of the program right berfore the function call: The input will contain an integer n (1 <= n <= 50), followed by two lists of n integers (0 <= x_i, y_i <= 1000).
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
        #State of the program after the if-else block has been executed: `n` is an integer between 1 and 50 (inclusive), `x` is a sorted list of input integers, `y` is a sorted list of input integers, and the sum of the elements in `x` is equal to the sum of the elements in `y`. If `x` is equal to `y`, 'Yes' has been printed; otherwise, 'No' has been printed to the console.
    #State of the program after the if-else block has been executed: `n` is an integer between 1 and 50 (inclusive), `x` is a list of input integers, `y` is a list of input integers. If the sum of the elements in `x` is not equal to the sum of the elements in `y`, then 'No' has been printed to the console. If the sum of the elements in `x` is equal to the sum of the elements in `y`, then `x` and `y` are sorted lists, and if `x` is equal to `y`, 'Yes' has been printed; otherwise, 'No' has been printed to the console.
#Overall this is what the function does:The function accepts an integer n and two lists of n integers as input, checks if their sums are equal, and if so, checks if the sorted lists are equal, printing 'Yes' if they are equivalent and 'No' otherwise.

