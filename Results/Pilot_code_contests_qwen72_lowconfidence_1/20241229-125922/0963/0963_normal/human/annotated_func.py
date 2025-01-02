#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100, and the array is a list of (2·n - 1) integers where each element does not exceed 1000 in absolute value.
def func():
    INT_MIN = -1000000007
    if (__name__ == '__main__') :
        n = int(raw_input())
        a = sorted([int(x) for x in raw_input().split()])
        res = INT_MIN
        for i in range(0, 2 * n, 2 - n % 2):
            res = max(res, sum([(-x) for x in a[:i]] + a[i:]))
            
        #State of the program after the  for loop has been executed: `n` is the input integer, `a` is the initial sorted list of (2·n - 1) integers, `INT_MIN` is -1000000007, `res` is the maximum value of `sum([(-x) for x in a[:i]] + a[i:])` for all `i` in the range `0, 2 - n % 2, 4 - n % 2, ..., 2 * n - (2 - n % 2)`, `i` is `2 * n - (2 - n % 2)`.
        print(res)
    #State of the program after the if block has been executed: *`n` is an integer such that 2 ≤ n ≤ 100, and the array `a` is a sorted list of (2·n - 1) integers where each element does not exceed 1000 in absolute value. `INT_MIN` is -1000000007. If the program is being executed as the main module, `res` is printed, and `i` is set to `2 * n - (2 - n % 2)`.
#Overall this is what the function does:The function `func` reads an integer `n` (where 2 ≤ n ≤ 100) and a list of (2·n - 1) integers from the user input. It then sorts the list and calculates the maximum possible value of the sum of the elements in the list, where the sign of the first `i` elements is flipped (i.e., multiplied by -1), and `i` ranges from 0 to (2·n - 1) in steps defined by `2 - n % 2`. The function prints the maximum value found. After execution, `n` remains the same, the list `a` is sorted, `INT_MIN` is -1000000007, and the maximum value `res` is printed. Note that the function only performs these actions if it is being executed as the main module. If the function is imported and called from another module, it does nothing.

