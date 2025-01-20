#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 50; x and y are lists of n integers each, where 0 ≤ x_i, y_i ≤ 1000 for all i.
def func():
    n = int(input())

x = list(map(int, input().split()))

y = list(map(int, input().split()))

total_x = sum(x)

total_y = sum(y)
    if (total_y > total_x) :
        print('No')
    else :
        print('Yes')
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ n ≤ 50, `x` is a list of n integers each in the range [0, 1000], `y` is a list of n integers each in the range [0, 1000], `total_x` is the sum of the elements in `x`, `total_y` is the sum of the elements in `y`. If `total_y` > `total_x`, the program maintains these conditions without further changes. If `total_y` ≤ `total_x`, 'Yes' has been printed to the console.
#Overall this is what the function does:The function reads an integer `n` and two lists `x` and `y` of `n` integers each from the standard input. It then calculates the sums of the elements in `x` and `y`. If the sum of the elements in `y` is greater than the sum of the elements in `x`, the function prints "No". Otherwise, it prints "Yes". The function does not return any value. After the function executes, `n` remains an integer such that 1 ≤ n ≤ 50, `x` and `y` remain lists of `n` integers each in the range [0, 1000], and the sums `total_x` and `total_y` are calculated but not used further.

