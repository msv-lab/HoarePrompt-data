#State of the program right berfore the function call: n is a non-negative integer not exceeding 2,000,000,000, and k is a positive integer such that 1 <= k <= 9.
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
        
    #State of the program after the  for loop has been executed: `n` is a string representation of a non-negative integer not exceeding 2,000,000,000; `k` is an integer between 1 and 9; `count_zeros` is the number of '0' digits found in the last `k` digits of `n`; `to_remove` is the number of non-zero digits found in the last `k` digits of `n`. If the loop does not execute, `count_zeros` and `to_remove` remain 0.
    if (count_zeros == k) :
        print(to_remove)
    else :
        print(len(n) - 1)
    #State of the program after the if-else block has been executed: *`n` is a string representation of a non-negative integer not exceeding 2,000,000,000; `k` is an integer between 1 and 9. If `count_zeros` equals `k`, then `to_remove` is 0. Otherwise, `count_zeros` is 0, `to_remove` is the number of non-zero digits found in the last `k` digits of `n`, which is less than `k`; the output of the print statement is the length of `n` minus 1.
#Overall this is what the function does:The function accepts a non-negative integer `n` (up to 2,000,000,000) and a positive integer `k` (1 to 9). It counts the number of trailing zeros in `n`. If exactly `k` zeros are found, it prints the number of non-zero digits before the zeros. If fewer than `k` zeros are found, it prints the length of `n` minus one. If `n` has no digits, it will still handle printing based on the checks performed.

