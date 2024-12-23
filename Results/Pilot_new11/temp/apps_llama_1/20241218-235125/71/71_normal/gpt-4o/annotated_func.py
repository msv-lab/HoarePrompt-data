#State of the program right berfore the function call: n is an integer and k is a positive integer between 1 and 9, such that 0 <= n <= 2,000,000,000.
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
        
    #State of the program after the  for loop has been executed: `n` is a string, `k` is an integer, `count_zeros` is either equal to `k` if `k` '0's were found from the end of `n`, or less than `k` if the end of `n` was reached without finding `k` '0's, and `to_remove` is the count of non-'0' digits encountered before the loop terminated.
    if (count_zeros == k) :
        print(to_remove)
    else :
        print(len(n) - 1)
    #State of the program after the if-else block has been executed: `n` is a string, `k` is an integer, `count_zeros` is either equal to `k` if `k` '0's were found from the end of `n`, or less than `k` if the end of `n` was reached without finding `k` '0's, and `to_remove` is the count of non-'0' digits encountered before the loop terminated. If `count_zeros` equals `k`, then the value of `to_remove` has been printed. Otherwise, if `count_zeros` is less than `k`, the length of `n` minus 1, which is equal to `len(n) - 1`, has been printed.
#Overall this is what the function does:The function accepts two parameters, `n` and `k`, where `n` is a string representation of an integer and `k` is a positive integer between 1 and 9. It calculates the number of non-zero digits from the end of `n` until it encounters `k` zeros or reaches the beginning of `n`. If `k` zeros are found, it prints the count of non-zero digits encountered before the `k` zeros. If `k` zeros are not found, it prints the length of `n` minus 1. The function does not handle cases where `n` is an empty string, `k` is outside the specified range, or `n` contains non-digit characters. After the function concludes, the state of the program is that a value has been printed to the console, which is either the count of non-zero digits or the length of `n` minus 1, and the input parameters `n` and `k` remain unchanged.

