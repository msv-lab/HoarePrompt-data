#State of the program right berfore the function call: n is a non-negative integer less than or equal to 2,000,000,000, and k is a positive integer such that 1 <= k <= 9.
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
        
    #State of the program after the  for loop has been executed: `count_zeros` is the number of trailing zeros in the integer represented by `n`, `to_remove` is the number of non-zero digits before the last `k` zeros, `n` is a non-empty string representing a non-negative integer less than or equal to 2,000,000,000; `k` is an integer between 1 and 9.
    if (count_zeros == k) :
        print(to_remove)
    else :
        print(len(n) - 1)
    #State of the program after the if-else block has been executed: *`count_zeros` is the number of trailing zeros in the integer represented by `n`, `to_remove` is the number of non-zero digits before the last `k` zeros, `n` is a non-empty string representing a non-negative integer less than or equal to 2,000,000,000, and `k` is an integer between 1 and 9. If `count_zeros` is equal to `k`, the value of `to_remove` is unknown. Otherwise, the length of `n` is greater than 0.
#Overall this is what the function does:The function accepts a non-negative integer `n` (up to 2,000,000,000 represented as a string) and a positive integer `k` (between 1 and 9). It counts the number of trailing zeros in `n`. If the number of trailing zeros equals `k`, it prints the number of non-zero digits before these trailing zeros. If the count of trailing zeros is not equal to `k`, it prints the length of `n` minus one. Thus, it handles cases where `n` might have fewer than `k` trailing zeros and prints the length of the number minus one when such a condition occurs.

