#State of the program right berfore the function call: The input consists of two integers, n and k, where n is a non-negative integer less than or equal to 2,000,000,000 and k is a positive integer between 1 and 9 (inclusive).
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
        
    #State of the program after the  for loop has been executed: `n` is a string representation of a non-negative integer less than or equal to 2,000,000,000, `k` is an integer between 1 and 9 (inclusive), `count_zeros` is the number of trailing zeros in `n` up to `k`, and `to_remove` is the number of non-zero digits from the end of `n` until the last of the `k` zeros or the start of `n` if fewer than `k` zeros exist.
    if (count_zeros == k) :
        print(to_remove)
    else :
        print(len(n) - 1)
    #State of the program after the if-else block has been executed: `n` is a string representation of a non-negative integer less than or equal to 2,000,000,000, `k` is an integer between 1 and 9 (inclusive), `count_zeros` is the number of trailing zeros in `n` up to `k`, and `to_remove` is the number of non-zero digits from the end of `n` until the last of the `k` zeros or the start of `n` if fewer than `k` zeros exist. If `count_zeros` equals `k`, then the value of `to_remove` has been returned. Otherwise, the number of trailing zeros in `n` is less than `k`, and a value of `len(n) - 1` has been printed.
#Overall this is what the function does:The function accepts two integers as input, `n` and `k`, where `n` is a non-negative integer less than or equal to 2,000,000,000 and `k` is a positive integer between 1 and 9 (inclusive). It processes the string representation of `n` from right to left, counting trailing zeros until it finds `k` zeros or reaches the start of `n`. If it finds `k` zeros, it returns the number of non-zero digits encountered after the last of these `k` zeros. If it doesn't find `k` zeros, it returns the length of `n` minus 1. The function doesn't explicitly handle edge cases such as `n` being 0 or `k` being greater than the number of digits in `n`, but based on the code, in such cases, it will either return 0 (if `n` has fewer than `k` zeros and is not a single digit) or the length of `n` minus 1 (if `n` has fewer than `k` zeros). The function does not raise any error messages for specific inputs as suggested in the overall description, but rather follows the logic described in the step-by-step annotations and code.

