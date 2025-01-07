#State of the program right berfore the function call: n is a non-negative integer less than or equal to 2,000,000,000, and k is a positive integer between 1 and 9.
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
        
    #State of the program after the  for loop has been executed: `n` is the original numeric string input, `k` is an integer, `count_zeros` is the count of zeros from the end of `n` until `k` zeros are found or until all digits have been processed, and `to_remove` is the count of non-zero digits from the end of `n` until `k` zeros are found or until all digits have been processed.
    if (count_zeros == k) :
        print(to_remove)
    else :
        print(len(n) - 1)
    #State of the program after the if-else block has been executed: *`n` is the original numeric string input, `k` is an integer, `count_zeros` is the count of zeros from the end of `n` until `k` zeros are found or until all digits have been processed, and `to_remove` is the count of non-zero digits from the end of `n` until `k` zeros are found or until all digits have been processed. If `count_zeros` equals `k`, then `to_remove` has been returned at the output. Otherwise, the value `len(n) - 1` has been printed and the count of zeros from the end of `n` is less than `k`.
#Overall this is what the function does:The function accepts a numeric string `n` and an integer `k`, and prints the count of non-zero digits from the end of `n` until the `k`th zero is found. If `k` zeros are not found, it prints the length of `n` minus one, effectively handling cases where `n` does not contain `k` zeros.

