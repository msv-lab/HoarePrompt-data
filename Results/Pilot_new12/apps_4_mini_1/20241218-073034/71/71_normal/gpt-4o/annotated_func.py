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
        
    #State of the program after the  for loop has been executed: `n` is a non-empty string, `k` is a positive integer, `count_zeros` is the number of zeros in `n` (or `k` if `k` zeros were found), `to_remove` is the number of non-zero digits checked before reaching `k` zeros (or total non-zero digits if `count_zeros` is less than `k`).
    if (count_zeros == k) :
        print(to_remove)
    else :
        print(len(n) - 1)
    #State of the program after the if-else block has been executed: *`n` is a non-empty string, `k` is a positive integer. If the number of zeros in `n` equals `k`, `to_remove` is printed. If the number of zeros in `n` is less than `k`, `to_remove` represents the non-zero digits checked before reaching `count_zeros`, and the output printed is `len(n) - 1`.
#Overall this is what the function does:The function reads a non-empty string representation of a non-negative integer `n` and a positive integer `k` from input. It counts the number of trailing zeros in `n`, determining how many non-zero digits were encountered before reaching `k` zeros. If exactly `k` zeros are found at the end of `n`, it outputs the count of non-zero digits found before the zeros. If the number of zeros is less than `k`, it outputs the length of the string `n` minus one (which considers all digits but one). Therefore, the function effectively calculates a measure based on the number of zeros and non-zero digits in the input number `n`, with specific handling when the conditions are not met. The function has no defined return value and instead prints the result directly to the console.

