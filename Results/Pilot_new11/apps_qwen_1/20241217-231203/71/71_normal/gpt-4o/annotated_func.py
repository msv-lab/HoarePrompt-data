#State of the program right berfore the function call: n is an integer such that 0 ≤ n ≤ 2,000,000,000, and k is an integer such that 1 ≤ k ≤ 9.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-empty string, `k` is a non-negative integer, `count_zeros` is the total count of zeros in `n` up to the point where `count_zeros` equals `k` (if `count_zeros` reaches `k`, the loop breaks), `to_remove` is the number of digits in `n` that have not been processed when the loop breaks or 0 if the loop does not execute.
    if (count_zeros == k) :
        print(to_remove)
    else :
        print(len(n) - 1)
    #State of the program after the if-else block has been executed: *`n` is a non-empty string, `k` is a non-negative integer, `count_zeros` is the total count of zeros in `n` up to the point where `count_zeros` equals `k` (if `count_zeros` reaches `k`, the loop breaks), `to_remove` is the number of digits in `n` that have not been processed when the loop breaks or 0 if the loop does not execute, if `count_zeros` equals `k`, the value of `to_remove` is printed; otherwise, the printed value is `len(n) - 1`.
#Overall this is what the function does:The function `func()` accepts two parameters: `n` (an integer where \(0 \leq n \leq 2,000,000,000\)) and `k` (an integer where \(1 \leq k \leq 9\)). It processes the string representation of `n` in reverse order to count the number of zeros until the count reaches `k`. Once `k` zeros are found, it calculates the number of digits in `n` that have not been processed and prints this value. If the loop exits without finding exactly `k` zeros, it prints `len(n) - 1`. The function ensures that both `n` and `k` are within their specified ranges. If `n` is less than 0 or `k` is out of the range \(1 \leq k \leq 9\), the function would encounter errors due to invalid inputs, although no explicit error handling is shown in the code.

