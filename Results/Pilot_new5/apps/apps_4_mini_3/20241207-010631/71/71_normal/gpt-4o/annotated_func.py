#State of the program right berfore the function call: n is a non-negative integer between 0 and 2,000,000,000, and k is a positive integer between 1 and 9.
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
        
    #State of the program after the  for loop has been executed: `count_zeros` is equal to the number of '0's in `n` from the right until `k` is reached or the end of the string is reached, `to_remove` is equal to the number of non-zero digits encountered before reaching `k` zeros, `n` is the original string representation of the non-negative integer. If `count_zeros` is less than `k`, the loop has iterated over all digits of `n` without finding enough zeros.
    if (count_zeros == k) :
        print(to_remove)
    else :
        print(len(n) - 1)
    #State of the program after the if-else block has been executed: *`count_zeros` is the number of '0's in `n` from the right until `k` is reached or the end of the string is reached, `to_remove` is the number of non-zero digits encountered before reaching `k` zeros, and `n` is the original string representation of the non-negative integer. If `count_zeros` is equal to `k`, then `to_remove` is printed. Otherwise, `len(n) - 1` has been printed, indicating that the output is `len(n) - 1`.
#Overall this is what the function does:The function accepts a non-negative integer `n` (as a string) and a positive integer `k`. It counts the number of trailing zeros in `n` from the right and also counts the number of non-zero digits encountered before reaching `k` zeros. If `k` zeros are found, it prints the count of non-zero digits. If fewer than `k` zeros are found in `n`, it prints the length of `n` minus one. This indicates that if there are not enough trailing zeros, the function will output the length of the number minus one, which could lead to misleading results depending on the input.

