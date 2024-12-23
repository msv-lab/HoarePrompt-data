#State of the program right berfore the function call: n is a non-negative integer (0 ≤ n ≤ 2,000,000,000), and k is a positive integer (1 ≤ k ≤ 9).
def func():
    n, k = map(str, input().split())
    k = int(k)
    count_zeros = 0
    to_remove = 0
    for digit in reversed(n):
        if digit == '0':
            count_zeros += 1
        else:
            to_remove += 1
        
        if count_zeros == k:
            break
        
    #State of the program after the  for loop has been executed: `n` is greater than or equal to 0, `count_zeros` is equal to the number of trailing zeros in `n`, `to_remove` is equal to the number of non-zero digits encountered before reaching `k` trailing zeros, and `k` is a positive integer.
    if (count_zeros == k) :
        print(to_remove)
    else :
        print(len(n) - 1)
    #State of the program after the if-else block has been executed: *`n` is greater than or equal to 0. If `count_zeros` is equal to `k`, the value of `to_remove` is printed. Otherwise, if `count_zeros` is not equal to `k`, an invalid operation for a numeric type occurs, as `len(n) - 1` cannot be processed.
#Overall this is what the function does:The function reads a non-negative integer `n` (up to 2 billion) and a positive integer `k` (between 1 and 9) from input, and processes `n` to determine the number of digits to remove if `n` has exactly `k` trailing zeros. If exactly `k` trailing zeros are found, it prints the number of non-zero digits encountered before the `k` trailing zeros. If there are not exactly `k` trailing zeros, it prints `len(n) - 1`, which corresponds to one less than the length of the string representation of `n`. However, since `len(n)` represents the number of characters in the string and not a direct numeric computation, it may be misleading to imply that an invalid operation could occur, but ultimately it yields a valid integer output. Thus, the function does not explicitly handle cases where `n` has fewer than `k` trailing zeros effectively beyond providing a fallback computation.

